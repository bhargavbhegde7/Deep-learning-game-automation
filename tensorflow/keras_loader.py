import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import _pickle as cPickle
from keras.models import model_from_json
from keras.models import model_from_yaml

sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
(x_train, y_train_old),(x_test, y_test_old) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train_old/y_test_old

x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1

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
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
	
val_loss, val_acc = loaded_model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy

predictions = loaded_model.predict(x_test)
print("---------------------------")

print(np.argmax(predictions[0]))
print(np.argmax(predictions[1]))
