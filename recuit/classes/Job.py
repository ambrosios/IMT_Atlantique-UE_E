#!/usr/bin/env python

__author__ = 'Chams Lahlou'
__coauthor__ = 'Amaury Colin'
__date__ = 'Octobre 2019 - décembre 2022'
__version__ = '0.2'

import numpy as np;

class Job():
    def __init__(self, numero, liste_durees=[]):
        """
        Crée un job en indiquant son numéro et les durées de ses opérations.
        Les opérations sont numérotées à partir de 0.
        """

        # numéro du job
        self.numero = numero

        # durée de chaque opération du job
        self.duree_operation = [i for i in liste_durees]

        # date de début de chaque opération si le job est ordonnancé
        self.date_debut = [None for i in liste_durees]

        #####################
        # exo 1 :  A REMPLIR
        #####################
        self.duree = np.sum(self.duree_operation);



    def afficher(self):
        print("Job", self.numero,"de durée totale", self.duree, ":")
        for numero in range(len(self.duree_operation)):
            print("  opération", numero, 
                  ": durée =", self.duree_operation[numero], 
                  "et début =", self.date_debut[numero])

# Pour tester
if __name__ == "__main__":
    a = Job(1,[1,3,5,18,23])
    # a.afficher()
    print(a.duree);