class Mob:
    def __init__(self, nom, points_de_vie, degats, niveau ):
        self.nom = nom
        self.niveau = niveau 
        self.points_de_vie = points_de_vie
        self.degats = degats
        

    
    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom} et inflige {self.degats} !")
        cible.points_de_vie -= self.degats


class Sanglier(Mob): 
    def __init__(self, nom, niveau):
        points_de_vie = niveau * 10
        degats = niveau * 5
        super().__init__(nom, points_de_vie, degats, niveau)

        
sanglier = Sanglier("Sanglier Mignon", 1)

