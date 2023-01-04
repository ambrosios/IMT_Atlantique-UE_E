# Algorithme du recuit simulé

**Auteurs :** Amaury COLIN, Thibault Le Roy

**Date :** 4 janvier 2023

**Version :** v0.2

**Langage de programmation :** Python

**Cadre de l'exercice :** cours de résolution approchée, UE E de *Conception, Optimisation, et Pilotage des Systèmes Industriels (COPSI)* à [IMT Atlantique](https://imt-atlantique.fr).

## Exécution de l'algorithme

Pour exécuter l'algorithme, il faut s'assurer d'avoir scipy d'installé dans son environnement Python.

Pour lancer l'exécution, après le paramétrage effectué, il faut exécuter le fichier

		algorithme_recuit.py


## Paramétrage de l'algorithme

L'algorithme offre plusieurs possibilités de paramétrage qui sont regroupées dans le fichier *config.py*.

* DONNEES_INITIALES : le jeu de données utilisé
* NOMBRE_ITERATIONS : le nombre d'itérations
* ALPHA : paramètre de variation de la température
* AFFICHAGE\_NOM_ALGORITHME : le nom de l'algorithme
* AFFICHAGE\_DONNEES_PROBLEME : affichage des données initiales
* AFFICHAGE\_HEURISTIQUE : affichage de l'heuristique de départ
* AFFICHAGE\_T : affichage des premières températures (nombre entier)
* AFFICHAGE\_NOUVEAU_VOISIN : affichage de tous les voisins dans le voisinage considéré
* AFFICHAGE\_VOISIN_CHOISI : affichage du voisin sélectionné dans le voisinage considéré
* AFFICHAGE\_RESULTAT : affichage de la solution
* AFFICHAGE\_STAT : affichage des statistiques de l'exécution
	



