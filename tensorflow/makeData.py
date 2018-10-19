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

training_data_samples = []
def create_training_samples():
	#for imgName in range(1, 194776):
	path = os.path.join(DATADIR)
	
	IMG_SIZE = 100
	for img in tqdm(range(1, 194576)):
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
	for img in tqdm(range(194576, 194776)):
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
			if count >= 194576:
				break
			array_of_words = line.split(',')
			training_data_labels.append(array_of_words[1])
			img_name = array_of_words[0]
				
			count += 1

test_data_labels = []
def create_test_labels():
	count = 1
	img_name = ""
	with open(LABELFILE) as f:
		for line in f:
			if count > 194575 and count < 194776:
				array_of_words = line.split(',')
				test_data_labels.append(array_of_words[1])
				img_name = array_of_words[0]
				
			count += 1

create_training_samples()
create_training_labels()

create_test_samples()
create_test_labels()

x_train = training_data_samples
y_train = training_data_labels

x_test = test_data_samples
y_test = test_data_labels

