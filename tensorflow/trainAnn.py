import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np


#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

'''

screenshots 1 to 194775
train 1 to 194575
test 194576 to 194775

'''
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import re

DATADIR = "screenshots"
LABELFILE = "labels.txt"

TRAINING_COUNT = 20000
LAST_NUMBER = 21000

training_data_samples = []
def create_training_samples():
	#for imgName in range(1, 194776):
	path = os.path.join(DATADIR)
	
	IMG_SIZE = 100
	for img in tqdm(range(1, TRAINING_COUNT+1)):
		try:
			img_array = cv2.imread(os.path.join(path,str(img)+".jpeg") ,cv2.IMREAD_GRAYSCALE)
			new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
			training_data_samples.append(new_array)
		except Exception as e:
			print(e)
			pass

test_data_samples = []
def create_test_samples():
	#for imgName in range(1, 194776):
	path = os.path.join(DATADIR)
	
	IMG_SIZE = 100
	for img in tqdm(range(TRAINING_COUNT+1, LAST_NUMBER+1)):
		try:
			img_array = cv2.imread(os.path.join(path,str(img)+".jpeg") ,cv2.IMREAD_GRAYSCALE)
			new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
			test_data_samples.append(new_array)
		except Exception as e:
			print(e)
			pass

training_data_labels = []
def create_training_labels():
	count = 1
	img_name = ""
	with open(LABELFILE) as f:
		for line in f:
			if count >= TRAINING_COUNT+1:
				break
			array_of_words = line.split(',')
			training_data_labels.append(int(array_of_words[1]))
			img_name = array_of_words[0]
				
			count += 1

test_data_labels = []
def create_test_labels():
	count = 1
	img_name = ""
	with open(LABELFILE) as f:
		for line in f:
			if count > TRAINING_COUNT and count < LAST_NUMBER+1:
				array_of_words = line.split(',')
				test_data_labels.append(int(array_of_words[1]))
				img_name = array_of_words[0]
				
			count += 1

create_training_samples()
create_training_labels()

create_test_samples()
create_test_labels()

x_train = training_data_samples
y_train = np.zeros((20000,), dtype=int)
for index, val in enumerate(training_data_labels):
	y_train[index] = val
#y_train = training_data_labels

x_test = test_data_samples
y_test = np.zeros((1000,), dtype=int)
for index, val in enumerate(test_data_labels):
	y_test[index] = val
#y_test = test_data_labels



#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------



x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1
x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1

model = tf.keras.models.Sequential()  # a basic feed-forward model
model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track

model.fit(x_train, y_train, epochs=3)  # train the model

val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy

predictions = model.predict(x_test)
print("---------------------------")

#print(np.argmax(predictions[50]))

count = 1
for prediction in predictions:
	if np.argmax(prediction) == 1:
		print(20000+count, '--', np.argmax(prediction), '--', y_test[count-1])
	count += 1