#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tempfile
from flask import Flask, request, jsonify
import image_quality
from image_quality.evaluater.predict import image_file_to_json, image_dir_to_json, predict, score_images, score_video
from image_quality.utils.utils import calc_mean_score, save_json
import urllib
import shutil
import argparse
from keras import backend as K
from PIL import ImageFile, Image
from image_quality.handlers.model_builder import Nima
from image_quality.handlers.data_generator import TestDataGenerator

app = Flask('server')

def load_model(config):
  global model
  model = Nima(config.base_model_name)
  model.build()
  model.nima_model.load_weights(config.weights_file)
  # model.nima_model._make_predict_function()  # https://github.com/keras-team/keras/issues/6462
  model.nima_model.summary()

# todo handle arbitrary media, identify type
# https://pypi.org/project/python-libmagic/

@app.route('/predict_images', methods=['POST'])
def predict_images():
  global images

  if request.method == 'POST':
    images = request.json
    print('images',images)

    if images:
      temp_dir = tempfile.mkdtemp()
      for image in images:
        filename_w_ext = os.path.basename(image)
        try:
          urllib.request.urlretrieve(image, os.path.join(temp_dir,filename_w_ext))
        except:
          print('An exception occurred :' + image)
        # print('file dest exists?',os.path.exists(os.path.join(temp_dir,filename_w_ext)))


      result = score_images(model,temp_dir)
      shutil.rmtree(temp_dir)
      return jsonify(result)

    return jsonify({'error': 'Image is not available'})

@app.route('/predict_videos', methods=['POST'])
def predict_videos():
  global videos

  if request.method == 'POST':
    videos = request.json
    print('videos',videos)

    result = []
    if videos:
      for video in videos:
        ares = score_video([model],video)
        result.append(ares[0])
      return jsonify(result)

    return jsonify({'error': 'Video is not available'})

if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('-b', '--base-model-name', help='CNN base model name', required=True)
  parser.add_argument('-w', '--weights-file', help='path of weights file', required=True)
  args = parser.parse_args()

  load_model(args)
  app.run(host='0.0.0.0', port=5005)