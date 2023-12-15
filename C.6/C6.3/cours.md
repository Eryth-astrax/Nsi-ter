[<-](../cours.md)

# C6.3

## I

Ouvrir DB Browser.

Cliquer sur le bouton "Nouvelle Base de Données".

Dans la fenêtre Windows d'enregistrement qui s'ouvre, choisir un emplacement et un nom de base, par exemple "MaBase".

Une fenêtre s'ouvre. Cliquer sur le bouton "Annuler".

Ouvrir l'onglet "Exécuter le SQL".

Taper la requête suivante et valider :

```sql
CREATE TABLE utilisateur
(
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    ville VARCHAR(255)
)
```
## II

### II.2

a) Ajouter la personne Zheblouse Agathe qui habite à Orléans.

```sql
INSERT INTO utilisateur VALUES (0,"Agathe", "Zheblouse", "Orléans")
```



b) Ajouter, en une seule requête, les personnes suivantes : Kase Camille qui habite à Paris et Paillalé Eva qui habite Bordeaux.

```sql
INSERT INTO utilisateur
VALUES
    (1,"Cammille", "kase", "Paris"),
    (2,"Eva", "Paillalé", "Bordeau")
```

c) Modifier la ville de Paillalé Eva qui a déménagé à Brest.

```sql
UPDATE utilisateur
SET ville = "Brest"
WHERE id = 2
```

86.160.180.4