import glob

import cv2
from matplotlib import pyplot as plt

import acquisitionImage


def compterObjet(ima):
    rows = 2
    columns = len(ima) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    # Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    mypath = glob.glob("/home/ismael/Bureau/M1 IFI SIM/Traitement d'image/TP4/TP4_Groupe2/*.jpg")
    image = acquisitionImage.chemin(mypath)
    liste = []
    for dilated in ima:
        fig.add_subplot(rows, columns, compt)
        # Détermine les contours de chaque objet de l'image
        (cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # En cercle chaque contour avec une image de couleur
        rgb = cv2.cvtColor(image[compt-1], cv2.COLOR_BGR2RGB)
        cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
        plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        # Affiche le nombre d'objet de l'image
        plt.title("Image " + str(compt)+" contient "+str(len(cnt))+" objets")
        compt = compt + 1
    plt.show()
    return liste