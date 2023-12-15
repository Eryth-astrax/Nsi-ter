[<-](../cours.md)

# C7.2

[![source](../../images.jpg)](https://nsi2023.ostralo.net/2_terminale/chap07_optimisation/C7.2_assertions.php)

## I. travail préliminaire

* application
    
    on considere le code suivant: 
    ```py
    def f(t):
    a = 0
    for i in range(len(t)):
        if t[i] > t[a]:
            a = i
    return a
    ```

    * Que vaut f([0, 9, 4]) ?
    
        cela vaut 1

    * Améliorer la lisibilité du code de cette fonction en choisissant des noms parlants, en ajoutant des annotations de type et une docstring complète pour la fonction.

        ```py
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
        ```


        [test](app.I.py)

    * Que renvoie la fonction :

        - avec le paramètre t1 = [-9, -4, -1] ?
            
                >>> 2

        - avec le paramètre t2 = [5, 0] ?

                >>> 0

        - avec le paramètre t3 = [] ?

                >>> 0

    * quelle sont les precondition

        ``liste`` doit etre une liste d'entier non-vide

    

## app_III.1

* application 1
    Reprendre le code de la fonction du I) en y ajoutant une assertion pour assurer que la liste passée en paramètre n'est pas vide.

    ```py
    def max(liste:list)->int:
        """
        renvoie la position du nombre le plus grand
        parameters:
            liste ; list
        returns:
            int
        """
        assert liste != [] "la liste ne doit pas etre vide"
        x = 0
        for i in range(len(liste)):
            if liste[i] > liste[x]:
                x = i
        return x
    ```

## app_III.2

* Proposer quelques lignes de code avec une assertion permettant d'assurer qu'une liste contient uniquement des entiers.

    ```py
    for val in liste:
        assert isinstance(val, int) "la liste ne doit contenir que des entiers"   
    ```

* Compléter le code précédant pour assurer qu'une liste contient uniquement des entiers positifs ou nuls.

    ```py
    for val in liste:
        assert isinstance(val, int) "la liste ne doit contenir que des entiers"   
        assert val >= 0 "laliste ne doit contenir que des entier positif ou nul"
    ```

## app_III.3

* On considère la fonction dont le début du code est donné ci-dessous :

    ```py
    from random import randint
    def liste_uniques(N, d, f):
        """
        Renvoie une liste de N nombres entiers aléatoires entre d et f (compris) sans aucun doublon.
        """
    ```

    * Lister toutes les préconditions sur les paramètres de cette fonction.

        ``N`` doit etre un entier non nul.

        ``d`` et ``f`` doivent etre des entiers.

        ``d`` doit etre inferieur a ``f``.

    * Compléter le code de la fonction.

        ```py
        from random import randint
        def liste_uniques(N, d, f):
            """
            Renvoie une liste de N nombres entiers aléatoires entre d et f (compris) sans aucun doublon.
            """
            liste = []
            for i in range(N):
                liste.append(randint(d,f))
            return liste
        ```

    * Ajouter des assertions au code de la fonction afin que le programme soit interrompu si les préconditions ne sont pas respectées.

        ```py
        from random import randint
        def liste_uniques(N, d, f):
            """
            Renvoie une liste de N nombres entiers aléatoires entre d et f (compris) sans aucun doublon.
            """
            assert isinstance(N, int) and N > 0 "N doi etre un entier non nul"
            assert isinstance(d, int) " d foit etre un entier"
            assert isinstance(f, int) "f doit etre un entier"
            assert d < f "d doit etre inferieur a f"
            liste = []
            for i in range(N):
                liste.append(randint(d,f))
            return liste
        ```

