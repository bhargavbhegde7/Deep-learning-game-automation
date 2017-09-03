# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 20:33:52 2017

@author: Bhargav
"""

import numpy as np
from matplotlib import pyplot as plt

data = [[0,   0, 1],
        [0,   1, 1],
        [1,   0, 1],
        [1,   1, 0]]

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

#random init of weights
w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

iterations = 500000
learning_rate = 0.1
costs = [] # keep costs during training, see if they go down

for i in range(iterations):
    ri = np.random.randint(len(data))
    point = data[ri]
    
    z = point[0]*w1 + point[1]*w2 + b
    
    pred = sigmoid(z)
    
    target = point[2]
    cost = np.square(pred - target)
    
    costs.append(cost)
    
    dcost_pred = 2 * (pred - target)
    dpred_dz = sigmoid_p(z)
    
    dz_dw1 = point[0]
    dz_dw2 = point[1]    
    dz_db = 1
    
    dcost_dz = dcost_dw1 = dcost_pred * dpred_dz
    
    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db
    
    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b  = b  - learning_rate * dcost_db

z00 = w1 * 0 + w2 * 0 + b
z01 = w1 * 0 + w2 * 1 + b
z10 = w1 * 1 + w2 * 0 + b
z11 = w1 * 1 + w2 * 1 + b

pred00 = sigmoid(z00)
pred01 = sigmoid(z01)
pred10 = sigmoid(z10)
pred11 = sigmoid(z11)

print(pred00)
print(pred01)
print(pred10)
print(pred11)