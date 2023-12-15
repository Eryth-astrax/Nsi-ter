from PIL import Image

objet_image = Image.open("C1_modularite/C1.2/ballon.png")
c_noir = (0,0,0)


for i in range (objet_image.width):
    objet_image.putpixel((i,0), c_noir)
    objet_image.putpixel((i,objet_image.height-1), c_noir)
    
for i in range (objet_image.height):
    objet_image.putpixel((0,i), c_noir)
    objet_image.putpixel((objet_image.width-1,i), c_noir)
    
objet_image.save(objet_image.filename + '_contour.png','png')