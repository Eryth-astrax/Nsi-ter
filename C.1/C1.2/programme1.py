from PIL import Image

largeur = 20
hauteur = 20
c_blanc = (255,255,255)
objet_image = Image.new('RGB', (largeur, hauteur), c_blanc)

c_rouge = (255, 0, 0)
objet_image.putpixel((9,9), c_rouge)
objet_image.putpixel((10,9), c_rouge)
objet_image.putpixel((9,10), c_rouge)
objet_image.putpixel((10,10), c_rouge)

objet_image.show()

objet_image.save('rouge1.png','png')