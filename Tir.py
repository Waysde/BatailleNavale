import pygame


# TOUS CE QUI SE PASSE LORS DE LA PHASE DE JEU


def tour_tir(joueur, ennemi, jeu):

    afficher_jeu(joueur, ennemi, jeu)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                co = tir(ennemi["plateau"], jeu)

                if co is not False:
                    degat = verif_touche(ennemi["plateau"], co[0], co[1])

                    ennemi["plateau"], ennemi["armee"] = trouver_bateau(ennemi["plateau"], degat, co[0], co[1], ennemi["armee"])

                    gagnant = fin(ennemi["armee"])
                    if gagnant:
                        jeu.victoire(joueur, ennemi)
                    else:
                        if not degat:
                            jeu.changement = True

                    afficher_jeu(joueur, ennemi, jeu)

    return ennemi


# Permet au joueur de sélectionner une case pour tirer
def tir(plateau, jeu):

    souris_x, souris_y = pygame.mouse.get_pos()
    x = (souris_x-jeu.ecart_width[1])//jeu.carre
    y = (souris_y-jeu.ecart_height)//jeu.carre

    if 0 <= y <= 9 and 0 <= x <= 9:
        if plateau[y][x] == 0 or plateau[y][x] == 1:

            return y, x

    return False


# Vérifie si le tir touche un bateau
def verif_touche(plateau, y, x):
    if plateau[y][x] == 1:
        return True
    else:
        return False


# Vérifie qu'au moins un bateau est safe
def fin(armee):
    for bateau in armee:
        if bateau.safe:
            return False
    return True


def trouver_bateau(plateau, degat, y, x, armee):
    if degat:
        plateau[y][x] = 3

        for bateau in armee:
            if bateau.Vx != 0:
                if y == bateau.y:
                    if bateau.Vx > 0:
                        for Bx in range(bateau.x, bateau.x+bateau.Vx+1):
                            if Bx == x:
                                return toucher(bateau, plateau), armee
                    else:
                        for Bx in range(bateau.x, bateau.x+bateau.Vx-1, -1):
                            if Bx == x:
                                return toucher(bateau, plateau), armee

            else:
                if x == bateau.x:
                    if bateau.Vy > 0:
                        for By in range(bateau.y, bateau.y+bateau.Vy+1):
                            if By == y:
                                return toucher(bateau, plateau), armee
                    else:
                        for By in range(bateau.y, bateau.y+bateau.Vy-1, -1):
                            if By == y:
                                return toucher(bateau, plateau), armee
    else:
        plateau[y][x] = 2  # Si le tir ne touche pas on met la case à 2 pour dire que le tir est dans l'eau

    return plateau, armee


def toucher(bateau, plateau):
    bateau.damage()

    if bateau.degat == bateau.longueur:

        bateau.safe = False
        plateau = entoure(plateau, bateau)

        bateau.origin_image = pygame.image.load(f"image/{bateau.longueur} casesCoule.png")
        bateau.tourner()

    return plateau


def afficher_jeu(joueur, ennemi, jeu):
    for bateau in joueur["armee"]:
        bateau.bouger(jeu, jeu.ecart_width[0])
        jeu.win.blit(bateau.image, bateau.rect)
    draw(jeu, joueur["plateau"], jeu.ecart_width[0])

    for bateau in ennemi["armee"]:
        if not bateau.safe or not jeu.tir:
            bateau.bouger(jeu, jeu.ecart_width[1])
            jeu.win.blit(bateau.image, bateau.rect)

    draw(jeu, ennemi["plateau"], jeu.ecart_width[1])


def draw(jeu, plateau, ecart_width):
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):

            if plateau[y][x] == 2:
                pass
                jeu.win.blit(jeu.images[0], (x * jeu.carre + ecart_width, y * jeu.carre + jeu.ecart_height))
            elif plateau[y][x] == 3:
                pass
                jeu.win.blit(jeu.images[1], (x * jeu.carre + ecart_width, y * jeu.carre + jeu.ecart_height))


