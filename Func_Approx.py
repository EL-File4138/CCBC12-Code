# -*- coding: utf-8 -*-

"""
Func_Approx.py
Author: Rorical
Notator: EL_File4138

A Solution for CCBC12 Timeline E 1899.
根据后处理图像拟合函数。
"""

import scipy.optimize as optimize
import numpy as np
from matplotlib import pyplot as plt
import cv2
from math import pi

img = cv2.imread("polar.png")

img = cv2.GaussianBlur(img, (5,5), 0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(img)
plt.show()

_, res = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

plt.imshow(res)
plt.show()

locs = []
xs = []

for x in range(len(res[0])):
    for y in range(len(res)):
        if res[y][x] == 255:
            xs.append(x/1770 * pi)
            locs.append((1354-y)/1354*85 - 25)
            break

plt.figure('Line fig')
ax = plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('y')


ax.scatter(xs, locs, color='r', s=1)
plt.show()

def target_func(x, A, B, C, D, E):
    return A*np.sin(x)+B*np.sin(2*x)+C*np.sin(3*x)+D*np.sin(4*x)+E*np.sin(5*x)

para, _ = optimize.curve_fit(target_func, xs, locs)

print(para)