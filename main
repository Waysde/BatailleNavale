from Placement import *
from Jeu import *

pygame.init()


# ___________INITIALISATION DES VALEURS___________
armee1 = armement()  # Créer une armée composée de bateaux
boat1 = 0  # Permet de voir quel bateau est sélectionné dans l'armée
plateau1 = mouvement(armee1)  # Place les bateaux de l'armée sur le plateau

# meme chose avec l'armée 2
armee2 = armement()
boat2 = 0
plateau2 = mouvement(armee2)

# reset les valeurs qui permettent de commencer la partie
joueur = 1
running = True
debut = True
game = True

# Fait tourner la fenêtre(pas utilisé pour le moment, car on joue tout le temps)
while running:

    # Boucle pour la phase de placement des bateaux
    while debut:

        # boucle pour la phase de placement des bateaux du joueur 1
        while joueur == 1:

            running, joueur, plateau1, armee1, boat1, debut, game = tour_debut(plateau1, armee1, boat1, 1)

        # Même chose pour le joueur 2
        while joueur == 2:

            running, joueur, plateau2, armee2, boat2, debut, game = tour_debut(plateau2, armee2, boat2, 2)

    win.fill((0, 0, 0))
    while game:

        while joueur == 1:

            plateau1, plateau2, armee2, game, joueur = tour_tir(plateau1, plateau2, armee2, 1)

        # Même chose pour le joueur 2
        while joueur == 2:

            plateau2, plateau1, armee1, game, joueur = tour_tir(plateau2, plateau1, armee1, 2)
