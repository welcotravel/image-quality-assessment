WEIGHTS_FILE=/tmp/image_quality/models/MobileNet/weights_mobilenet_technical_0.11.hdf5
BASE_MODEL_NAME=MobileNet
DOCKER_IMAGE=nima-http
RUN="python evaluater/server.py --base-model-name $BASE_MODEL_NAME --weights-file $WEIGHTS_FILE"

echo $RUN
eval $RUN


