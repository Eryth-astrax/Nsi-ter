import random

def taille():
    maison = [[0]]
    for i in range(random.randint(1,6)):
        maison.append([0,0,0])
    return maison

def toit(maison):
    maison[0]= random.randint(0,1)
    return maison

def etage(maison):
    for i in range(1,len(maison)):
        for n in range (len(maison[i])):
            maison[i][n] = random.randint(1,2)
    return maison

def RDC(maison):
    porte = random.randint(0,2)
    long=len(maison)-1
    for i in range(len(maison[long])):
        if i == porte:
            maison[long][i]=0
        else:
            maison[long][i]=random.randint(1,2)
    return maison


            