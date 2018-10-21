import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import re

#---------------------------------------------------------------------------------
#----------------------------- READ AND PREPATE DATA -----------------------------
#---------------------------------------------------------------------------------
DATASET_PATH = "dataset"
DATADIR = DATASET_PATH+"/"+"samples"
LABELFILE = DATASET_PATH+"/"+"labels"+"/"+"labels.txt"

TRAINING_AMOUNT = 40000
TESTING_AMOUNT = 2000

training_data_samples = []
def create_training_samples():
	#for imgName in range(1, 194776):
	path = os.path.join(DATADIR)
	
	IMG_SIZE = 100
	for img in tqdm(range(0, TRAINING_AMOUNT)):
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
	for img in tqdm(range(TRAINING_AMOUNT, TRAINING_AMOUNT+TESTING_AMOUNT)):
		try:
			img_array = cv2.imread(os.path.join(path,str(img)+".jpeg") ,cv2.IMREAD_GRAYSCALE)
			new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
			test_data_samples.append(new_array)
		except Exception as e:
			print(e)
			pass

training_data_labels = []
def create_training_labels():
	count = 0
	img_name = ""
	with open(LABELFILE) as f:
		for line in f:
			if count >= TRAINING_AMOUNT:
				break
			array_of_words = line.split(',')
			training_data_labels.append(int(array_of_words[1]))
			img_name = array_of_words[0]
				
			count += 1
			
test_data_labels = []
def create_test_labels():
	count = 0
	img_name = ""
	with open(LABELFILE) as f:
		for line in f:
			if count >= TRAINING_AMOUNT and count < TRAINING_AMOUNT+TESTING_AMOUNT:
				array_of_words = line.split(',')
				test_data_labels.append(int(array_of_words[1]))
				img_name = array_of_words[0]
				
			count += 1

create_training_samples()
create_training_labels()

create_test_samples()
create_test_labels()

x_train = training_data_samples
y_train = np.zeros((TRAINING_AMOUNT,), dtype=int)
for index, val in enumerate(training_data_labels):
	y_train[index] = val

x_test = test_data_samples
y_test = np.zeros((TESTING_AMOUNT,), dtype=int)
for index, val in enumerate(test_data_labels):
	y_test[index] = val
#---------------------------------------------------------------------------------
#----------------------------- READ AND PREPATE DATA -----------------------------
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
#------------------------------ CREATE MODEL AND TRAIN ---------------------------
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

model.fit(x_train, y_train, epochs=5)  # train the model

val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy

#---------------------------------------------------------------------------------
#------------------------------ CREATE MODEL AND TRAIN ---------------------------
#---------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# ----------------------------- save the model ---------------------------------------
# ------------------------------------------------------------------------------------
'''
# save the model to desk
model_json = model.to_json()
with open("model.json", "w") as json_file:
	json_file.write(model_json)

# serialize the weights
model.save_weights("model.h5")
print(" ----- saved model to disk")
'''

# serialize model to YAML
model_yaml = model.to_yaml()
with open("model.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)
	
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# ------------------------------------------------------------------------------------
# ----------------------------- save the model ---------------------------------------
# ------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
#------------------------------ TEST ---------------------------------------------
#---------------------------------------------------------------------------------
predictions = model.predict(x_test)

print("---------------------------------")
print("----------- TEST ----------------")
print("---------------------------------")

count = 0
for prediction in predictions:
	if np.argmax(prediction) == 1:
		print(TRAINING_AMOUNT+count, '--', np.argmax(prediction), '--', y_test[count])
	count += 1
#---------------------------------------------------------------------------------
#------------------------------ TEST ---------------------------------------------
#---------------------------------------------------------------------------------