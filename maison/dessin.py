from PIL import Image
import random

def color_aleat():
    coul_temp = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return coul_temp

def rectangle(objet_image,coord,coord_max,color):
    x=coord[0]
    y=coord[1]
    x_max=coord_max[0]
    y_max=coord_max[1]
    for i in range (x,x_max+1):
        for n in range(y, y_max+1):
            objet_image.putpixel((i,n), color)

def background():
    None

    
def fenetre():
    None

def porte():
    None
    
def etage():
    None
    
def toit():
    None
    
def rdc(objet_image,coord,coord_max,color):
    rectangle(objet_image,coord,coord_max,color)

def immeuble(objet_image,immeuble_liste,coord): 
    color=color_aleat()
    print(color)
    rdc(objet_image,(coord[0][0],140),coord[1],color)
    
    
