import random

def make_matrix(N, M):
    """
    Make an N rows by M columns make_matrix

    """
    return [[0 for i in range(M)] for i in range(N)]

def between(min, max):
    """
    return a rel random value between min and max.
    """

    return random.random() * (max-min) + min
