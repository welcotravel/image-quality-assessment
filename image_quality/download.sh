#!/bin/sh
mkdir -p /tmp/image_quality/models/MobileNet
wget https://s3.amazonaws.com/dev.welco.me/image_quality/model/MobileNet/config_aesthetic_cpu.json
mv config_aesthetic_cpu.json /tmp/image_quality/models/MobileNet/
wget https://s3.amazonaws.com/dev.welco.me/image_quality/model/MobileNet/config_aesthetic_gpu.json
mv config_aesthetic_gpu.json /tmp/image_quality/models/MobileNet/
wget https://s3.amazonaws.com/dev.welco.me/image_quality/model/MobileNet/config_technical_cpu.json
mv config_technical_cpu.json /tmp/image_quality/models/MobileNet/
wget https://s3.amazonaws.com/dev.welco.me/image_quality/model/MobileNet/config_technical_gpu.json
mv config_technical_gpu.json /tmp/image_quality/models/MobileNet/
wget https://s3.amazonaws.com/dev.welco.me/image_quality/model/MobileNet/weights_mobilenet_aesthetic_0.07.hdf5
mv weights_mobilenet_aesthetic_0.07.hdf5 /tmp/image_quality/models/MobileNet/
wget https://s3.amazonaws.com/dev.welco.me/image_quality/model/MobileNet/weights_mobilenet_technical_0.11.hdf5
mv weights_mobilenet_technical_0.11.hdf5 /tmp/image_quality/models/MobileNet/
