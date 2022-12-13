from individu import Individu


class Evaluateur():
    
    def __init__(self, indiv: Individu):
        self.individu = indiv
        
    def evaluer(self):
        return self.fonction_evaluation();
    
    def fonction_evaluation():
        return False