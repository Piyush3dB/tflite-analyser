!#/bin/bash

rm -rf schema.fbs
wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/schema/schema.fbs;
flatc --version
flatc --python schema.fbs