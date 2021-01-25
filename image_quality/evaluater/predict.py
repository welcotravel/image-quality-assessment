
import os
import glob
import json
import argparse
import urllib
import tempfile
import shutil
import sys
from sys import platform
import image_quality
from image_quality.utils.utils import calc_mean_score, save_json
from image_quality.handlers.model_builder import Nima
from image_quality.handlers.data_generator import TestDataGenerator
from PIL import ImageFile, Image
from keras import backend as K
import videokf as vf

TOOLS_PATH = '/usr/bin/'
if platform == 'darwin':
  TOOLS_PATH = '/usr/local/bin/'

FFMPEG_PATH =os.path.join(TOOLS_PATH,'ffmpeg')
FFPROBE_PATH =os.path.join(TOOLS_PATH,'ffprobe')

def fetch_model():
  # download model
  dirname = os.path.dirname(__file__)
  working_path = '/tmp/image_quality/models/MobileNet'
  model_files = [
    'config_aesthetic_cpu.json',
    'config_aesthetic_gpu.json',
    'config_technical_cpu.json',
    'config_technical_gpu.json',
    'weights_mobilenet_aesthetic_0.07.hdf5',
    'weights_mobilenet_technical_0.11.hdf5',
  ]

  files_exist = True
  for model_file in model_files:
    file_path   = os.path.join(working_path,model_file)
    files_exist = files_exist and os.path.exists(file_path)
  if not files_exist:
    os.system(os.path.join(dirname,'../','download.sh'))

def image_file_to_json(img_path):
  img_dir = os.path.dirname(img_path)
  img_id = os.path.basename(img_path)

  return img_dir, [{'image_id': img_id}]


def image_dir_to_json(img_dir, img_type=None):
  img_paths = []
  if img_type:
    img_paths = glob.glob(os.path.join(img_dir, '*.'+img_type))
  else:
    img_paths = glob.glob(os.path.join(img_dir, '*'))

  samples = []
  for img_path in img_paths:
    img_id = os.path.basename(img_path)
    samples.append({'image_id': img_id})
  return samples


def predict(model, data_generator):
  return model.predict(data_generator, workers=8, use_multiprocessing=True, verbose=1)


def main(base_model_name, weights_file, image_source, predictions_file):
  # load samples
  if os.path.isfile(image_source):
    image_dir, samples = image_file_to_json(image_source)
  else:
    image_dir = image_source
    samples = image_dir_to_json(image_dir)

  # build model and load weights
  nima = Nima(base_model_name, weights=None)
  nima.build()
  nima.nima_model.load_weights(weights_file)

  # initialize data generator
  data_generator = TestDataGenerator(samples, image_dir, 64, 10, nima.preprocessing_function())

  # get predictions
  predictions = predict(nima.nima_model, data_generator)

  # calc mean scores and add to samples
  for i, sample in enumerate(samples):
    sample['mean_score_prediction'] = calc_mean_score(predictions[i])

  print(json.dumps(samples, indent=2))

  if predictions_file is not None:
    save_json(samples, predictions_file)


def score_images(model,image_source):
  # load samples
  if os.path.isfile(image_source):
    image_dir, samples = image_file_to_json(image_source)
  else:
    image_dir = image_source
    samples = image_dir_to_json(image_dir)

  ImageFile.LOAD_TRUNCATED_IMAGES = True
  Image.MAX_IMAGE_PIXELS = None

  # initialize data generator
  data_generator = TestDataGenerator(samples, image_dir, 64, 10, model.preprocessing_function())

  # get predictions
  predictions = predict(model.nima_model, data_generator)
  K.clear_session()

  # calc mean scores and add to samples
  for i, sample in enumerate(samples):
    sample['mean_score_prediction'] = calc_mean_score(predictions[i])

  return samples

def score_video(models,url_to_video):
  temp_dir = tempfile.mkdtemp()
  filename = os.path.basename(url_to_video)
  path_to_video = os.path.join(temp_dir,filename)
  urllib.request.urlretrieve(url_to_video, path_to_video)
  vf.extract_keyframes(path_to_video, ffmpeg_exe=FFMPEG_PATH,ffprobe_exe=FFPROBE_PATH,method='iframes')

  results = []
  for model in models:
    scores = score_images(model,os.path.join(temp_dir,'keyframes'))
    print('rank_video scores')
    for score in scores:
      print(score)
    # average 3 highest scores for media score
    vals = []
    for score in scores:
      vals.append(score['mean_score_prediction'])
    top_vals = vals.copy()
    top_vals = sorted(top_vals, reverse=True)
    top_vals = top_vals[:3]
    avg = sum(top_vals)/len(top_vals)
    results.append({'image_id':filename,  'mean_score_prediction': avg, 'scores': vals })

  shutil.rmtree(temp_dir)
  return results


if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('-b', '--base-model-name', help='CNN base model name', required=True)
  parser.add_argument('-w', '--weights-file', help='path of weights file', required=True)
  parser.add_argument('-is', '--image-source', help='image directory or file', required=True)
  parser.add_argument('-pf', '--predictions-file', help='file with predictions', required=False, default=None)

  args = parser.parse_args()

  main(**args.__dict__)
