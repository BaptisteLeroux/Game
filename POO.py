class Arme:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats

class Sort:
    def __init__(self, nom, degats, mana):
        self.nom = nom
        self.degats = degats
        self.mana = mana

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

class Guerrier(Personnage):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie, arme)
        self.classe = "Guerrier"
    
    def fonce_dans_le_tas(self, cible):
        print("Je suis un puissant guerrier !")
        print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom} !")
        cible.points_de_vie -= self.arme.degats


class Mage(Personnage):
    def __init__(self, nom, points_de_vie, arme, points_de_mana):
        super().__init__(nom, points_de_vie, arme)
        self.classe = "Mage"
        self.points_de_mana = points_de_mana
    
    def lancer_sort(self, cible, sort):
        if self.points_de_mana >= sort.mana:
            print(f"Je lance le sort {sort.nom} sur {cible.nom} !")
            cible.points_de_vie -= sort.degats
            self.points_de_mana -= sort.mana
        else:
            print("Tu es à court de mana !")

class Archer(Personnage):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie, arme)
        self.classe = "Archer"
    
    def viser(self, cible):
        print("Je vise avec précision !")
        print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom} !")
        cible.points_de_vie -= self.arme.degats


# Exemple d'utilisation :

epee = Arme("Épée", 20)
arc = Arme("Arc", 15)

boule_de_feu = Sort("Boule de feu", 20, 30)
boule_de_glace = Sort("Boule de Glace", 30, 45)

guerrier = Guerrier("Garen", 100, epee)
mage = Mage("Ahri", 80, boule_de_feu, 100)
archer = Archer("Ashe", 90, arc)

guerrier.fonce_dans_le_tas(mage)
mage.lancer_sort(archer, boule_de_feu)
archer.viser(guerrier)

mage.lancer_sort(archer, boule_de_feu)

mage.lancer_sort(archer, boule_de_feu)

mage.lancer_sort(archer, boule_de_glace)



print (archer.points_de_vie)