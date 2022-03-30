from Placement import *
from Tir import *
from Game import Game

# ___________INITIALISATION DES VALEURS___________
pygame.init()

jeu = Game(1920, 60)
jeu.image()

pygame.display.set_caption("Bataille Navale")
win = pygame.display.set_mode((jeu.width, jeu.height))

clock = pygame.time.Clock()

armee1 = armement(jeu)
armee2 = armement(jeu)
plateau1 = mouvement(armee1)
plateau2 = mouvement(armee2)

jeu.init_valeur(armee1, armee2, plateau1, plateau2, win)

# _________________BOUCLE DU JEU_________________
while jeu.running:

    jeu.background()

    if jeu.debut:
        jeu.debuter()

    # Phase de placement des bateaux
    elif jeu.placement:

        # Phase de placement des bateaux du joueur 1
        if jeu.joueur1["tour"]:
            # voir Placement.py
            jeu.joueur1 = tour_debut(jeu.joueur1, jeu)

        # Même chose pour le joueur 2
        if jeu.joueur2["tour"]:

            jeu.joueur2 = tour_debut(jeu.joueur2, jeu)

    elif jeu.tir:

        if jeu.joueur1["tour"]:
            # voir Tir.py
            jeu.joueur2 = tour_tir(jeu.joueur1, jeu.joueur2, jeu)

        # Même chose pour le joueur 2
        if jeu.joueur2["tour"]:

            jeu.joueur1 = tour_tir(jeu.joueur2, jeu.joueur1, jeu)

    else:
        afficher_jeu(jeu.perdant, jeu.gagnant, jeu)
        jeu.finir()

    pygame.display.flip()
    clock.tick(jeu.FPS)

    if jeu.changement:
        jeu.changer_tour()
