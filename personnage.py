class Personnage:
    def __init__(self, nom, points_de_vie, arme):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.arme = arme
    
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom} !")
        cible.points_de_vie -= self.arme.degats

    def equiper_arme(self, arme):
        self.arme = arme

    def info(self):
        print(f"{self.nom} possède {self.points_de_vie} points de vie")

    def estVivant(self):
        if (self.points_de_vie > 0) : 
            print("Toujours vivant comme Renaud")
        else :
            print(f"{self.nom} est mort !")
            del self

class Guerrier(Personnage):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie, arme)
        self.classe = "Guerrier"
    
    def fonce_dans_le_tas(self, cible):
        print("Je suis un puissant guerrier !")
        print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom} et inflige {self.arme.degats} points de dégâts!")
        cible.points_de_vie -= self.arme.degats


class Mage(Personnage):
    def __init__(self, nom, points_de_vie, arme, points_de_mana):
        super().__init__(nom, points_de_vie, arme)
        self.classe = "Mage"
        self.points_de_mana = points_de_mana
    
    def lancer_sort(self, cible, sort):
        if self.points_de_mana >= sort.mana:
            print(f"{self.nom} lance le sort {sort.nom} sur {cible.nom}  et inflige {sort.degats} points de dégâts !")
            cible.points_de_vie -= sort.degats
            self.points_de_mana -= sort.mana
        else:
            print(f"{self.nom} est à court de mana !")
    
    def info(self):
        print(f"{self.nom} possède {self.points_de_vie} points de vie et {self.points_de_mana} points de mana")

class Archer(Personnage):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie, arme)
        self.classe = "Archer"
    
    def viser(self, cible):
        print("Je vise avec précision !")
        print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom} et inflige {self.arme.degats} points de dégâts !")
        cible.points_de_vie -= self.arme.degats
