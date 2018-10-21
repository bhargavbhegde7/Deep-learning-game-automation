import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import _pickle as cPickle
from keras.models import model_from_json

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
(x_train, y_train_old),(x_test, y_test_old) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train_old/y_test_old

x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1
x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1

# only keep the pictures of one number in the x_train
indicesToKeep = []
for idx, val in tqdm(enumerate(y_train_old)):
    if y_train_old[idx] == 7:
        indicesToKeep.append(idx)

y_train = np.zeros((60000,), dtype=int)

for index in tqdm(indicesToKeep):
    y_train[index] = 1
	
model = tf.keras.models.Sequential()  # a basic feed-forward model
model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track

model.fit(x_train, y_train, epochs=3)  # train the model

y_test = np.zeros((10000,), dtype=int)

i = 0
for eachValue in tqdm(y_test_old):
    if eachValue == 7:
        y_test[i] = 1
    i = i+1

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
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
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
	
val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy

predictions = model.predict(x_test)
print("---------------------------")

print(np.argmax(predictions[0]))
print(np.argmax(predictions[1]))
