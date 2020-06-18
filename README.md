# tflite-analyser

https://github.com/oxmlsys/tflite-tools/blob/master/tflite_tools


```bash

make pipup;
make clean_venv;
make venv;
source ./venv/bin/activate;
./install_venv.sh;
pip freeze;


```



Install flatc

solution for flatc and flatbuffers for linux ubuntu :

```
choice "folder for installation"
cd "folder for installation"
git clone https://github.com/google/flatbuffers.git
cd flatbuffers
cmake -G "Unix Makefiles"
make
sudo ln -s /full-path-to-flatbuffer/flatbuffers/flatc /usr/local/bin/flatc
chmod +x /full-path-to-flatbuffer/flatbuffers/flatc
run in any place as "flatc"
```

Git/tflite-analyser$ flatc --version
flatc version 1.12.0


/Git/tflite-analyser$ pip freeze
absl-py==0.9.0
astor==0.8.1
flatbuffers==1.12
gast==0.3.3
google-pasta==0.2.0
grpcio==1.29.0
h5py==2.10.0
importlib-metadata==1.6.1
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.2
Markdown==3.2.2
numpy==1.16.1
protobuf==3.12.2
six==1.15.0
tensorboard==1.14.0
tensorflow==1.14.0
tensorflow-estimator==1.14.0
termcolor==1.1.0
Werkzeug==1.0.1
wrapt==1.12.1
zipp==3.1.0

