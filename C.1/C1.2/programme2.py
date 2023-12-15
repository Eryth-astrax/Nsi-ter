from PIL import Image

largeur = 600
hauteur = 400
c_bleu = (0,0,255)
c_blanc = (255,255,255)
c_rouge = (255,0,0)
objet_image = Image.new('RGB', (largeur, hauteur), c_blanc)

for i in range(200):
    for n in range(400):
        objet_image.putpixel((i,n), c_bleu)
        
for i in range(400,600):
    for n in range(400):
        objet_image.putpixel((i,n), c_rouge)
        
objet_image.save("drapeau.png","png")