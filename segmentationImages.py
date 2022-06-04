import cv2
from matplotlib import pyplot as plt


def segmentationGray1(ima):
    rows = 2
    columns = len(ima) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    # Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    seuil1 = 110.0
    seuil2 = 40.0
    liste = []
    for gray_correct in ima:
        fig.add_subplot(rows, columns, compt)
        # Application du seuillage adaptatif de openCV pour segmenter notre image tout en utilisant
        # le filtre Gaoussien et Moyenneur
        thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 19)
        liste.append(thresh)
        plt.imshow(thresh, cmap='gray')
        plt.axis('off')
        plt.title("Image segmenté " + str(compt))
        compt = compt + 1
    plt.show()
    return liste


def segmentationGray2(ima):
    rows = 2
    columns = len(ima) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    # Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    seuil1 = 110.0
    seuil2 = 40.0
    liste = []
    for gray_correct in ima:
        fig.add_subplot(rows, columns, compt)
        if compt == 4:
            # Application du seuillage adaptatif de openCV pour segmenter notre image tout en utilisant
            # le filtre Gaoussien et Moyenneur
            thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255,
                                           50)
        elif compt == 1:
            thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255,
                                           10)
        else:
            thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 0)
        liste.append(thresh)
        plt.imshow(thresh, cmap='gray')
        plt.axis('off')
        plt.title("Image segmenté " + str(compt))
        compt = compt + 1
    plt.show()
    return liste