os: windows 10
cuda: CUDA 9.0
cudnn: cuDNN v7.3.1 (Sept 28, 2018), for CUDA 9.0
gpu: GeForce GTX 1050 Ti major: 6 minor: 1 memoryClockRate(GHz): 1.506
tensorflow: 1.13.0-dev20181018, gpu version
keras: 2.2.4

* run the game.py to play
* run the create_dataset.py file to save samples as well as the labels
* run train_n_test_n_save.py to train, test and save the models based on these screen shots
* run load_n_test.py to load the trained model and test it on the test samples to make sure the saved model works
* run ann_game.py to see the ann play the game by itself








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