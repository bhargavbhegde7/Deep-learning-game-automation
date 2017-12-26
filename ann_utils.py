import math
import random

def sigmoid(x):
    return 1.0/(1 + math.exp(-x))

def deriv_sigmoid(x):
    sgmd = sigmoid(x)
    return (1 - sgmd) * sgmd

def make_matrix(N, M):
    """
    Make an N rows by M columns make_matrix
    """
    return [[0 for i in range(M)] for i in range(N)]

def between(min, max):
    """
    return a real random value between min and max.
    """

    return random.random() * (max-min) + min
