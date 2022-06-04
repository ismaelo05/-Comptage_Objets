# Permet de définir la taille de chaque image lors de l'affichage
import cv2
import numpy as np
from matplotlib import pyplot as plt, cm
from matplotlib.pyplot import figure, imshow

# Fonction permettant de convertir une image en niveau de gris
def convertImage1(imageList):
    rows = 2
    columns = len(imageList) // rows
    fig = plt.figure(figsize=(15, 20))
    #Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    images = []
    for original in imageList:
        fig.add_subplot(rows, columns, compt)
        gray_im = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        # Convertion en niveau de gris
        gray_correct = np.array(255 * (gray_im / 255) ** 1.2 , dtype='uint8')
        plt.imshow(gray_correct,cmap=cm.gray)
        plt.axis('off')
        plt.title("Image de niveau de gris " + str(compt))
        compt = compt + 1
        images.append(gray_correct)
    plt.show()
    return images

# Fonction permettant de convertir une image en niveau de gris
def convertImage2(imageList):
    rows = 2
    columns = len(imageList) // rows
    fig = plt.figure(figsize=(15, 20))
    #Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    images = []
    for original in imageList:
        fig.add_subplot(rows, columns, compt)
        # convertion en niveau de gris
        gray_correct = np.array(255 * (original / 255) ** 1.2 , dtype='uint8')
        plt.imshow(gray_correct,cmap=cm.gray)
        plt.axis('off')
        plt.title("Image de niveau de gris " + str(compt))
        compt = compt + 1
        images.append(gray_correct)
    plt.show()
    return images