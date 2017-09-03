import keras
import numpy as np

data_in = np.array([[0,0],[0,1],[1,0],[1,1]])

logic_and = np.array([[0],[0],[0],[1]])

model = keras.models.Sequential(layers=[
    keras.layers.Dense(input_dim=2, units=1),
    keras.layers.Activation(keras.activations.sigmoid)
])

model.compile(optimizer=keras.optimizers.SGD(lr=.5), loss='mse')

model.fit(data_in, logic_and, epochs = 5000, verbose=False)

print("---------------------------------")

print(model.predict(np.array([[0,0]])))
print(model.predict(np.array([[0,1]])))
print(model.predict(np.array([[1,0]])))
print(model.predict(np.array([[1,1]])))
