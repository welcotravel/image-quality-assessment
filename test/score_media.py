import sys
import shutil
import os
import time
from image_quality.handlers.model_builder import Nima
from image_quality.evaluater.predict import fetch_model,score_video

fetch_model() # ensure model weights are local in image quality path
image_quality_path           = '/tmp/image_quality/'
image_ranking_model_name     = 'MobileNet'
image_ranking_technical_file = os.path.join(image_quality_path,'models/MobileNet/weights_mobilenet_technical_0.11.hdf5')
image_ranking_aesthetic_file = os.path.join(image_quality_path,'models/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5')

technical_model = None
aesthetic_model = None
def load_models():
  global technical_model
  technical_model = Nima(image_ranking_model_name)
  technical_model.build()
  technical_model.nima_model.load_weights(image_ranking_technical_file)
  technical_model.nima_model.summary()
  global aesthetic_model
  aesthetic_model = Nima(image_ranking_model_name)
  aesthetic_model.build()
  aesthetic_model.nima_model.load_weights(image_ranking_aesthetic_file)
  aesthetic_model.nima_model.summary()

load_models()

models =  [technical_model,aesthetic_model]

media_path = sys.argv[1]
ts_start   = time.time_ns()
scores     = score_video(models,media_path)
ts_end     = time.time_ns()
technical_scores = scores[0]['scores']
aesthetic_scores = scores[1]['scores']
print('scores time',(ts_end - ts_start)/(1e9))
