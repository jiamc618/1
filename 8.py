import numpy as np
import math as ma

x0 = np.ones(10)
x1 = np.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
x2 = np.array([2, 3, 4, 2, 3, 4, 2, 4, 1, 3])
y = np.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

X = np.stack((x0, x1, x2), axis=1)
print('X:\n{}'.format(X))

maty = np.mat(y)
Y = np.array(maty.T)
print('Y:\n{}'.format(Y))

W = (np.mat(X).T * np.mat(X)).I * np.mat(X).T * np.mat(Y)
print('W:\n{}\nshape of W:\n{}'.format(W, W.shape))