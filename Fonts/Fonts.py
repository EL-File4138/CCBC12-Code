"""
Fonts.py
Author: Rorical
Notator: EL_File4138

A Solution for CCBC12 Timeline E 2066.
过滤那个该死的字。
! 效果不佳，请谨慎尝试。
"""

import cv2
import numpy as np

img = cv2.imread("words.png", 0)

template = cv2.imread('word.png', 0)

w, h = template.shape[::-1]
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.885
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), -1)
cv2.imshow('res', res)
cv2.imshow('res', img)
cv2.waitKey()
cv2.imwrite("a.png", img)