#!/usr/bin/env python

""" Classe Ordonnancement """

__author__ = 'Chams Lahlou'
__date__ = 'Octobre 2019 - janvier 2021'
__version__ = '0.2'

import job

class Ordonnancement():

    # constructeur pour un ordonnancement vide
    def __init__(self, nombre_machines):
        # liste des jobs dans l'ordre où ils doivent être ordonnancés
        self.sequence = [] 

        # nombre de machines utilisées
        self.nombre_machines = nombre_machines

        # durée de l'ordonnancement, c'est-à-dire date de fin de la dernière
        # opération exécutée
        self.duree = 0 

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


    def ordonnancer_job(self, job):
        fin_machine_before=0 #temps de fin de la machine d'avant
        for ind in range(self.nombre_machines):
            date_dispo = self.date_disponibilite[ind] #date de début possible du job  sur la machine
            job.date_debut[ind]=max(date_dispo,fin_machine_before)
            fin_machine_before = job.date_debut[ind] + job.duree_operation[ind]
            self.date_disponibilite[ind]=fin_machine_before
        self.sequence.append(job)


    def ordonnancer_liste_job(self, liste_jobs):
         for job in liste_jobs:
             self.ordonnancer_job(job)
         self.duree =liste_jobs[-1].duree_operation[-1] + liste_jobs[-1].date_debut[-1]


# Pour tester
if __name__ == "__main__":
    c = job.Job(1,[5,9,8,10,1])
    d = job.Job(2,[9,3,10,1,8])
    b = job.Job(3,[9,4,5,8,6])
    a = job.Job(4,[4,8,8,7,2])
    #a.afficher()
    #b.afficher()
    l = [a,b,c,d]
    ordo = Ordonnancement(5)
    ordo.ordonnancer_liste_job(l)
    ordo.afficher()
    a.afficher()
    b.afficher()
    c.afficher()
    d.afficher()
    
