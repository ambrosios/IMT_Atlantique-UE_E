from Individu import Individu
from ordonnancement import Ordonnancement

# Une instance de Evaluateur permet d'évaluer un individu
# Un Evaluateur permet de :
#   * évaluer un Individu (ordonnancemens) : déterminer la durée maximale de l'ordonnancement

class Evaluateur():
    
    def __init__(self, indiv: Individu, nb_machines: int):
        self.individu = indiv
        self.nombre_machines = nb_machines
    
    # evaluer permet d'évaluer un individu
    def evaluer(self):
        self.eval = self.fonction_evaluation();
        return self.eval
    
    # fonction_evaluation permet d'obtenir l'évaluation d'un individu
    # fonction_evaluation est ici définie comme la durée minimale possible avec l'ordonnancement
    def fonction_evaluation(self):
        ordo = Ordonnancement(self.nombre_machines);
        ordo.ordonnancer_liste_job(self.individu.sequence)
        return ordo.duree;
    
    # get_individu retourne l'individu évalué
    def get_individu(self):
        return self.individu
    
    # get_eval retourne la valeur de l'évalusation de l'individu évalué
    def get_eval(self):
        return self.eval
    
    # __lt__ sert de comparaison des éléments pour les heapq
    def __lt__(self, indiv2):
        return self.evaluer() < indiv2.evaluer()