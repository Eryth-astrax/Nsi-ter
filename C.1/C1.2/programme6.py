from PIL import Image
from random import randint

def couleur_aleat():
    coul_temp = (randint(0,255), randint(0,255), randint(0,255))
    return coul_temp


largeur = 200
hauteur = 200
objet_image = Image.new('RGB', (largeur, hauteur),(255,255,255))

for i in range(largeur):
    for n in range(hauteur):
        objet_image.putpixel((i,n), couleur_aleat())
        
objet_image.show()