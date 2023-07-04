import arme
import sort
import personnage as ps
import random as rd
import ennemi



guerrier = ps.Guerrier("Garen", 100, arme.epee, 0)
mage = ps.Mage("Ahri", 80, sort.boule_de_feu, 100, 0)
archer = ps.Archer("Ashe", 90, arme.arc, 0)


#Actions
print ("Premier tour")
guerrier.fonce_dans_le_tas(mage)
mage.lancer_sort(archer, sort.boule_de_feu)
archer.viser(guerrier)

guerrier.info()
mage.info()
archer.info()

print ("Deuxième tour")

mage.lancer_sort(archer, sort.boule_de_feu)

mage.lancer_sort(archer, sort.boule_de_feu)

mage.lancer_sort(archer, sort.boule_de_glace)
print(f"En trébuchant, {guerrier.nom} tombe sur une {arme.mega_massue_de_la_mort_qui_pique.nom} et l'équipe")
guerrier.equiper_arme(arme.mega_massue_de_la_mort_qui_pique)
guerrier.fonce_dans_le_tas(archer)

archer.info()

archer.estVivant()

archer.boire_potion_de_vie()

archer.info()

archer.estVivant()


print(ennemi.sanglier.points_de_vie)
print(ennemi.sanglier.degats)