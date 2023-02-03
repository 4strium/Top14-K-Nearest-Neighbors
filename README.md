# Introduction
Nous allons nous intéresser à la méthode dite des « [des k plus proches voisins](https://www.ibm.com/topics/knn) » *(en anglais « k nearest neighbors » ; d’où le sigle KNN)*.

Le principe est assez simple, on dispose d’un ensemble de données, chaque donnée dispose de **deux paramètres numériques que l’on utilisera en tant qu’abscisse et ordonnée.**
*(Exemples : taille, poids, couleur, …).*

Cela nous permettra de comparer les différentes données via ces paramètres, et notamment les distances qui séparent les différents points dans une représentation graphique.

Mais il ne faut pas perdre de vue le but initial de l’algorithme qui est de **classifier les données de l’ensemble de manière optimisée !**
C’est pour cela qu’intervient un troisième critère destiné à la classification d’un élément.
*(Exemples : espèces de fleurs, poste des joueurs dans une équipe, …).*

# Représentation
<html>
    <p align="center">
        <img src="https://github.com/4strium/Top14-K-Nearest-Neighbors/blob/main/representation_knn.png" alt="KNN diagram"/>
    </p>
</html>

# Cas pratique
Nous allons maintenant nous atteler à la conception d’un programme qui indexera la taille et le poids des différents joueurs du Top14 ainsi que leur poste sur le terrain au cours de la saison 2019/2020.

Nous nous retrouvons donc bien avec nos **deux types d’informations** :
1. **Deux données numériques destinées à la comparaison** de deux éléments de l’ensemble : *Taille (x) et Poids (y)*
2. **Un critère destiné à la classification** d’un élément : *Poste du joueur*

L’objectif est tout d’abord de **représenter cet ensemble dans un graphique**, puis, par la suite, l’utilisateur sera invité à **saisir une taille et un poids arbitraire** dans le but de **créer un nouvel élément** que l’algorithme KNN devra parvenir à **classifier dans le poste le plusapproprié à la morphologie saisie !**

# Programmation
Afin de rendre plus compréhensible le programme, nous allons décomposer l’algorithme en plusieurs blocs/fonctions :

## Importation des librairies et dépendances :
Chaque module est utilisé dans un but bien précis.

```python 
import pandas                       # Manipulation du fichier csv
import math                         # Calcul des distances
import matplotlib.pyplot as courbe  # Représentation graphique
```

## Extraire toutes les données du fichier CSV :
Dans cette fonction on récupère, tout d’abord, absolument toutes les données de la base dans un *"DataFrame"*, puis dans un second temps, une liste de tous les descripteurs du fichier.

```python 
def extractionDonnees(nomFichier='JoueursTop14.csv'):
    """Cette fonction récupère les données d'un fichier csv et renvoie deux valeurs :
    La liste des descripteurs et la liste de toutes les données"""
    players = pandas.read_csv(nomFichier, sep=';', encoding='utf-8')
    
    descripteurs = list(players.columns) # Je récupére les descripteurs.

    return (players, descripteurs) # On retourne un Tuple contenant les deux ensembles de données.
```

## Extraire seulement les données sur une équipe choisie :
Dans cette fonction, on localise dans la colonne « Equipe » les lignes qui comportent la valeur exacte de l’équipe choisie par l’utilisateur.
*(Exemples : Toulouse, Racing92, …)*
Si l’utilisateur choisi plutôt d’étudier **tous** les joueurs du Top14, alors la fonction n’est pas exécutée car on manipulera par la suite l’ensemble des données !

```python
def extraireEquipe(players, choix_equipe):
    """De l'ensemble des listes, on extrait seulement celles d'une équipe
    Parmi les équipes, on trouve "Agen", "Bayonne", "Bordeaux", "Brive", "Castres", "Clermont",
    "La Rochelle", "Lyon", "Montpellier", "Paris", "Pau", "Racing92", "Toulon" et "Toulouse"
    On peut aussi écrire "Tous" pour avoir tous les joueurs du top 14"""
    
    precise_play = players.loc[(players["Equipe"] == choix_equipe)]
    
    return precise_play

equipes_disponibles = ["Agen", "Bayonne", "Bordeaux", "Brive", "Castres", "Clermont", "La Rochelle", "Lyon", "Montpellier", "Paris", "Pau", "Racing92", "Toulon", "Toulouse"]

team = str(input('Choisissez votre équipe : \n'))   # On interroge l'utilisateur sur l'équipe qu'il souhaite étudier !

if team == 'Tous' :             # Possibilté d'étudier tous les joueurs du Top 14

    data_team = extractionDonnees()[0].values.tolist()    # On convertis le DataFrame entier en liste.
    team = 'Top14 entier'

elif team in equipes_disponibles :  # Vérification que l'équipe choisie est bien dans la liste disponible.

    data_team = extraireEquipe(extractionDonnees()[0], team)  # On extrait seulement les joueurs de l'équipe choisie.
    data_team = data_team.values.tolist()                     # On convertis le DataFrame de l'équipe en liste.

else : 
    print("Désolé, cette équipe n'est pas disponible...")
    exit()                                                    # On stoppe l'éxécution du code.
```

## Représenter graphiquement le nuage de points :
Dans cette partie nous allons utiliser la librairie Python « [MatplotLib](https://matplotlib.org/) » qui va nous permettre de réalise un nuage de points avec la taille des joueurs en abscisse et leurs poids en ordonnée !

```python
def representation(data,descripteurs):
    global team
    """data est une liste de joueurs avec leurs caractéristiques.
    On extrait leur taille et poids puis on représente ces données dans un repère
    (une couleur par type de poste la position étant déterminée par la liste des descripteurs)
    Les types de postes sont "Avant", "2ème ligne", "3ème ligne", "Demi", "Trois-Quarts" et "Arrière" """
    
    taille = []
    poids=[]
    poste=[]

    for i in range(len(data)) :
        val_temp = data[i]
        taille_temp = val_temp[descripteurs.index('Taille (en cm)')]
        poids_temp = val_temp[descripteurs.index('Poids (en kg)')]
        poste_temp = val_temp[descripteurs.index('Type poste')]
        taille.append(taille_temp)
        poids.append(poids_temp)
        poste.append(poste_temp)
        
    # Création de la courbe :
    title = "Analyse de l'équipe de rugby de " + team
    courbe.title(title, fontsize=18)
    courbe.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    courbe.xlabel('Taille (en cm)')
    courbe.ylabel('Poids (en kg)')
    for i in range(len(data)) :
        if poste[i] == 'Avant' :
            point1 = courbe.scatter(taille[i], poids[i], marker="x", c="blue")
        if poste[i] == '2ème ligne' :
            point2 = courbe.scatter(taille[i], poids[i], marker="+", c="red")
        if poste[i] == '3ème ligne' :
            point3 = courbe.scatter(taille[i], poids[i], marker="1", c="green")
        if poste[i] == 'Demi' :
            point4 = courbe.scatter(taille[i], poids[i], marker="o", c="purple")
        if poste[i] == 'Trois-Quarts' :
            point5 = courbe.scatter(taille[i], poids[i], marker="*", c="brown")
        if poste[i] == 'Arrière' :
            point6 = courbe.scatter(taille[i], poids[i], marker="^", c="orange")
    courbe.legend([point1, point2, point3, point4, point5, point6],['Avant','2ème ligne','3ème ligne','Demi','Trois-Quarts','Arrière'], shadow=True, title=team, title_fontsize=15, loc='lower right')
    
    return (taille, poids, poste)

# Appel de la fonction :
data_for_search = representation(data_team, extractionDonnees()[1])
```

## Balayage et calcul des distances entre le point de l’utilisateur et ceux des joueurs :
Via les deux fonctions suivantes nous allons calculer les différentes distances euclidiennes, entre le point saisi par l’utilisateur et tous les points des joueurs.

On rappelle la formule pour calculer une distance euclidienne :

$ d=√((x_2-x_1 )^2+(y_2-y_1 )^2 ) $