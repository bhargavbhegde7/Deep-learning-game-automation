import numpy as np
from matplotlib import pyplot as plt

data = [[3,   1.5, 1],
        [2,   1,   0],
        [4,   1.5, 1],
        [3,   1,   0],
        [3.5, .5,  1],
        [2,   .5,  0],
        [5.5,  1,  1],
        [1,    1,  0]]

mystery_flower = [4.5, 1]

def vis_data():
    plt.grid()

    for i in range(len(data)):
        c = 'r'
        if data[i][2] == 0:
            c = 'b'
        plt.scatter([data[i][0]], [data[i][1]], c=c)

    plt.scatter([mystery_flower[0]], [mystery_flower[1]], c='gray')
    plt.ion()
    plt.show()

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

plt.plot(costs)
z = w1 * mystery_flower[0] + w2 * mystery_flower[1] + b
pred = sigmoid(z)

print(pred)
print("close to 0 -> blue, close to 1 -> red")