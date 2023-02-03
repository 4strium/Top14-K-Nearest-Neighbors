# Introduction
Nous allons nous intéresser à la méthode dite des « des k plus proches voisins »
(en anglais « k nearest neighbors » ; d’où le sigle KNN).

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
    1. <u>Deux données numériques destinées à la comparaison</u> de deux éléments de l’ensemble : **Taille (x) et Poids (y)**
    2. Un <u>critère destiné à la classification</u> d’un élément : **Poste du joueur**