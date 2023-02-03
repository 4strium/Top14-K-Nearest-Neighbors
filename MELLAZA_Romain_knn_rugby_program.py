import pandas                       # Manipulation du fichier csv
import math                         # Calcul des distances
import matplotlib.pyplot as courbe  # Représentation graphique

def extractionDonnees(nomFichier='JoueursTop14.csv'):
    """Cette fonction récupère les données d'un fichier csv et renvoie deux valeurs :
    La liste des descripteurs et la liste de toutes les données"""
    players = pandas.read_csv(nomFichier, sep=';', encoding='utf-8')
    
    descripteurs = list(players.columns) # Je récupére les descripteurs.

    return (players, descripteurs) # On retourne un Tuple contenant les deux ensembles de données.

def extraireEquipe(players, choix_equipe):
    """De l'ensemble des listes, on extrait seulement celles d'une équipe
    Parmi les équipes, on trouve "Agen", "Bayonne", "Bordeaux", "Brive", "Castres", "Clermont",
    "La Rochelle", "Lyon", "Montpellier", "Paris", "Pau", "Racing92", "Toulon" et "Toulouse"
    On peut aussi écrire "Tous" pour avoir tous les joueurs du top 14"""
    
    precise_play = players.loc[(players["Equipe"] == choix_equipe)]
    
    return precise_play

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

def distance(x1,y1,x2,y2):
    """Distance euclidienne entre les points de coordonnées (x1;y1) et (x2;y2)"""
    result_dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return result_dis

def balayage_points(data_graph, taille_user, poids_user):
    """Calcul des distances entre le point de l'utilisateur et les points des différents postes"""
    taille_x = data_graph[0]
    poids_y = data_graph[1]
    poste_val = data_graph[2]

    list_ecart = list()

    # On calcule la distance pour chaque élément :
    for element in range(len(taille_x)) :
        verdict = distance(taille_user,poids_user,taille_x[element],poids_y[element])
        
        # Puis on ajoute la distance ainsi que le poste actuellement étudié :
        list_ecart.append([verdict, poste_val[element]])
    
    return list_ecart

def classification(data_ecart):
    sum_avant = 0
    nb_avant = 0
    sum_2emeligne = 0
    nb_2emeligne = 0
    sum_3emeligne = 0
    nb_3emeligne = 0
    sum_demi = 0
    nb_demi = 0
    sum_trois_quarts = 0
    nb_trois_quarts = 0
    sum_arriere = 0
    nb_arriere = 0

    for k in range(len(data_ecart)) :
        if data_ecart[k][1] == 'Avant' :
            sum_avant += data_ecart[k][0]
            nb_avant += 1
        elif data_ecart[k][1] == '2ème ligne' :
            sum_2emeligne += data_ecart[k][0]
            nb_2emeligne += 1 
        elif data_ecart[k][1] == '3ème ligne' :
            sum_3emeligne += data_ecart[k][0]
            nb_3emeligne += 1
        elif data_ecart[k][1] == 'Demi' :
            sum_demi += data_ecart[k][0]
            nb_demi += 1
        elif data_ecart[k][1] == 'Trois-Quarts' :
            sum_trois_quarts += data_ecart[k][0]
            nb_trois_quarts += 1
        elif data_ecart[k][1] == 'Arrière' :
            sum_arriere += data_ecart[k][0]
            nb_arriere += 1

    list_of_all_avg = list()

    avg_avant = sum_avant / nb_avant
    list_of_all_avg.append(['Avant', avg_avant])
    avg_2emeligne = sum_2emeligne / nb_2emeligne
    list_of_all_avg.append(['2ème ligne', avg_2emeligne])
    avg_3emeligne = sum_3emeligne / nb_3emeligne
    list_of_all_avg.append(['3ème ligne', avg_3emeligne])
    avg_demi = sum_demi / nb_demi
    list_of_all_avg.append(['Demi', avg_demi])
    avg_trois_quarts = sum_trois_quarts / nb_trois_quarts
    list_of_all_avg.append(['Trois-Quarts', avg_trois_quarts])
    avg_arriere = sum_arriere / nb_arriere
    list_of_all_avg.append(['Arrière', avg_arriere])

    return list_of_all_avg

def add_point_user(taille_user, poids_user):
    courbe.scatter(taille_user, poids_user, marker="X", c="black")
    courbe.text(taille_user+0.2, poids_user+0.2, 'Vous')

    courbe.savefig('representation_graphique.png')

    courbe.show()

def best_post(predi):
    predi.sort(key = lambda x: x[1])

    return predi

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

data_for_search = representation(data_team, extractionDonnees()[1])

taille_saisie = int(input("Saisissez votre taille en cm :\n"))
poids_saisie = int(input("Saisissez votre poids en kg :\n"))

list_distances = balayage_points(data_for_search, taille_saisie, poids_saisie)

predictions = classification(list_distances)

predictions = best_post(predictions)

print("\nPredictions :",predictions,"\n")

print("Le meilleur poste pour vous dans l'équipe de",team,"est :",predictions[0][0],"\n")

add_point_user(taille_saisie, poids_saisie)