# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:46:14 2019

@author: dit
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('C:\\Users\\dit\\Pictures\\cat.jpeg')
image1 = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

plt.imshow(image)