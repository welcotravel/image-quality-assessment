import sys
import os
import shutil
from image_quality.evaluater.predict import extract_keyframes

video_path = sys.argv[1]
results = extract_keyframes(video_path,[1,3])
print('extract_keyframes results',results)
if results['extracted_frames']:
  for file in results['extracted_frames']:
    base_name = os.path.basename(file)
    shutil.copyfile(file,'./' + base_name)