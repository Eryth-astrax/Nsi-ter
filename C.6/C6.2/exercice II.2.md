[<-](../cours.md)

# C6.2

## I

Artiste(__idArtist__ : int, nom : varchar, prenom : varchar, annéNaiss : int)

Film(__idFilm__ : int, titre : varchar, année : int, #idRéalisateur : int, genre : varchar, resumé : text, #codePays : varchar)

* l'attribut idRéalisateur fait reference a la clé __idArtist__ de la table Artiste
* l'attribut codePays reference a la clé __code__ de la table Pays

Internaute(__email__ : varchar, nom : varchar, prenom : varchar, #codePays : varchar)

* l'attribut codePays reference a la clé __code__ de la table Pays


Notation(__idFilm__ : int, email : varchar, note : int)


Pays(__code__ : varchar, nom : varchar, langue : varchar)


role(#__idFilm__ : int, #__idActeur__ : int, nomRôle : varchar)

* l'attribut __idActeur__ reference a la clé __idArtiste__ de la table Artiste
* l'attribut __idActeur__ reference a la clé __idFilm__ de la table Film

___

## II.2

a) retourner tous les titre de films

```sql
SELECT titre 
FROM Film
```

b) Retourner le nombre de films.

```sql
SELECT COUNT(titre) 
FROM Film
```

c) Retourner le nombre de films français.


```sql
SELECT COUNT(titre) 
FROM Film 
WHERE codePays = "FR"
```

d) Retourner les titres des films sortis en 2000.

```sql
SELECT COUNT(titre) 
FROM Film 
WHERE année = 2000
```

e) Retourner les titres des films sortis avant 1950.

```sql
SELECT COUNT(titre) 
FROM Film 
WHERE année < 1950
```
f) Retourner les titres des films sortis entre 1980 et 1990.

```sql
SELECT COUNT(titre) 
FROM Film 
WHERE année > 1950 AND année < 1990
```

g) Retourner les titres et les années de sortie des films sortis avant 1950.

```sql
SELECT titre, année 
FROM Film 
WHERE année < 1950
```

h) Retourner les titres et les années de sortie des films sortis entre 1950 et 1960 par année croissante.
    
```sql
SELECT titre, année 
FROM Film 
WHERE année > 1950 and année < 1960
ORDER BY année ASC 
```

i) Retourner les titres des films de science-fiction

```sql
SELECT titre
FROM Film
WHERE genre = "Science-Fiction"
```

j) Retourner le nombre de films de science-fiction

```sql
SELECT COUNT(titre)
FROM Film
WHERE genre = "Science-Fiction"
```

k) Retourner les titres des films de science-fiction sortis avant 1980

```sql
SELECT COUNT(titre)
FROM Film
WHERE genre = "Science-Fiction" AND année < 1980
```

l) Retourner les années lors desquelles des films sont sortis (chaque année ne doit apparaitre qu'une seule fois)

```sql
SELECT DISTINCT année
FROM Film
```

---

## III Interrogation avec jointure de plusieurs tables

### III.2 Travail à faire

a) Retourner la liste des films (titre et nom du réalisateur) classés par ordre alphabétique.

```sql
SELECT titre, idRéalisateur
FROM Film
ORDER BY titre ASC
```

b) Retourner la liste des films (titre et nom du pays en toutes lettres) sortis en 2000.

```sql
SELECT titre, codePays
FROM Film
WHERE année = 2000
```

c) La liste des acteurs (prénom, nom et rôle) du film "Il faut sauver le soldat Ryan" dont l'idFilm est 857.

```sql
SELECT prénom, nom, nomRôle
FROM Rôle JOIN Artiste ON Rôle.idActeur = Artiste.idArtiste
WHERE idFilm = 857
```

d) La liste des films (titre et année) dans lesquels l'acteur Tom Cruise a tournée sachant que l'idArtiste de Tom Cruise est 500.

```sql
SELECT titre, année
FROM Rôle JOIN Film ON Rôle.idFilm = Film.idFilm
WHERE idActeur = 500
```


### III.3 Pour aller plus loin : requêtes imbriquées

Expliquer, en détaillant chaque clause, la requête suivante :

```sql
SELECT DISTINCT prénom, nom
FROM Artiste JOIN Rôle ON Artiste.idArtiste = Rôle.idActeur
WHERE idFilm IN (SELECT idFilm FROM Film WHERE codePays= 'FR')
ORDER BY nom
```

la requête va renvoyer le nom et le prénom des acteurs dans tous les film francais.