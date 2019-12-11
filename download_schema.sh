!#/bin/bash

rm -rf tflite

wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/schema/schema.fbs

flatc --python schema.fbs

