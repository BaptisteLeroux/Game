class Arme:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats

armes_disponibles = [
    Arme("Épée", 20),
    Arme("Arc", 15),
    Arme("Mega massue de la mort qui pique", 40)
]


epee = Arme("Épée", 20)
arc = Arme("Arc", 15)
mega_massue_de_la_mort_qui_pique = Arme("Mega massue de la mort qui pique", 40)