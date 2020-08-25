#!/bin/bash
set -e

BASE_MODEL_NAME=$1
WEIGHTS_FILE=$2
IMAGE_SOURCE=$3

# predict
python evaluater/predict.py \
--base-model-name $BASE_MODEL_NAME \
--weights-file $WEIGHTS_FILE \
--image-source $IMAGE_SOURCE
