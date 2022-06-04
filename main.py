import glob
from os import path

import cv2
import matplotlib.pyplot as plt
import acquisitionImage
import affichageImage
import affichageImageFiltre
import checkColorImage
import comptageObjetImage
import convertImageGray
import segmentationImages
from acquisitionImage import chemin

# Chemin d'accès aux fichiers images d'un repertoire
mypath = glob.glob("/home/ismael/Bureau/M1 IFI SIM/Traitement d'image/TP4/TP4_Groupe2/*.jpg")

# Lecture de fichiers images d'un repertoire
image = acquisitionImage.chemin(mypath)

# Vérifie si les images entrées sont couleurs ou non
imageCouleur, imageGray = checkColorImage.color(image)
print(len(imageGray))
print(len(imageCouleur))
if len(imageGray) != 0: # Cas ou elles sont de niveaux de gris
    # fonction d'affichage des images
    image1 = affichageImage.afficher2(imageGray)
    # fonction de convertion d'une image de couleur en une image de niveau de gris
    image2 = convertImageGray.convertImage2(image1)
    # fonction pour segmenter des images avec une valeur seuil de 110.0
    image3 = segmentationImages.segmentationGray2(image2)
    # Premier filtrage des images qui est celui de Canny
    image4 = affichageImageFiltre.afficherImageFiltre2(image3)
    # Dilaté les images
    image5 = affichageImageFiltre.dilateImage2(image4)
    # Affiche le nombre d'objets de chaque image
    image6 = comptageObjetImage.compterObjet(image5)
if len(imageCouleur) != 0: # Cas ou elles sont couleurs
    # fonction d'affichage des images
    image1 = affichageImage.afficher1(imageCouleur)
    # print(image1)
    # fonction de convertion d'une image de couleur en une image de niveau de gris
    image2 = convertImageGray.convertImage1(image1)
    # fonction pour segmenter des images
    image3 = segmentationImages.segmentationGray1(image2)
    # Premier filtrage des images qui est celui de Canny
    image4 = affichageImageFiltre.afficherImageFiltre1(image3)
    # Dilaté les images
    image5 = affichageImageFiltre.dilateImage1(image4)
    # Affiche le nombre d'objets de chaque image
    image6 = comptageObjetImage.compterObjet(image5)

# fonction d'affichage des images en RGB
# image1 = affichageTSL.afficherTSL(image2)

