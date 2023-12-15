from PIL import Image

def rectangle(coord,taille):
    for i in range(coord[0] ,coord[0] + taille[0]+1):
        for n in range(coord[1] ,coord[1] + taille[1]+1):
            if n == coord[1] or n == (coord[1] + taille[1]):
                objet_image.putpixel((i-(taille[0]//2), n-(taille[1]//2)),(0,0,0))
            if i == coord[0] or i == ((coord[0]+taille[0])):
                objet_image.putpixel((i-(taille[0]//2), n-(taille[1]//2)),(0,0,0))


c_blanc=(255,255,255)
objet_image = Image.new('RGB', (800, 800), c_blanc)

def fonc_recur(coord,taille):
    if taille[1] <= 0 or taille[0] <= 0:
        print("stop")
    else:
        rectangle(coord,taille)
        fonc_recur(coord,(taille[0]-20,taille[1]-20))
        

fonc_recur((400,400),(300,300))
objet_image.show()