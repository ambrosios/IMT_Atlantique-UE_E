#!/usr/bin/env python

""" Classe Ordonnancement """

__author__ = 'Chams Lahlou'
__coauthor__ = 'Amaury Colin'
__date__ = 'Octobre 2019 - décembre 2022'
__version__ = '0.2'

import numpy as np

class Ordonnancement():

    # constructeur pour un ordonnancement vide
    def __init__(self, nombre_machines):
        # liste des jobs dans l'ordre où ils doivent être ordonnancés
        self.sequence = [] 

        # nombre de machines utilisées
        self.nombre_machines = nombre_machines

        # durée de l'ordonnancement, c'est-à-dire date de fin de la dernière
        # opération exécutée
        self.duree = 0  # Cmax

        # pour chaque machine, date à partir de laquelle on peut exécuter une
        # nouvelle opération.
        # Les machines sont numérotées à partir de 0
        self.date_disponibilite = [0 for i in range(self.nombre_machines)]


    def afficher(self):
        print("Ordre des jobs :", end='')
        for job in self.sequence:
            print(" ",job.numero," ", end='')
        print()
        for job in self.sequence:
            print("Job", job.numero, ":", end='')
            for machine in range(self.nombre_machines):
                print(" op", machine, 
                      "à t =", job.date_debut[machine],
                      "|", end='')
            print()
        print("Cmax =", self.duree)


    #####################
    # exo 2 :  A REMPLIR
    #####################
    def ordonnancer_job(self, job, liste_already_provided = False):
        if not(liste_already_provided):
            self.sequence = self.sequence + [job]
        
        for i in range(self.nombre_machines):
            if i < 1:
                job.date_debut[0] = self.date_disponibilite[0]
            else:
                job.date_debut[i] = max(self.date_disponibilite[i - 1], self.date_disponibilite[i])
                
            self.date_disponibilite[i] = job.date_debut[i] + job.duree_operation[i]
            
            if self.duree < self.date_disponibilite[i]:
                self.duree = self.date_disponibilite[i]


    #####################
    # exo 3 :  A REMPLIR
    #####################
    def ordonnancer_liste_job(self, liste_jobs):
        self.sequence = liste_jobs[:]
        self.duree = 0  # Cmax
        self.date_disponibilite = [0 for i in range(self.nombre_machines)]
        
        for job in self.sequence:
            self.ordonnancer_job(job, True)
    
    def ordonnancer_liste_job_with_return_ordo(self, liste_jobs):
        self.ordonnancer_liste_job(liste_jobs)
        return self
    
    def get_duree(self):
        for i in range(self.nombre_machines):
            if self.duree < self.date_disponibilite[i]:
                self.duree = self.date_disponibilite[i]
        return self.duree