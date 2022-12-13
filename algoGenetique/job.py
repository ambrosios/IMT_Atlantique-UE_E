#!/usr/bin/env python

__author__ = 'Chams Lahlou'
__date__ = 'Octobre 2019 - novembre 2020'
__version__ = '0.2'

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

    def afficher(self):
        print("Job", self.numero,"de durée totale", self.duree, ":")
        for numero in range(len(self.duree_operation)):
            print("  opération", numero, 
                  ": durée =", self.duree_operation[numero], 
                  "et début =", self.date_debut[numero])