import random
import numpy as np


FICHIER_DONNEES = "algoGenetique/data/jeu2.txt" # Jeu de données avec nombre de jobs, nombre de machines, durées de chaque opération


N = 100 # Taille de la population
AFFICHER_AJUSTEMENT_TAILLE_POPULATION = True # Indique si la taille de la population a été ajustée à N+1 (dans le cas où N impair)

NOMBRE_ITERATIONS = 100 # Nombre d'itérations par exécution de l'algorithme génétique

NOMBRE_EXECUTIONS = 2

PROBABILITE_MUTATION_FONCTION = random.uniform # Fonction aléatoire pour déterminer si un individu aura une mutation (ex : np.random.normal)
PROBABILITE_MUTATION_SEUIL_DEPART = 0.2 # Probabilité pour un enfant de subir une mutation
PROBABILITE_MUTATION_DYNAMIQUE = True # Augmente la probabilité d'avoir des mutations lorsqu'il y a un optimum local trouvé
MUTATION_DYNAMIQUE_SEUIL = 0.4 # Si un individu a un taux de présencé dans la population supérieur à ce seuil, alors la mutation dynamique a lieu

SEUIL_SELECTION_MEILLEURS = 1/N # Taux de meilleurs individus conservés

AFFICHER_NOM_ALGORITHME = True # Affiche le nom de l'algorithme au lancement du script
AFFICHER_POPULATION = False # Affiche la population à chaque itération
AFFICHER_NOMBRE_DOUBLONS = False # Affiche la population à chaque itération
AFFICHER_NOUVEAUX_INDIVIDUS = False # Affiche les individus créés
AFFICHER_POPULATION_APRES_NAISSANCE = False # Affiche la population à chaque itération
AFFICHER_CORRECTIONS = False # Affiche la correction avec avant/après
AFFICHER_MUTATIONS = False # Affiche les mutations réalisées
AFFICHER_EVALUATIONS = False # Affiche la valeur de l'évaluation de tous les individus de la population
AFFICHER_SELECTIONNES = False # Affiche les individus sélectionné et leur évaluation
AFFICHER_MEILLEUR_A_CHAQUE_ITERATION = False # Affiche la progression du meilleur individu de la population
AFFICHER_GRAPHIQUE = True
AFFICHER_TEMPS_EXECUTION = True # Affiche le temps nécessaire pour finir l'évaluation