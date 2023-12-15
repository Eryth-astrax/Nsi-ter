import portuguais
import random
from PIL import Image,  ImageShow
#import dessin

def ville():
    nbre_immeuble=4
    return nbre_immeuble
def imeuble():
    Maison=portuguais.taille()
    Maison=portuguais.toit(Maison)
    Maison=portuguais.etage(Maison)
    Maison=portuguais.RDC(Maison)
    return Maison


#carte de la ville
Ville=ville()
liste_immeuble = []
for i in range(Ville):
    liste_immeuble.append(imeuble())

c_blanc=(255,255,255)

objet_image = Image.new('RGB', (800, 600), c_blanc)
decal = 48


#dessin
def color_aleat():
    coul_temp = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return coul_temp

def rectangle(coordA,coordB,color):
    xA,yA=coordA
    xB,yB=coordB
    for i in range (xA,xB):
        for n in range(yA,yB):
            y=(600-1)-n
            objet_image.putpixel((i,y-1), color)
            
def triangle(coordA,coordB,color):
    xA,yA=coordA
    xB,yB=coordB
    x=0
    for n in range(yA,yB):
        for i in range (xA+x*2,xB-x*2):
            y=(600-1)-n
            objet_image.putpixel((i,y-1), color)
        x+=1
            
def contour(coordA,coordB,nbre_etage):
    xA,yA=coordA
    xB,yB=coordB
    c_noir=(0,0,0)
    for i in range (yA,yB-58):
        y=(600-1)-i
        objet_image.putpixel((xA,y), c_noir)
        objet_image.putpixel((xB,y), c_noir)     
    for i in range (xA,xB):
        for n in range(nbre_etage):
            y=(600-1)- (n*60) - 100
            objet_image.putpixel((i,y), c_noir)


def contour_fen(coordA,coordB):
    xA,yA=coordA
    xB,yB=coordB
    c_noir=(0,0,0)
    for i in range (yA,yB):
        y=(600-1)-i
        objet_image.putpixel((xA,y-1), c_noir)
        objet_image.putpixel((xB,y), c_noir)
    yA=(600-1)-yA
    yB=(600-1)-yB
    for i in range (xA,xB+1):
        objet_image.putpixel((i,yA), c_noir)
        objet_image.putpixel((i,yB), c_noir)
            

def background():
    start_color = (0,0,0)  
    middle_color=(255,255,255) 


    increment_r = (middle_color[0] - start_color[0]) / 1500
    increment_g = (middle_color[1] - start_color[1]) / 1500
    increment_b = (middle_color[2] - start_color[2]) / 1500

    for y in range(500):
        r = int(start_color[0] + increment_r * y)
        g = int(start_color[1] + increment_g * y)
        b = int(start_color[2] + increment_b * y)
        for x in range(800):
            objet_image.putpixel((x, y), (r, g, b))
            
    for y in range(600):
        for x in range(3,797):
            if random.randint(1,650-y) == 10:
                taille = random.randint(1,3)
                rectangle((x,y),(x+taille,y+taille),(255,255,150))
                
    for y in range(499,600):
        for x in range(800):
            objet_image.putpixel((x, y), (128,128,118))
    
    rectangle((0,100),(799,102),(0,0,0))
    
    for y in range(40,60):
        for x in range(0,800,100):         
            rectangle((x+y-40,y),(x+50+y-40,y+1),(255,255,255))
            
            
def volet(coordA,coordB):
    couleur=color_aleat()
    rectangle(coordA,(coordB[0]-21,coordB[1]),couleur)
    rectangle((coordA[0]+22,coordA[1]),coordB,couleur)
    
def draw_humain_balcon(coord1):
    humain = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,1,1,0,0,0,0,1,2,2,1,0,0,0],
    [0,1,1,0,0,0,0,1,2,2,1,0,0,0],
    [0,1,1,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,0,0,0,0,0,1,1,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,2,2,2,2,2,2,1,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [0,0,1,2,2,2,2,2,2,2,2,2,2,1],
    [0,0,0,1,2,2,2,2,2,2,2,2,2,1],
    [0,0,0,0,1,2,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,1,1,1,1,1,2,1],
    [0,0,0,0,0,1,2,1,0,0,0,1,2,1],
    [0,0,0,0,1,2,1,0,0,0,0,1,2,1],
    [0,0,0,1,2,1,0,0,0,0,0,1,2,1],
    [0,0,0,1,2,1,0,0,0,0,0,1,2,1],
    [0,0,1,2,1,0,0,0,0,0,0,1,2,1],
    [0,0,1,2,1,0,0,0,0,0,0,1,2,1],
    [0,0,1,2,1,0,0,0,0,0,0,1,2,1],
    [0,0,1,2,1,0,0,0,0,0,0,1,2,1],
    [0,0,1,1,1,0,0,0,0,0,0,1,1,1]]
    if random.randint(1,3)==3:
        for y in range(len(humain)):
            for x in range(len(humain[y])):
                coord2=(coord1[0]+x,coord1[1]-y)
                x1=coord2[0]+10
                y1=(600-1)-coord2[1]-len(humain)
                if humain[y][x] == 1:
                    objet_image.putpixel((x1,y1), (0,0,0)) 
                if humain[y][x] == 2:
                    objet_image.putpixel((x1,y1), (245,245,220))
    else:
        for y in range(len(humain)):
            for x in range(len(humain[y])):
                coord2=(coord1[0]+x,coord1[1]-y)
                x1=coord2[0]+10
                y1=(600-1)-coord2[1]-len(humain)
                if humain[y][x] == 1:
                    objet_image.putpixel((x1,y1), (0,0,0)) 
                if humain[y][x] == 2:
                    objet_image.putpixel((x1,y1), ((245,245,220)))

