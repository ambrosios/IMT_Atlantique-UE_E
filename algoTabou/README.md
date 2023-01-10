# Algorithme Tabou

**Auteur :** Yann LEGENDRE

**Date :** 3 Janvier 2023

**Version :** v0.1

**Language de programmation :** Python

**Cadre de l'exercice :** cours de résolution approchée, UE E de _Conception, Optimisation, et Pilotage des Systèmes Industriels (COPSI)_ à [IMT Atlantique](https://imt-atlantique.fr/).


## Execution de l'algorithme

Pour exécuter l'algorithme, il faut s'assurer d'avoir time d'installé dans son environnement Python. De plus, afin d'afficher la barre de chargement, il est possible d'installer la bibliothèque progress.

Pour lancer l'exécution, après le paramétrage effectué dans le fichier *config.py*, il faut exécuter le fichier

	execute.py

## Paramétrage de l'algorithme

L'algorithme offre plusieurs possibilités de paramétrage qui sont regroupées dans le fichier *config.py*.

* MULTIPLE_JEUX : Permet d'exécuter plusieurs jeux de données à la suite
* MULTIPLE_FICHIERS_DONNEES : Liste de jeux de données avec nombre de jobs, nombre de machines, durées de chaque opération
* FICHIER_DONNEES : Fichier de données utilisé lorsque MULTIPLE_JEUX est faux
* NOMBRE_ITERATIONS : Nombre d'itérations par exécution de l'algorithme tabou
* AFFICHER_SOLUTIONS : Affichage des solutions
* AFFICHER_BARRE_DE_CHARGEMENT : Affichage d'une barre de progression