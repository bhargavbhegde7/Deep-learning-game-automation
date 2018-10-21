import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import re
from keras.models import model_from_yaml
from keras.models import model_from_json

#---------------------------------------------------------------------------------
#----------------------------- READ AND PREPATE TEST DATA ------------------------
#---------------------------------------------------------------------------------
DATASET_PATH = "dataset"
DATADIR = DATASET_PATH+"/"+"samples"
LABELFILE = DATASET_PATH+"/"+"labels"+"/"+"labels.txt"

TRAINING_AMOUNT = 8000
TESTING_AMOUNT = 2000

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

create_test_samples()
create_test_labels()

x_test = test_data_samples
y_test = np.zeros((TESTING_AMOUNT,), dtype=int)
for index, val in enumerate(test_data_labels):
	y_test[index] = val
	
x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1
#---------------------------------------------------------------------------------
#----------------------------- READ AND PREPATE TEST DATA ------------------------
#---------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# ---------------------------- LOAD THE MODEL ----------------------------------------
# ------------------------------------------------------------------------------------

'''
# load saved model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json, custom_objects={'GlorotUniform': tf.keras.initializers.glorot_uniform(seed=None)})
'''

# load YAML and create model
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml, custom_objects={'GlorotUniform': tf.keras.initializers.glorot_uniform(seed=None)})

loaded_model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track

# load weights into the new model
loaded_model.load_weights("model.h5")
print(" ----- loaded model from disk")

# ------------------------------------------------------------------------------------
# ---------------------------- LOAD THE MODEL ----------------------------------------
# ------------------------------------------------------------------------------------
	
val_loss, val_acc = loaded_model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy

#---------------------------------------------------------------------------------
#------------------------------ TEST ---------------------------------------------
#---------------------------------------------------------------------------------
predictions = loaded_model.predict(x_test)

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
