# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("color.png")

views = [(-90, 180), (0, 0), (180, -90)]

for xrot, yrot in views:
    for y in range(0, 300, 50):
        X = []
        Y = []
        Z = []
        for c in img[y]:
            X.append(c[2]) #R
            Y.append(c[1]) #G
            Z.append(c[0]) #B


            fig = plt.figure()

        axis = plt.axes(projection='3d')
        axis.set_xlabel('R')
        axis.set_ylabel("G")
        axis.set_zlabel("B")

        axis.view_init(xrot, yrot)
        axis.scatter3D(X, Y, Z)
        plt.show()