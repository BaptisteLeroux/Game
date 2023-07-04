from arme import Arme, armes_disponibles
from sort import Sort, sorts_disponibles
import personnage as ps

# Création des objets
epee = armes_disponibles[0]
arc = armes_disponibles[1]
mega_massue_de_la_mort_qui_pique = armes_disponibles[2]


boule_de_feu = sorts_disponibles[0]
boule_de_glace = sorts_disponibles[1]

guerrier = ps.Guerrier("Garen", 100, epee)
mage = ps.Mage("Ahri", 80, boule_de_feu, 100)
archer = ps.Archer("Ashe", 90, arc)


#Actions
print ("Premier tour")
guerrier.fonce_dans_le_tas(mage)
mage.lancer_sort(archer, boule_de_feu)
archer.viser(guerrier)

guerrier.info()
mage.info()
archer.info()

print ("Deuxième tour")

mage.lancer_sort(archer, boule_de_feu)

mage.lancer_sort(archer, boule_de_feu)

mage.lancer_sort(archer, boule_de_glace)
print(f"En trébuchant, {guerrier.nom} tombe sur une {mega_massue_de_la_mort_qui_pique.nom} et l'équipe")
guerrier.equiper_arme(mega_massue_de_la_mort_qui_pique)
guerrier.fonce_dans_le_tas(archer)

archer.info()

archer.estVivant()
