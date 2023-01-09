import config
import time as t
from Classes.algorithme import Algorithme
from Classes.ordonnancement import Ordonnancement

def lancer_algo(nom_jeu):
    print('--- '+nom_jeu[0]+ ' ---')
    prob = Algorithme()
    prob.definir_par_fichier(nom_jeu[1])
    o = Ordonnancement(prob.nombre_machines)
    debut = t.time()
    resultat=prob.tabou()
    fin=t.time()
    print('temps : ',fin-debut,"s\n")
    print('resultat : ')   
    if config.AFFICHER_SOLUTIONS:
        print('ordre final :',resultat[0],'\n')
    t.sleep(0.5)
    print('duree minimale : ',resultat[1],'\n')
    t.sleep(1)
    return resultat[1]





t.sleep(0.3)
print("""
 ██░ ██ ▓█████  ██▓     ██▓     ▒█████      █     █░ ▒█████   ██▀███   ██▓    ▓█████▄     ▐██▌ 
▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▒██▒  ██▒   ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▓██▒    ▒██▀ ██▌    ▐██▌ 
▒██▀▀██░▒███   ▒██░    ▒██░    ▒██░  ██▒   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▒██░    ░██   █▌    ▐██▌ 
░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ▒██   ██░   ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ▒██░    ░▓█▄   ▌    ▓██▒ 
░▓█▒░██▓░▒████▒░██████▒░██████▒░ ████▓▒░   ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░██████▒░▒████▓     ▒▄▄  
 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░ ▒░▒░▒░    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒▒▓  ▒     ░▀▀▒ 
 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░  ░ ▒ ▒░      ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░ ▒  ░ ░ ▒  ▒     ░  ░ 
 ░  ░░ ░   ░     ░ ░     ░ ░   ░ ░ ░ ▒       ░   ░  ░ ░ ░ ▒    ░░   ░   ░ ░    ░ ░  ░        ░ 
 ░  ░  ░   ░  ░    ░  ░    ░  ░    ░ ░         ░        ░ ░     ░         ░  ░   ░        ░    
                                                                               ░               
""")
t.sleep(2)

if config.MULTIPLE_JEUX:
    liste_noms = []
    liste_resultats=[]
    for nom_jeu in config.MULTIPLE_FICHIERS_DONNEES:
        resultat = lancer_algo((nom_jeu))
        liste_noms.append(nom_jeu)
        liste_resultats.append(resultat)
    print('\n \n \n')
    print('____________________')
    print('\n \n')
    print('--- RESULTATS ---')
    print('\n')
    for compteur in range(len(liste_noms)):
        print('Pour '+liste_noms[compteur][0]+':')
        print(liste_resultats[compteur])
        print('---')

else :
    resultat = lancer_algo((config.FICHIER_DONNEES,config.FICHIER_DONNEES))
    print('\n \n \n')
    print('____________________')
    print('\n \n')
    print('--- RESULTAT ---')
    print('\n \n')
    print('Pour '+config.FICHIER_DONNEES+': \n')
    print(resultat)
    print('\n \n')
    print('---')
    




