from Bateaux import *
from Draw import *
import pygame

# TOUS CE QU'IL SE PASSE DURANT LE PLACEMENT DES BATEAUX


# créer un tableau rempli de 0
def tableau():
    plateau = []
    for i in range(10):
        plateau.append([0 for j in range(10)])
    return plateau


# Créer les bateaux et les met dans une liste armée
def armement():
    b1 = Bateau(0, 0, 4, 0)
    b2 = Bateau(0, 2, 3, 0)
    b3 = Bateau(0, 4, 2, 0)
    b4 = Bateau(0, 6, 2, 0)
    b5 = Bateau(0, 8, 1, 0)
    armee = [b1, b2, b3, b4, b5]
    return armee


# Permet de passer au bateau suivant
def next(SelectedBoat):
    SelectedBoat += 1
    if SelectedBoat == 5:
        SelectedBoat = 0
    return SelectedBoat


# Permet de passer au bateau précedent
def previous(SelectedBoat):
    SelectedBoat -= 1
    if SelectedBoat == -1:
        SelectedBoat = 4
    return SelectedBoat


# Tout ce qu'il ce passe lors d'un tour pendant la phase de placement des bateaux
def placement(plateau, armee, boat, event):
    colision = -1

    if event.type == pygame.KEYDOWN:
        # Si la touche haut est pressée
        if event.key == pygame.K_UP:
            armee[boat].move_forward(plateau)  # On fait avancer le bateau sélectionné

        # Même chose pour toutes les touches
        elif event.key == pygame.K_DOWN:
            armee[boat].move_backward(plateau)

        elif event.key == pygame.K_LEFT:
            armee[boat].turn_left(plateau)

        elif event.key == pygame.K_RIGHT:
            armee[boat].turn_right(plateau)

        # Si la touche enter est pressée
        elif event.key == pygame.K_RETURN:
            colision = 0
            for bateau in armee:  # pour chaque bateau
                if colision == 0:
                    # On compte le nombre de fois qu'il en touche un autre
                    colision += bateau.coller(plateau)
                else:
                    break

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Si on détecte un click gauche
            boat = next(boat)  # On sélectionne le bateau suivant
        if event.button == 3:  # Si on détecte un click droit
            boat = previous(boat)

    return plateau, armee, boat, colision


def tour_debut(plateau, armee, boat, joueur):
    running = True
    debut = True
    game = False
    # affichage du plateau
    draw_board(plateau, height, width, 450, 0)

    # permet de fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        plateau, armee, boat, colision = placement(plateau, armee, boat, event)

        if colision == 0:
            if joueur == 1:
                joueur = 2
            else:
                debut = False
                joueur = 1
                game = True

    plateau = mouvement(armee)  # On met à jour le plateau

    return running, joueur, plateau, armee, boat, debut, game


# Permet de changer le plateau après chaque mouvement
def mouvement(armee):
    plateau = tableau()
    for bateau in armee:
        if bateau.Vx != 0:
            if bateau.Vx > 0:  # Si le bateau est horizontal est orienté vers la droite
                for x in range(bateau.x, bateau.x + bateau.Vx + 1):  # On parcourt les coordonnées du bateau
                    # On affiche une valeur différente selon si c'est l'avant, l'arrière ou le milieu du bateau
                    if x == bateau.x:
                        plateau[bateau.y][x] = 1.00
                    elif x == bateau.x + bateau.Vx:
                        plateau[bateau.y][x] = 1.10
                    else:
                        plateau[bateau.y][x] = 1.20
            # Et aussi selon sa direction
            else:
                for x in range(bateau.x, bateau.x + bateau.Vx - 1, -1):
                    if x == bateau.x:
                        plateau[bateau.y][x] = 1.01
                    elif x == bateau.x + bateau.Vx:
                        plateau[bateau.y][x] = 1.11
                    else:
                        plateau[bateau.y][x] = 1.20

        else:
            if bateau.Vy > 0:
                for y in range(bateau.y, bateau.y + bateau.Vy + 1):
                    if y == bateau.y:
                        plateau[y][bateau.x] = 1.02
                    elif y == bateau.y + bateau.Vy:
                        plateau[y][bateau.x] = 1.12
                    else:
                        plateau[y][bateau.x] = 1.21
            else:
                for y in range(bateau.y, bateau.y + bateau.Vy - 1, -1):
                    if y == bateau.y:
                        plateau[y][bateau.x] = 1.03
                    elif y == bateau.y + bateau.Vy:
                        plateau[y][bateau.x] = 1.13
                    else:
                        plateau[y][bateau.x] = 1.21

    return plateau
