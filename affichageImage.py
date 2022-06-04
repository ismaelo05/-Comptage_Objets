import cv2
from matplotlib import pyplot as plt


def afficher1(image):
    rows = 2
    columns = len(image) // rows

    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    # Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    for name in image:
        fig.add_subplot(rows, columns, compt)
        plt.imshow(cv2.cvtColor(name, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.title("Image " + str(compt))
        compt = compt + 1

    plt.show()
    return image

def afficher2(image):
    rows = 2
    columns = len(image) // rows

    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    # Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    for name in image:
        fig.add_subplot(rows, columns, compt)
        plt.imshow(name, cmap='gray')
        plt.axis('off')
        plt.title("Image " + str(compt))
        compt = compt + 1

    plt.show()
    return image