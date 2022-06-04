from functools import reduce

import PIL
from cv2 import cv2
from PIL import Image
def color(image):
    gray = []
    couleur = []
    for i in image:

        if len(i.shape) < 3:
            gray.append(i)
        else:
            couleur.append(i)

    return couleur, gray


