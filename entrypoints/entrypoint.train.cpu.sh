#!/bin/bash
set -e

# start training
python -W ignore trainer/train.py -j /image-quality-assessment/image_quality/$TRAIN_JOB_DIR -i /image-quality-assessment/image_quality/images
