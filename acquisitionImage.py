import os
from os import listdir
from os.path import isfile, join
import numpy
import cv2
from pathlib import Path

def chemin(mypath):
    images = []
    for imagepath in mypath:
        img = cv2.imread(str(imagepath))
        root, extension = os.path.splitext(imagepath)
        # print(extension)
        if extension == '.png':
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (200, 200))
        images.append(img)
    return images


