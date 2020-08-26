# docker run --rm -it -p 5005:5005 nima-http 

WEIGHTS_FILE=/image-quality-assessment/image_quality/models/MobileNet/weights_mobilenet_technical_0.11.hdf5
BASE_MODEL_NAME=MobileNet
DOCKER_IMAGE=nima-http

# DOCKER_RUN="docker run --rm -it -p 5005:5005 nima-http MobileNet image_quality/models/MobileNet/weights_mobilenet_technical_0.11.hdf5"
DOCKER_RUN="docker run --rm -it -p 5005:5005 $DOCKER_IMAGE $BASE_MODEL_NAME $WEIGHTS_FILE"

echo $DOCKER_RUN
eval $DOCKER_RUN