# Met à jour le plateau après qu'un bateau est coulé
# On met des cases "dans l'eau" autour du bateau, car il ne peut pas y avoir deux bateaux collés
# A = bateau, B = autour du bateau
def entoure(plateau, bateau):
    if bateau.Vx != 0:
        if bateau.Vx > 0:  # Si le bateau est horizontal est orienté vers la droite
            for x in range(bateau.x, bateau.x + bateau.Vx + 1):  # On parcourt les coordonnées du bateau
                plateau[bateau.y][x] = 4  # On change les valeurs du plateau pour afficher le bateau en noir
                # On vérifie autour du bateau comme dans coller() pour changer les valeurs du plateau
                if bateau.y > 0:
                    plateau[bateau.y - 1][x] = 2
                if bateau.y < 9:
                    plateau[bateau.y + 1][x] = 2
            if bateau.x + bateau.Vx < 9:
                plateau[bateau.y][bateau.x + bateau.Vx + 1] = 2
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x + bateau.Vx + 1] = 2
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x + bateau.Vx + 1] = 2
            if bateau.x > 0:
                plateau[bateau.y][bateau.x - 1] = 2
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x - 1] = 2
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x - 1] = 2

        else:
            for x in range(bateau.x, bateau.x + bateau.Vx - 1, -1):
                plateau[bateau.y][x] = 4
                if bateau.y > 0:
                    plateau[bateau.y - 1][x] = 2
                if bateau.y < 9:
                    plateau[bateau.y + 1][x] = 2
            if bateau.x < 9:
                plateau[bateau.y][bateau.x + 1] = 2
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x + 1] = 2
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x + 1] = 2
            if bateau.x + bateau.Vx > 0:
                plateau[bateau.y][bateau.x + bateau.Vx - 1] = 2
                if bateau.y > 0:
                    plateau[bateau.y - 1][bateau.x + bateau.Vx - 1] = 2
                if bateau.y < 9:
                    plateau[bateau.y + 1][bateau.x + bateau.Vx - 1] = 2

    else:
        if bateau.Vy > 0:
            for y in range(bateau.y, bateau.y + bateau.Vy + 1):
                plateau[y][bateau.x] = 4
                if bateau.x > 0:
                    plateau[y][bateau.x - 1] = 2
                if bateau.x < 9:
                    plateau[y][bateau.x + 1] = 2
            if bateau.y + bateau.Vy < 9:
                plateau[bateau.y + bateau.Vy + 1][bateau.x] = 2
                if bateau.x > 0:
                    plateau[bateau.y + bateau.Vy + 1][bateau.x - 1] = 2
                if bateau.x < 9:
                    plateau[bateau.y + bateau.Vy + 1][bateau.x + 1] = 2
            if bateau.y > 0:
                plateau[bateau.y - 1][bateau.x] = 2
                if bateau.x > 0:
                    plateau[bateau.y - 1][bateau.x - 1] = 2
                if bateau.x < 9:
                    plateau[bateau.y - 1][bateau.x + 1] = 2
        else:
            for y in range(bateau.y, bateau.y + bateau.Vy - 1, -1):
                plateau[y][bateau.x] = 4
                if bateau.x > 0:
                    plateau[y][bateau.x - 1] = 2
                if bateau.x < 9:
                    plateau[y][bateau.x + 1] = 2
            if bateau.y < 9:
                plateau[bateau.y + 1][bateau.x] = 2
                if bateau.x > 0:
                    plateau[bateau.y + 1][bateau.x - 1] = 2
                if bateau.x < 9:
                    plateau[bateau.y + 1][bateau.x + 1] = 2
            if bateau.y + bateau.Vy > 0:
                plateau[bateau.y + bateau.Vy - 1][bateau.x] = 2
                if bateau.x > 0:
                    plateau[bateau.y + bateau.Vy - 1][bateau.x - 1] = 2
                if bateau.x < 9:
                    plateau[bateau.y + bateau.Vy - 1][bateau.x + 1] = 2
    return plateau
