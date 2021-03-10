import sys
import shutil
import os
# from image_quality.handlers.model_builder import Nima
# from image_quality.evaluater.predict import fetch_model,score_video,extract_best_keyframe

# fetch_model() # ensure model weights are local in image quality path
# image_quality_path           = '/tmp/image_quality/'
# image_ranking_model_name     = 'MobileNet'
# image_ranking_technical_file = os.path.join(image_quality_path,'models/MobileNet/weights_mobilenet_technical_0.11.hdf5')
# image_ranking_aesthetic_file = os.path.join(image_quality_path,'models/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5')

# technical_model = None
# aesthetic_model = None
# def load_models():
#   global technical_model
#   technical_model = Nima(image_ranking_model_name)
#   technical_model.build()
#   technical_model.nima_model.load_weights(image_ranking_technical_file)
#   technical_model.nima_model.summary()
#   global aesthetic_model
#   aesthetic_model = Nima(image_ranking_model_name)
#   aesthetic_model.build()
#   aesthetic_model.nima_model.load_weights(image_ranking_aesthetic_file)
#   aesthetic_model.nima_model.summary()

# load_models()

# models =  [technical_model,aesthetic_model]

# video_path = sys.argv[1]
# scores = score_video(models,video_path)
# technical_scores = scores[0]['scores']
# aesthetic_scores = scores[1]['scores']

video_path = sys.argv[1]
from image_quality.evaluater.predict import extract_best_keyframe
technical_scores = [5.346501521766186, 4.848883301019669, 5.329231716692448, 4.224607564508915, 5.301447421312332, 5.5119233429431915, 5.456210754811764]
aesthetic_scores = [5.28801537102845,  4.030074798293072, 8.78550138650462, 5.033853497268865, 4.575664479605621, 4.816268427704927, 4.675694878416834]

print('technical_scores',technical_scores)
print('aesthetic_scores',aesthetic_scores)
results = extract_best_keyframe(video_path,technical_scores,aesthetic_scores)
print('best keyframe results',results)
if results['extracted_frame_path']:
  shutil.copyfile(results['extracted_frame_path'],'./test.jpg')