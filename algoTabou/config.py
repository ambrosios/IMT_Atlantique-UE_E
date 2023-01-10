import random
import numpy as np
import os


DATA_DIR = os.getcwd() + "/data/"

MULTIPLE_JEUX = True

MULTIPLE_FICHIERS_DONNEES = [('JEU 1',DATA_DIR + "jeu1.txt"), ('JEU 2',DATA_DIR + "jeu2.txt"), ('TAIL 01',DATA_DIR + "tai01.txt"), ('TAIL 11',DATA_DIR + "tai11.txt"), ('TAIL 21',DATA_DIR + "tai21.txt"), ('TAIL 31', DATA_DIR + "/tai31.txt"), ('TAIL 41',DATA_DIR + "tai41.txt"), ('TAIL 51',DATA_DIR + "tai51.txt")]     # Jeux de données avec nombre de jobs, nombre de machines, durées de chaque opération
FICHIER_DONNEES = DATA_DIR + "jeu1.txt"

NOMBRE_ITERATIONS = 70 # Nombre d'itérations par exécution de l'algorithme tabou


AFFICHER_SOLUTIONS = False

AFFICHER_BARRE_DE_CHARGEMENT = False