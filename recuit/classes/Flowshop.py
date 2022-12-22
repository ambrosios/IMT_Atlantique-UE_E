#!/usr/bin/env python

"""Résolution du flowshop de permutation : 

 - par l'algorithme NEH
 - par une méthode évaluation-séparation
 """

__author__ = 'Chams Lahlou'
__coauthor__ = 'Amaury Colin'
__date__ = 'Octobre 2019 - décembre 2022'
__version__ = '0.3'

import classes.Job
from classes.Ordonnancement import Ordonnancement
import config

import numpy as np;

import heapq

# valeurt maximale d'un entier
MAXINT = 10000

class Flowshop():
    def __init__(self, liste_jobs: list, nombre_machines: int):

        # nombre de jobs pour le problème
        self.nombre_jobs = len(liste_jobs)

        # nombre de machines pour le problème
        self.nombre_machines = nombre_machines

        # ensemble des jobs pour le problème (l'ordre n'est pas important)
        self.liste_jobs = liste_jobs[:]

    def ordonnancer_selon_NEH(self):
        """renvoie la liste des jobs ordonnée selon NEH"""
    	
        # on trie les jobs selon leurs durées décroissantes
        l = [job for job in self.liste_jobs]
        l = sorted(l, key=lambda job:job.duree, reverse=True)
        
        meilleurSousOrdo = [l[0]];
        ordonneur = Ordonnancement(self.nombre_machines);
        
        for jobCourantIndex in range(1, len(l)):
            sousOrdos = [];
            for k in range(0, len(meilleurSousOrdo) + 1):
                sousOrdo = meilleurSousOrdo[:];
                sousOrdo.insert(k, l[jobCourantIndex]);
                sousOrdos.append(sousOrdo);
            
            ordonneur.ordonnancer_liste_job(sousOrdos[0]);
            meilleurSousOrdo = ordonneur.sequence[:];
            CmaxMini = ordonneur.get_duree();
            
            for j in range(0, len(sousOrdos)):
                ordonneur.ordonnancer_liste_job(sousOrdos[j]);
                if CmaxMini > ordonneur.get_duree():
                    meilleurSousOrdo =  ordonneur.sequence[:];
                    CmaxMini = ordonneur.get_duree();
            
            ordonneur.ordonnancer_liste_job(meilleurSousOrdo)
                
        self.liste_jobs = meilleurSousOrdo
        
    def get_duree(self):
        ordo = Ordonnancement(self.nombre_machines)
        ordo.ordonnancer_liste_job(self.liste_jobs)
        return ordo.get_duree()
 
    def get_voisinage(self):
        v = []
        for i in range(len(self.liste_jobs)):
            for j in range(i + 1, len(self.liste_jobs)):
                voisin = Flowshop(self.liste_jobs[:], self.nombre_machines)
                voisin.permuter(i, j)
                v.append(voisin)
                
                if config.AFFICHAGE_NOUVEAU_VOISIN:
                    print("Nouveau voisin :", voisin.str())
                    
        return v
    
    def permuter(self, i, j):
        e1 = self.liste_jobs[i]
        e2 = self.liste_jobs[j]
        
        s = self.liste_jobs[:]
        s[i], s[j] = e2, e1
        
        self.liste_jobs = s[:]


    def str(self):
        s = "["
        for j in self.liste_jobs:
            s+= str(j.numero) + ", "
        s = s[: -2]
        s+="]"
        return s