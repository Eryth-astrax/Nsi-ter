[<-](../cours.md)

# C7.1


[![source](../../images.jpg)](https://nsi2023.ostralo.net/2_terminale/chap07_optimisation/C7.1_lisibilite.php)


## III doctring

### III.1 application

* app.1 Améliorer le code suivant :

    ```py
    def f(t):
        a = 0
        for i in range(len(t)):
            a = a + t[i]
        return a
    ```

    code ameliorer:

    ```py
    def somme(liste):
        total = 0
        for val in liste:
            total += liste[i]
        return total
    ```

* app.2 Écrire le code de la fonction dont la docstring est la suivante :

    ```py
    '''
    Calcule et renvoie la moyenne (avec deux chiffres après la virgule) des valeurs d'un tableau de nombres
    Parameters:
        t : (list) Liste de nombres
    Returns:
        (float) Moyenne arrondie à 2 chiffres après la virgule
    '''
    ```

    code:

    ```py
    def moyenne(t):
        total = 0
        for val in t:
            total += val
        return round(total/len(t), 2)
    ```


* app.3 Quels sont les premiers mots de la docstring du module random ?

    > [application](app.3.py)


* app.4 Améliorer la lisibilité du code ci-dessous (entre autre, en utilisant des fonctions).


    ```py
    Li = [[1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1]]
    for i in range(len(Li)):
        x = ""
        for j in Li[i]:
            if j:
                x = x + "• "
            else:
                x = x + "  "
        print(x)
    ```

    [correction](app.4.py)