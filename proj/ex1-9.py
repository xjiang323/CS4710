from numpy import *
import numpy as np

M = np.random.randint(0,20,size=(10,10))
N = np.random.randint(0,20,size=(10,10))

C = M - N
print(C)
