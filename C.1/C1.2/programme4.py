from PIL import Image
from random import randint


def aleatoire(n):
    if n==0:
        return 0
    else:
        return 255

def couleur_aleat_base():
    coul_temp = (aleatoire(randint(0,1)), aleatoire(randint(0,1)), aleatoire(randint(0,1)))
    return coul_temp
    
def couleur_aleat():
    coul_temp = (randint(0,255), randint(0,255), randint(0,255))
    return coul_temp

largeur = 100
hauteur = 100
objet_image = Image.new('RGB', (largeur, hauteur),couleur_aleat())
objet_image.show()
