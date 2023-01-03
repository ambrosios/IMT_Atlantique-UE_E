from math import exp
import random
from scipy import constants
from classes.Job import Job
from classes.Ordonnancement import Ordonnancement
from classes.DataLoader import DataLoader
import config
import time
from classes.Flowshop import Flowshop

class Recuit():
    
    T: int
    Sc: Flowshop
    S_star: Flowshop
    heuristique: Flowshop
    nombre_machines: int
    arret = False
    stats = {"Voisin meilleur": 0,
             "Ajustement de température": 0,
             "Ajustement de Sc": 0,
             "Ajustement Sc meilleur": 0,
             "Temps d'exécution (s)": 0
            }
    voisinage = []
    
    def __init__(self):
                
        self.N_execution = config.NOMBRE_ITERATIONS
        
        self.T = 1
        
        data = DataLoader(config.DONNEES_INITIALES)
        self.liste_jobs = data.get_liste_jobs()
        self.nombre_machines = data.get_nombre_machines()
        
        self.Sc = Flowshop(self.liste_jobs, self.nombre_machines)
        self.Sc.ordonnancer_selon_NEH()
        
        self.heuristique = Flowshop(self.Sc.liste_jobs, self.nombre_machines)
        
        self.S_star = self.Sc
        
        if config.AFFICHAGE_NOM_ALGORITHME:
            self.afficher_nom()
        
        if config.AFFICHAGE_DONNEES_PROBLEME:
            self.afficher_donnees_probleme()
        
        if config.AFFICHAGE_HEURISTIQUE:
            self.afficher_heuristique()


    def executer(self):
        self.c = 0
        nouveau_Sc = True
        while not(self.critere_arret()):
            
            self.c += 1
            
            if nouveau_Sc:
                # self.voisinage = self.voisinage + self.Sc.get_voisinage()
                self.voisinage = self.Sc.get_voisinage()
                nouveau_Sc = False
                
            s = self.get_dans_voisinage(self.Sc)
        
            if config.AFFICHAGE_VOISIN_CHOISI:
                print("Solution considérée :", s.str())
            
            if s.get_duree() < self.Sc.get_duree():
                self.S_star = s
                # self.Sc = s
                
                if config.AFFICHAGE_VOISIN_CHOISI:
                    print("Solution considérée :", s.str())
                
                self.stats['Voisin meilleur'] += 1
                
            else:
                
                self.stats['Ajustement de température'] += 1
                
                p = random.uniform(0, 1)
                if p <= exp((self.Sc.get_duree() - s.get_duree())/(constants.k * self.T)):
                    self.stats['Ajustement de Sc'] += 1
                    
                    nouveau_Sc = True
                    self.Sc = s
                    
                if self.Sc.get_duree() < self.S_star.get_duree():
                    self.stats['Ajustement Sc meilleur'] += 1
                    
                    self.S_star = self.Sc
                    
                self.T = self.T - config.ALPHA*self.T
                
                if self.c <= config.AFFICHAGE_T:
                    print("Valeur de T à l'itération", self.c, ":", self.T)
                
        if config.AFFICHAGE_RESULTAT:
            self.afficher_resultat()

        self.stats['Temps d\'exécution (s)'] = time.process_time() - self.stats['Temps d\'exécution (s)']

        return (self.S_star.str(), self.S_star.get_duree())

            
    def get_dans_voisinage(self, origine: list):
        if len(self.voisinage) == 0:
            self.arret = True
            voisin = origine

        else:
            random.shuffle(self.voisinage)
            voisin = self.voisinage[0]
            self.voisinage.pop(0)
        
        return voisin

    def set_temps_initial(self, temps):
        self.stats['Temps d\'exécution (s)'] = temps
  
    def critere_arret(self):
        return self.c >= self.N_execution or self.arret

    def afficher_nom(self):
        print()
        print("******************************************")
        print("*        Algorithme recuit simulé        *")
        print("******************************************")
    
    def afficher_donnees_probleme(self):
        print()
        print("*************** PARAMÈTRES ***************")
        print()
        print("Jeu de données :", config.DONNEES_INITIALES)
        print("Nombre de jobs :", len(self.liste_jobs))
        print("Nombre de machines :", self.nombre_machines)
    
    def afficher_heuristique(self):
        print()
        print("********** SOLUTION HEURISTIQUE **********")
        print()
        print("Heuristique :", self.Sc.str(), "avec une durée de", self.Sc.get_duree())
    
    def afficher_resultat(self):
        print()
        print("************* RÉSULTAT FINAL *************")
        print()
        print("Optimum local trouvé :", self.S_star.str(), "avec une durée de", self.S_star.get_duree())
    
    
    def afficher_stats(self):
        print()
        print("************** STATISTIQUES **************")
        print()
        print("* Nombre d'itérations :", self.c)
        for stat in self.stats.keys():
            print("*", stat, ":", self.stats[stat])
        print()
        print("******************************************")
        print()
