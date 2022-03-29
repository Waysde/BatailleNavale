from Bateaux import Bateau
import pygame

# TOUS CE QU'IL SE PASSE DURANT LE PLACEMENT DES BATEAUX


def tour_debut(joueur, jeu):
    # Tout ce qui se passe lors du tour d'un joueur
    # affichage du plateau
    afficher_placement(joueur["armee"], jeu)

    # permet de fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu.running = False
            pygame.quit()

        joueur, collision = action(joueur, event, jeu)
        # Regarde les actions du joueur

        if collision is False:  # Si le joueur a fini son tour
            if jeu.joueur1["tour"]:
                jeu.changer_tour()
            else:
                jeu.changer_tour()
                jeu.changer_phase()

    joueur["plateau"] = mouvement(joueur["armee"])  # On met à jour le plateau

    return joueur


def action(joueur, event, jeu):
    # Détecte les actions du joueur
    collision = None
    armee = joueur["armee"]
    plateau = joueur["plateau"]
    boat = joueur["boat"]

    if event.type == pygame.KEYDOWN:
        # Si la touche haut est pressée
        if event.key == pygame.K_UP:
            armee[boat].verif_avancer(plateau)  # On fait avancer le bateau sélectionné (voir Bateaux.py)
            armee[boat].bouger(jeu, jeu.ecart_width)

        # Même chose pour toutes les touches
        elif event.key == pygame.K_DOWN:
            armee[boat].verif_reculer(plateau)
            armee[boat].bouger(jeu, jeu.ecart_width)

        elif event.key == pygame.K_LEFT:
            armee[boat].verif_gauche(plateau, jeu)

        elif event.key == pygame.K_RIGHT:
            armee[boat].verif_droite(plateau, jeu)

        # Si la touche entrée est pressée
        elif event.key == pygame.K_RETURN:
            collision = False
            for bateau in armee:  # pour chaque bateau
                if not collision:
                    # On regarde s'il en touche un autre
                    collision = bateau.coller(plateau)
                else:
                    break

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Si on détecte un click gauche
            boat = suivant(boat)  # On sélectionne le bateau suivant
        if event.button == 3:  # Si on détecte un click droit
            boat = precedant(boat)

    joueur["armee"] = armee
    joueur["plateau"] = plateau
    joueur["boat"] = boat

    return joueur, collision


def afficher_placement(armee, jeu):
    for bateau in armee:
        jeu.win.blit(bateau.image, bateau.rect)


def armement(jeu):
    carre = jeu.carre
    ecart_height = jeu.ecart_height
    ecart_width = jeu.ecart_width

    b1 = Bateau(0, 0, 4, 0, pygame.image.load("image/5 cases.png"), carre, ecart_height, ecart_width)
    b2 = Bateau(0, 2, 3, 0, pygame.image.load("image/4 cases.png"), carre, ecart_height, ecart_width)
    b3 = Bateau(0, 4, 2, 0, pygame.image.load("image/3 cases.png"), carre, ecart_height, ecart_width)
    b4 = Bateau(0, 6, 2, 0, pygame.image.load("image/3 cases.png"), carre, ecart_height, ecart_width)
    b5 = Bateau(0, 8, 1, 0, pygame.image.load("image/2 cases.png"), carre, ecart_height, ecart_width)
    armee = [b1, b2, b3, b4, b5]
    return armee


# Permet de passer au bateau suivant
def suivant(selected_boat):
    selected_boat += 1
    if selected_boat == 5:
        selected_boat = 0
    return selected_boat


# Permet de passer au bateau precedent
def precedant(selected_boat):
    selected_boat -= 1
    if selected_boat == -1:
        selected_boat = 4
    return selected_boat


# Permet de changer le plateau après chaque mouvement
def mouvement(armee):
    plateau = tableau()
    for bateau in armee:
        if bateau.Vx != 0:
            if bateau.Vx > 0:  # Si le bateau est horizontal est orienté vers la droite
                for x in range(bateau.x, bateau.x + bateau.Vx + 1):  # On parcourt les coordonnées du bateau
                    plateau[bateau.y][x] = 1
            # Et aussi selon sa direction
            else:
                for x in range(bateau.x, bateau.x + bateau.Vx - 1, -1):
                    plateau[bateau.y][x] = 1

        else:
            if bateau.Vy > 0:
                for y in range(bateau.y, bateau.y + bateau.Vy + 1):
                    plateau[y][bateau.x] = 1
            else:
                for y in range(bateau.y, bateau.y + bateau.Vy - 1, -1):
                    plateau[y][bateau.x] = 1

    return plateau


# créer un tableau rempli de 0
def tableau():
    plateau = []
    for i in range(10):
        plateau.append([0 for j in range(10)])
    return plateau
