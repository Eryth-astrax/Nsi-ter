def max(liste:list)->int:
    """
    renvoie la position du nombre le plus grand
    parameters:
        liste ; list
    returns:
        int
    """
    x = 0
    for i in range(len(liste)):
        if liste[i] > liste[x]:
            x = i
    return x