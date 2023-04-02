from PIL import Image

def convertir_gris(img_RGB):
    """img(RGB) > img(L)
    prend une image en couleurs et la met en niveau de gris
    """
    largeur, hauteur = img_RGB.size
    img_gris = Image.new("L", img_RGB.size)
    for x in range(largeur):
        for y in range(hauteur):
            pixel = img_RGB.getpixel((x, y))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            l = 0.299*r+0.587*g+0.114*b
            img_gris.putpixel((x, y), int(l))
    return img_gris

def convertir_16x16(img):
    """img(L) > img(L)
    prend une image et en fait une autre 16 fois plus petite en faisant une moyenne de carrees de 16x16 pixel
    """
    largeur, hauteur = img.size
    img_16x16 = Image.new("L", (largeur//16, hauteur//16))
    ximg = 0
    yimg = 0
    adition_pixel = 0
    for x in range(largeur//16):
        for y in range(hauteur//16):
            for ximg_16x16 in range(16):
                for yimg_16x16 in range(16):
                    pixel = img.getpixel((ximg_16x16+ximg, yimg_16x16+yimg))
                    adition_pixel = adition_pixel+pixel
            img_16x16.putpixel((ximg//16, yimg//16), adition_pixel//256)
            yimg = yimg+16
            adition_pixel = 0
        yimg = 0
        ximg = ximg+16
    return img_16x16

def convertir_str_ASCII(img, echelle_ASCII, format16x16):
    """img, str, bool > list[str]
    if format16x16 == False:
    transforme l'image en chaine de caractere ASCII grace a une chaine de caractere echelle de luminance
    fait souvant des chaines très grandes ayant du mal à rentrer dans la console
    if format16x16 == True:
    transforme l'image en chaine de caractere ASCII plus petite grace a une chaine de caractere echelle de luminance
    fait des chaines plus petite on perds donc de la precision
    si la dimension de l'image n'est pas un multiple de 16 elle ne tiendra pas compte de la partie qui depasse
    """
    if img.mode != "L":
        img = convertir_gris(img)
    if format16x16 == True:
        img = convertir_16x16(img)
    largeur, hauteur = img.size
    img_ASCII = [["" for caractere in range(largeur)] for ligne in range(hauteur)]
    for x in range(largeur):
        for y in range(hauteur):
            pixel = img.getpixel((x, y))
            img_ASCII[y][x] = echelle_ASCII[pixel//(256//(len(echelle_ASCII)-1))]
    img_ASCII = ["".join(img_ASCII[ligne]) for ligne in range(len(img_ASCII))]
    for i in range(len(img_ASCII)):
        print (img_ASCII[i])
    return img_ASCII

def convertir_img_ASCII(img, echelle_ASCII, format16x16):
    """img, img(L), bool > img(L)
    if format16x16 == False:
    transforme l'image en image de caractere ASCII grace a une image echelle de luminance
    doit afficher des images tres grandes mais du coup il faut vraiment beaucoup de temps pour ne charger une image
    presque 50 minutes pour une image de 2064x1936 pixel nous avons donc mis une image d'exemple dans le fichier
    if format16x16 == True:
    transforme l'image en image de caractere ASCII plus petite grace a une image echelle de luminance
    fait des images plus petite on perds donc de la precision
    si la dimension de l'image n'est pas un multiple de 16 elle ne tiendra pas compte de la partie qui depasse
    """
    if img.mode != "L":
        img = convertir_gris(img)
    if format16x16 == True:
        img = convertir_16x16(img)
    largeur, hauteur = img.size
    largeur_echelle_ASCII, hauteur_echelle_ASCII = echelle_ASCII.size
    img_ASCII = Image.new("L", (largeur*16, hauteur*16))
    for x in range(largeur):
        for y in range(hauteur):
            pixel = img.getpixel((x, y))
            caractere = pixel//(256//(largeur_echelle_ASCII/16-1))
            for ximg_ASCII in range(16):
                for yimg_ASCII in range(16):
                    pixel_echelle_ASCII = echelle_ASCII.getpixel((ximg_ASCII+caractere*16, yimg_ASCII))
                    img_ASCII.putpixel((ximg_ASCII+x*16, yimg_ASCII+y*16), pixel_echelle_ASCII)
    img_ASCII.show()
    return img_ASCII    

def convertir_ASCII(img, echelle_ASCII, solution):
    """img, str/img(L) > list[str]/img(L)
    precondition: img == type(img), if solution == 1 ou 2 echelle_ASCII == type(str), if solution == 3 ou 4 echelle_ASCII == type(img), 1 >= solution >= 4
    permet de choisir entre les 4 solutions
    1:transforme en chaine de caractere ASCII directement dans la console
    2:transforme en petite chaine de caractere ASCII directement dans la console
    3:transforme en image ASCII (attention très long)
    4:transforme en petite image ASCII
    """
    if solution == 1:
        return convertir_str_ASCII(img, echelle_ASCII, False)
    elif solution == 2:
        return convertir_str_ASCII(img, echelle_ASCII, True)
    elif solution == 3:
        return convertir_img_ASCII(img, echelle_ASCII, False)
    else:
        return convertir_img_ASCII(img, echelle_ASCII, True)

"""img sert a mettre l'image a modifier
possibilite de mettre l'echelle souhaite
ranger l'echelle du plus foncé au plus clair
"""
img = Image.open("baboon.png")
echelle_ASCII_str_defaut = "@%#+:-. "
echelle_ASCII_img_defaut = convertir_gris(Image.open("Police d'écriture.png"))
convertir_ASCII(img, echelle_ASCII_str_defaut, 1)