def balcon(coordA,coordB):
    coord1=(coordA[0]-6,coordA[1]+30)
    coord2=(coordB[0]+6,coordA[1]+32)
    rectangle(coord1,coord2,(0,0,0))
    coord1=(coordA[0]-6,coordA[1])
    coord2=(coordB[0]+6,coordA[1]+2)
    rectangle(coord1,coord2,(0,0,0))
    for i in range(coord1[0],coord2[0]+2,4):
        coord1=(i,coordA[1])
        coord2=(i+2,coordA[1]+32)
        rectangle(coord1,coord2,(0,0,0))
            
def draw_humain(coord1):
    humain = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,1,1,0,0,0,0,1,2,2,1,0,0,0],
    [0,1,1,0,0,0,0,1,2,2,1,0,0,0],
    [0,1,1,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,0,0,0,0,0,1,1,0,0,0,0],
    [1,1,1,1,0,0,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,2,2,2,2,2,2,1,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,1],
    [0,0,1,2,2,2,2,2,2,2,2,2,2,1],
    [0,0,0,1,2,2,2,2,2,2,2,2,2,1],
    [0,0,0,0,1,2,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,1],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,1],]
    if random.randint(1,3)==3:
        for y in range(len(humain)):
            for x in range(len(humain[y])):
                coord2=(coord1[0]+x,coord1[1]-y)
                x1=coord2[0]+15
                y1=(600-1)-coord2[1]- len(humain)
                if humain[y][x] == 1:
                    objet_image.putpixel((x1,y1), (0,0,0)) 
                if humain[y][x] == 2:
                    objet_image.putpixel((x1,y1), (245,245,220))
    else:
        for y in range(len(humain)):
            for x in range(len(humain[y])):
                coord2=(coord1[0]+x,coord1[1]-y)
                x1=coord2[0]+10
                y1=(600-1)-coord2[1]-len(humain)
                if humain[y][x] == 1:
                    objet_image.putpixel((x1,y1), (0,0,0)) 
                if humain[y][x] == 2:
                    objet_image.putpixel((x1,y1), ((245,245,220)))
    

def fenetre(coordA,liste):
    for i in range(1,len(liste)):
        for n in range(3):
            balcon_chance = random.randint(1,3)
            if balcon_chance==1:
                if liste[i][n]==1 or liste[i][n]==2:
                    coord1=(coordA[0]+13+44*n,60*(len(liste)-1)-60*(i)+100)
                    coord2=(coordA[0]+43+44*n,60*(len(liste)-1)-15*i-45*(i-1)+100)
                    rectangle(coord1,coord2,(255,255,255))
                    if random.randint(1,10)==3:
                        draw_humain_balcon(coord1)
                    if liste[i][n]==2:
                        volet(coord1,coord2)
                    contour_fen(coord1,coord2)
                    balcon(coord1,coord2)
            else:
                if liste[i][n]==1 or liste[i][n]==2:
                    coord1=(coordA[0]+13+44*n,60*(len(liste)-1)-(45*i)-(15*(i-1))+100)
                    coord2=(coordA[0]+43+44*n,60*(len(liste)-1)-15*i-45*(i-1)+100)
                    rectangle(coord1,coord2,(255,255,255))
                    if random.randint(1,20)==3:
                        draw_humain(coord1)
                    if liste[i][n]==2:
                        volet(coord1,coord2)
                    contour_fen(coord1,coord2)
                    

def porte(coordA,liste):
    for i in range(len(liste)):
        if liste[i]==0:
            coord1=(coordA[0]+12*(i+1)+30*i,coordA[1])
            coord2=(coordA[0]+43*(i+1),coordA[1]+45)
            rectangle(coord1,coord2,(0,0,0))
    
def etage(coordA,coordB,color):
    rectangle((coordA[0],160),(coordB[0],coordB[1]-60),color)
    
def toit(coordB):
    toits=random.randint(1,2)
    if toits==1:
        coord1=(coordB[0]-145,coordB[1]-60)
        coord2=(coordB[0]+6,coordB[1]+3-60)
        rectangle(coord1,coord2,(0,0,0))
    else:
        coord1=(coordB[0]-145,coordB[1]-60)
        coord2=(coordB[0]+5,coordB[1]+20)
        triangle(coord1,coord2,(0,0,0))
    
def rdc(coordA,coordB,color):
    rectangle(coordA,(coordB[0],160),color)

def immeuble(immeuble_liste,coord,nbre_etage,n): 
    color=color_aleat()
    rdc(coord[0],coord[1],color)
    etage(coord[0],coord[1],color)
    contour(coord[0],coord[1],nbre_etage)
    toit(coord[1])
    porte(coord[0],immeuble_liste[nbre_etage-1])
    fenetre(coord[0],immeuble_liste)
    
    
#image
background()
for i in range(len(liste_immeuble)):
    hauteur = 60 * len(liste_immeuble[i])-1
    coord = [(decal,100),(decal+140,hauteur+100)]
    immeuble(liste_immeuble[i], coord,len(liste_immeuble[i]),i)
    decal+=140+48

objet_image.show()
objet_image.save("essai.png","PNG")


