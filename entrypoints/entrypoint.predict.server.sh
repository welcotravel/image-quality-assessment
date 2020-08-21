#!/bin/bash
set -e

BASE_MODEL_NAME=$1
WEIGHTS_FILE=$2

# predict
python -m evaluater.server \
--base-model-name $BASE_MODEL_NAME \
--weights-file $WEIGHTS_FILE

# python -m evaluater.server --base-model-name MobileNet --weights-file /models/MobileNet/weights_mobilenet_technical_0.11.hdf5

