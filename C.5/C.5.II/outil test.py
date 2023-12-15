import matplotlib.pyplot as plt
import random

def hauteur(t):
    if t == None:
        return 0
    else:
        _, t1, t2 = t
        return max([hauteur(t1), hauteur(t2)]) + 1

def draw_tree_aux(t, rect, dy, labels):
    if t == None:
        return None
    x1, x2, y1, y2 = rect
    xm = (x1 + x2) // 2
    x, t1, t2 = t
    draw_tree_aux(t1, (x1, xm, y1, y2 - dy), dy, labels)
    draw_tree_aux(t2, (xm, x2, y1, y2 - dy), dy, labels)
    if t1 != None:
        a, b = ((xm, (x1 + xm) // 2), (y2, y2 - dy))
        plt.plot(a, b, 'k', marker='o', markersize=20, markerfacecolor='white')
    if t2 != None:
        c, d = ((xm, (x2 + xm) // 2), (y2, y2 - dy))
        plt.plot(c, d, 'k', marker='o', markersize=20, markerfacecolor='white')
    if labels:
        plt.text(xm, y2, str(x), fontsize=10,
                 horizontalalignment='center', verticalalignment='center')

def draw_tree(t, labels=True):
    d = 512
    pad = 20
    dy = (d - 2 * pad) / (hauteur(t))
    draw_tree_aux(t, (pad, d - pad, pad, d - pad), dy, labels)
    plt.axis([0, d, 0, d])
    plt.axis('off')
    plt.show()

def name_random():
    return str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))

def arbre_binaire_aleat(t=0):
    x = 1
    if t > 1:
        x = random.randint(1,3)
    if t == 5:
        return None
    elif x == 3:
        return None
    else:
        return (name_random(), arbre_binaire_aleat(t+1), arbre_binaire_aleat(t+1))
    
def arbre_NB_aleat(taille,h,t=0):
    x = random.randint(1,taille)
    if t != h:
        arb_name = name_random()
        arb_temp = [ ]
        arb_temp.append(arb_name)
        for i in range(x):
            a = random.randint(1,2)
            if a == 1:
                arb_temp.append(arbre_NB_aleat(taille,h, t+1))
            else:
                arb_temp.append(None)
        return arb_temp
    
    else:
        arb_name = name_random()
        arb_temp = [ ]
        arb_temp.append(arb_name)
        for i in range(x):
            arb_temp.append(None)
        return arb_temp
    
def draw_arbre(abr,t=0):
    print('    '*t+'|_'+str(abr[0]))
    for i in range(1,len(abr)):
        if abr[i] == None:
            print('    '*(t+1)+'|_'+str(abr[i]))
        else:
            draw_arbre(abr[i],t+1)
    
"""
# ==== Exemple d'utilisation ====
if __name__ == '__main__':
    arbre = arbre_aleat()
    print(arbre)
    draw_tree(arbre)
"""
#draw_arbre(arbre_aleat())

draw_arbre(arbre_NB_aleat(5,6))