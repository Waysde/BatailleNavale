from Draw import *
import pygame


# TOUS CE QUI SE PASSE LORS DE LA PHASE DE JEU


# Permet au joueur de sélectionner une case pour tirer
def tir(plateau, height, width, taille):
    ecartH = (height-taille)//2  # ecart entre le haut de la fenêtre et le haut du tableau
    ecartW = width-taille-((width-taille*2)//3)  # ecart entre la gauche de la fenêtre et la gauche du tableau
    carre = taille // 10  # taille d'un carré

    X, Y = pygame.mouse.get_pos()  # On récupère les coordonnées de la souris
    x = (X-ecartW)//carre  # On calcule à quelle case elles correspondent
    y = (Y-ecartH)//carre
    if 0 <= y <= 9 and 0 <= x <= 9:  # On vérifie que ces coordonnées sont dans le plateau
        if plateau[y][x] == 0 or 1 <= plateau[y][x] < 2:  # Et qu'on tire sur de l'eau ou un bateau
            # Dans ce cas on return les coordonnées
            return y, x
    # sinon return False
    return False


# Vérifie si le tir touche un bateau
def touche(plateau, y, x):
    if 1 <= plateau[y][x] < 2:
        return True
    else:
        return False


# Vérifie qu'au moins un bateau est safe
def fin(armee):
    for bateau in armee:
        if bateau.etat == "safe":
            return False
    return True


def tour_tir(plateau, plat_ennemi, armee, joueur):
    game = True
    draw_board(plateau, height, width, 450, 1)
    draw_board(plat_ennemi, height, width, 450, 2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Si on détecte un click gauche

                co = tir(plat_ennemi, height, width, 450)  # On récupère les coordonnés de la souris

                if co is not False:  # Si co est une case valide
                    degat = touche(plat_ennemi, co[0], co[1])  # On vérifie si le tir touche
                    # On met à jour le plateau et l'armée
                    plat_ennemi, armee = verif(plat_ennemi, degat, co[0], co[1], armee)

                    draw_board(plateau, height, width, 450, 1)
                    draw_board(plat_ennemi, height, width, 450, 2)  # On met à jour la fenêtre

                    victoire = fin(armee)  # On vérifie si le joueur à gagné
                    if victoire:  # S'il gagne, on arrête le jeu sinon on passe au joueur 2
                        game = False
                        joueur = 0
                        pygame.quit()
                    else:
                        if not degat:
                            pygame.time.delay(1000)
                            # On fait une pause de 1s pour que le joueur est le temps de voir
                            # puis on change de joueur
                            if joueur == 1:
                                joueur = 2
                            else:
                                joueur = 1

    return plateau, plat_ennemi, armee, game, joueur


# Permet de mettre à jour le plateau après un tir
def verif(plateau, degat, y, x, armee):
    if degat:  # Si le tir touche
        plateau[y][x] += 2  # On rajoute 2 à la case pour l'afficher en orange

        for bateau in armee:  # Pour chaque bateau on va venir vérifier si c'est sur lui que l'on a tiré
            if bateau.Vx != 0:  # Si le bateau est horizontal
                if y == bateau.y:  # On vérifie que le bateau est sur la même ligne que le tir
                    if bateau.Vx > 0:  # Puis si le bateau est orienté vers la droite
                        for Bx in range(bateau.x, bateau.x+bateau.Vx+1):  # On parcourt les coordonnées du bateau
                            if Bx == x:  # Si la colonne du tir et du bateau corresponde
                                bateau.damage()  # On lui fait subir des dégâts
                                if bateau.degat == bateau.longueur:  # Si il a autant de dégât que de case
                                    bateau.etat = "coulé"  # Le bateau coule
                                    plateau = entoure(1, 2, plateau, bateau)  # On met à jour le plateau
                                    return plateau, armee
                    # Même principe pour toutes les directions
                    elif bateau.Vx < 0:
                        for Bx in range(bateau.x, bateau.x+bateau.Vx-1, -1):
                            if Bx == x:
                                bateau.damage()
                                if bateau.degat == bateau.longueur:
                                    bateau.etat = "coulé"
                                    plateau = entoure(1, 2, plateau, bateau)
                                    return plateau, armee

            else:
                if x == bateau.x:
                    if bateau.Vy > 0:
                        for By in range(bateau.y, bateau.y+bateau.Vy+1):
                            if By == y:
                                bateau.damage()
                                if bateau.degat == bateau.longueur:
                                    bateau.etat = "coulé"
                                    plateau = entoure(1, 2, plateau, bateau)
                                    return plateau, armee
                    elif bateau.Vy < 0:
                        for By in range(bateau.y, bateau.y+bateau.Vy-1, -1):
                            if By == y:
                                bateau.damage()
                                if bateau.degat == bateau.longueur:
                                    bateau.etat = "coulé"
                                    plateau = entoure(1, 2, plateau, bateau)
                                    return plateau, armee
    else:
        plateau[y][x] = 2  # Si le tir ne touche pas on met la case à 2 pour dire que le tir est dans l'eau

    return plateau, armee


def victoire(gagnant, tableau1, tableau2):

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Si la touche haut est pressée
            if event.key == pygame.K_RETURN:
                pass


# Met à jour le plateau après qu'un bateau est coulé
# On met des cases "dans l'eau" autour du bateau, car il ne peut pas y avoir deux bateaux collés
# A = bateau, B = autour du bateau
def entoure(A, B, plateau, bateau):
    if bateau.Vx != 0:
        if bateau.Vx > 0:  # Si le bateau est horizontal est orienté vers la droite
            for x in range(bateau.x, bateau.x + bateau.Vx + 1):  # On parcourt les coordonnées du bateau
                plateau[bateau.y][x] += A  # On change les valeurs du plateau pour afficher le bateau en noir
                # On vérifie autour du bateau comme dans coller() pour changer les valeurs du plateau
                if bateau.y > 0:
                    plateau[bateau.y - 1][x] = B
                if bateau.y < 9:
                    plateau[bateau.y + 1][x] = B
            if bateau.x + bateau.Vx < 9:
                plateau[bateau.y][bateau.x + bateau.Vx + 1] = B
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x + bateau.Vx + 1] = B
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x + bateau.Vx + 1] = B
            if bateau.x > 0:
                plateau[bateau.y][bateau.x - 1] = B
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x - 1] = B
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x - 1] = B

        else:
            for x in range(bateau.x, bateau.x + bateau.Vx - 1, -1):
                plateau[bateau.y][x] += A
                if bateau.y > 0:
                    plateau[bateau.y - 1][x] = B
                if bateau.y < 9:
                    plateau[bateau.y + 1][x] = B
            if bateau.x < 9:
                plateau[bateau.y][bateau.x + 1] = B
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x + 1] = B
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x + 1] = B
            if bateau.x + bateau.Vx > 0:
                plateau[bateau.y][bateau.x + bateau.Vx - 1] = B
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x + bateau.Vx - 1] = B
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x + bateau.Vx - 1] = B

    else:
        if bateau.Vy > 0:
            for y in range(bateau.y, bateau.y + bateau.Vy + 1):
                plateau[y][bateau.x] += A
                if bateau.x > 0:
                    plateau[y][bateau.x - 1] = B
                if bateau.x < 9:
                    plateau[y][bateau.x + 1] = B
            if bateau.y + bateau.Vy < 9:
                plateau[bateau.y + bateau.Vy + 1][bateau.x] = B
                if bateau.x > 0:
                    plateau[bateau.y + bateau.Vy + 1][bateau.x - 1] = B
                if bateau.x < 9:
                    plateau[bateau.y + bateau.Vy + 1][bateau.x + 1] = B
            if bateau.y > 0:
                plateau[bateau.y - 1][bateau.x] = B
                if bateau.x > 0:
                    plateau[bateau.y - 1][bateau.x - 1] = B
                if bateau.x < 9:
                    plateau[bateau.y - 1][bateau.x + 1] = B
        else:
            for y in range(bateau.y, bateau.y + bateau.Vy - 1, -1):
                plateau[y][bateau.x] += A
                if bateau.x > 0:
                    plateau[y][bateau.x - 1] = B
                if bateau.x < 9:
                    plateau[y][bateau.x + 1] = B
            if bateau.y < 9:
                plateau[bateau.y + 1][bateau.x] = B
                if bateau.x > 0:
                    plateau[bateau.y + 1][bateau.x - 1] = B
                if bateau.x < 9:
                    plateau[bateau.y + 1][bateau.x + 1] = B
            if bateau.y + bateau.Vy > 0:
                plateau[bateau.y + bateau.Vy - 1][bateau.x] = B
                if bateau.x > 0:
                    plateau[bateau.y + bateau.Vy - 1][bateau.x - 1] = B
                if bateau.x < 9:
                    plateau[bateau.y + bateau.Vy - 1][bateau.x + 1] = B
    return plateau
