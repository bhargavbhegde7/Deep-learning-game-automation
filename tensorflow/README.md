tutorial from https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/
installing gpu tensorflow : https://dzone.com/articles/installing-tensorflow-with-gpu-on-windows-10
(CUDA 9.0 and cuDNN v7.3.1 (Sept 28, 2018), for CUDA 9.0)
docker stuff for tensorflow from https://selfdrivingcars.mit.edu/setting-up-docker-and-tensorflow-for-windows/

docker pull tensorflow/tensorflow

then 

docker run <image>

then

C:\Users\bhegde>docker cp C:\Users\bhegde\Desktop\side\LearnANN\handwriting.py fervent_khorana:/handwriting.py

then

C:\Users\bhegde>docker exec -it fervent_khorana bash

your file will be under root directory