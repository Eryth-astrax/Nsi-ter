from PIL import Image

objet_image = Image.open("ballon.png")


def negative(coul):
    coul_temp=(255-coul[0],255-coul[1],255-coul[2])
    return coul_temp

couleur = objet_image.getpixel((100,100))
print("Le pixel qui est à la position (100, 100) à la couleur " + str(couleur))

for i in range (objet_image.width):
    for n in range(objet_image.height):
        objet_image.putpixel((i,n), negative(objet_image.getpixel((i,n))))
        
objet_image.show()
