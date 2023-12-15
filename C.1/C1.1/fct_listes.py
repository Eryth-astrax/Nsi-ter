"""
Module qui propose en ensemble de fonction pour travailler avec les listes d'entiers
"""

def max_liste(l:list) -> int:
    """
    Renvoie la plus grande valeur d'une liste non vide d'entiers

    >>> max_liste([10, 20, 5])
    20
    """
    assert l !=[], "La liste ne doit pas être vide"
    m = l[0]
    for elt in l:
        if elt > m:
            m = elt
    return m

def min_liste(l:list) -> int:
    """
    Renvoie la plus petite valeur d'une liste non vide d'entiers

    >>> min_liste([10, 20, 5])
    5
    """
    assert l !=[], "La liste ne doit pas être vide"
    m = l[0]
    for elt in l:
        if elt < m:
            m = elt
    return m


if __name__ == '__main__':
    print("Bonjour !")

