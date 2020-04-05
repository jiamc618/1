import numpy as np
import math as ma

x = np.array([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = np.array([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

xn = x.size
yn = y.size

xa = float(np.sum(x) / xn)
ya = float(np.sum(y) / yn)
fenzi = 0
fenmu = 0
for i in range(xn):
    fenzi += (x[i] - xa) * (y[i] - ya)
    fenmu += ma.pow((x[i] - xa), 2)
w = fenzi / fenmu
print("w:{}".format(w))
b = ya-w * xa
print("b:{}".format(b))