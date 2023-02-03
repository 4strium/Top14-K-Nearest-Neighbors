# Introduction
Nous allons nous intéresser à la méthode dite des « des k plus proches voisins »
(en anglais « k nearest neighbors » ; d’où le sigle KNN).

Le principe est assez simple, on dispose d’un ensemble de données, chaque donnée dispose de **deux paramètres numériques que l’on utilisera en tant qu’abscisse et ordonnée.**
<span style="color: green;">(Exemples : taille, poids, couleur, …).</span>
Cela nous permettra de comparer les différentes données via ces paramètres, et notamment les distances qui séparent les différents points dans une représentation graphique.

Mais il ne faut pas perdre de vue le but initial de l’algorithme qui est de **classifier les données de l’ensemble de manière optimisée !**
C’est pour cela qu’intervient un troisième critère destiné à la classification d’un élément.
<span style="color: green;">(Exemples : espèces de fleurs, poste des joueurs dans une équipe, …).</span>

# Représentation
<html>
    <p align="center">
        <img src="https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/cdp/cf/ul/g/ef/3a/KNN.component.l.ts=1639762044031.png/content/adobe-cms/us/en/topics/knn/jcr:content/root/table_of_contents/intro/complex_narrative/items/content_group/image" alt="KNN diagram"/>
    </p>
</html>