# tflite-analyser

https://github.com/oxmlsys/tflite-tools/blob/master/tflite_tools


```bash

rm -rf venv
sudo python3.6 -m pip install --upgrade pip
virtualenv -p /usr/bin/python3.6 venv
source ./venv/bin/activate
pip install -r requirements.txt


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



pip install flatbuffers
pip install tensorflow==1.14.0
pip install numpy==1.16.1


pip install -r requirements.txt

