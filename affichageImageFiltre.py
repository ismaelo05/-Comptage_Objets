import cv2
from matplotlib import pyplot as plt


def afficherImageFiltre1(imageList):
    # Nombre de ligne et colonne pour faciliter l'affichage des différentes images sur 3x2
    rows = 2
    columns = len(imageList) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    #Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    images = []
    for thresh in imageList:
        fig.add_subplot(rows, columns, compt)
        canny = cv2.Canny(thresh, 30, 150, 3) # Utilisation de la fonction proposée par openCV pour filtre de Canny
        images.append(canny)
        plt.imshow(canny, cmap='gray')
        plt.axis('off')
        plt.title("Image "+str(compt)+" avec foltre de Canny")
        compt = compt +1
    plt.show()
    return images

def afficherImageFiltre2(imageList):
    # Nombre de ligne et colonne pour faciliter l'affichage des différentes images sur 3x2
    rows = 2
    columns = len(imageList) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    #Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    images = []
    for thresh in imageList:
        fig.add_subplot(rows, columns, compt)
        if compt == 1:
            canny = cv2.Canny(thresh, 30, 200, 3) # Utilisation de la fonction proposée par openCV pour filtre de Canny
        else:
            canny = cv2.Canny(thresh, 30, 200, 3)
        images.append(canny)
        plt.imshow(canny, cmap='gray')
        plt.axis('off')
        plt.title("Image "+str(compt)+" avec foltre de Canny")
        compt = compt +1
    plt.show()
    return images


def dilateImage1(imageList):
    # Nombre de ligne et colonne pour faciliter l'affichage des différentes images sur 3x2
    rows = 2
    columns = len(imageList) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    #Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    images = []
    for canny in imageList:
        fig.add_subplot(rows, columns, compt)
        if compt == 1:
            dilated = cv2.dilate(canny, (1, 1), iterations=2)
        elif compt == 4:
            dilated = cv2.dilate(canny, (1, 1), iterations=21)
        else:
            dilated = cv2.dilate(canny, (1, 1), iterations=8)
        images.append(dilated)
        plt.imshow(dilated, cmap='gray')
        plt.axis('off')
        plt.title("Image "+str(compt)+" dilatée")
        compt = compt +1
    plt.show()
    return images

def dilateImage2(imageList):
    # Nombre de ligne et colonne pour faciliter l'affichage des différentes images sur 3x2
    rows = 2
    columns = len(imageList) // rows
    # Permet de définir la taille de chaque image lors de l'affichage
    fig = plt.figure(figsize=(15, 20))
    #Permet de parcourir chaque élément de la matricice d'affichage
    compt = 1
    # Parcours et récupération de chaque image de la liste des images
    # pour leur afficher suivant la disposition choisie
    images = []
    for canny in imageList:
        fig.add_subplot(rows, columns, compt)
        if compt == 1:
            dilated = cv2.dilate(canny, (1, 1), iterations=1)
        elif compt == 4:
            dilated = cv2.dilate(canny, (1, 1), iterations=-3)
        else:
            dilated = cv2.dilate(canny, (1, 1), iterations=1)
        images.append(dilated)
        plt.imshow(dilated, cmap='gray')
        plt.axis('off')
        plt.title("Image "+str(compt)+" dilatée")
        compt = compt +1
    plt.show()
    return images