#!/bin/bash
set -e

# start training
python -W ignore trainer/train.py -j /image-quality-assessment/image_quality/$TRAIN_JOB_DIR -i /image-quality-assessment/image_quality/images

# copy train output to s3
aws s3 cp /src/$TRAIN_JOB_DIR s3://$S3_BUCKET/$TRAIN_JOB_DIR --recursive
