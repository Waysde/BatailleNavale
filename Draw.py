import pygame

# ___________CREATION DE LA FENETRE___________
width = 1080
height = 720
pygame.display.set_caption("Bataille Navale")
win = pygame.display.set_mode((width, height))

# ___________IMPORTATION DES IMAGES___________
Bavant = pygame.image.load("image/BAvant.png").convert_alpha()
Bfin = pygame.image.load("image/BFin.png").convert_alpha()
Bmilieu = pygame.image.load("image/BMilieu.png").convert_alpha()
Cavant = pygame.image.load("image/CAvant.png").convert_alpha()
Cfin = pygame.image.load("image/CFin.png").convert_alpha()
Cmilieu = pygame.image.load("image/CMilieu.png").convert_alpha()
Tavant = pygame.image.load("image/TAvant.png").convert_alpha()
Tfin = pygame.image.load("image/TFin.png").convert_alpha()
Tmilieu = pygame.image.load("image/TMilieu.png").convert_alpha()
Croix = pygame.image.load("image/Touche.png").convert_alpha()


# ___________PERMET DE AFFICHER LE PLATEAU___________
# taille = taille du plateau
# n = plateau de gauche(1), de droite(2) ou au milieu(0)
# Si le plateau est à droite le joueur ne voit pas les bateaux
def draw_board(plateau, height, width, taille, n):
    ecartH = (height - taille) // 2  # ecart entre le haut de la fenêtre et le haut du tableau
    if n == 0:
        ecartW = (width - taille) // 2  # ecart entre la gauche de la fenêtre et la gauche du tableau
    elif n == 1:
        ecartW = (width - taille * 2) // 3  # meme chose quand le tableau est à gauche
    else:
        ecartW = width - taille - ((width - taille * 2) // 3)  # et quand il est à droite
    carre = taille // 10  # taille d'un carré

    border = (0, 0, 0)

    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            # On parcourt le plateau et pour chaque case on affiche une image selon sa valeur

            case = plateau[y][x]
            if n == 2:  # On montre les bateaux que pour le joueur
                if 1 <= case < 2:
                    case = 0
                elif 3 <= case < 4:
                    case = 5

            draw_case(case, x * carre + ecartW, y * carre + ecartH, carre)

            # Créer une bordure autour des cases
            pygame.draw.rect(win, border, pygame.Rect(x * carre + ecartW, y * carre + ecartH, carre, carre), 1)
            # Met à jour la fenêtre
            pygame.display.flip()


def draw_case(case, posx, posy, carre):
    # toutes les couleurs en RGB
    eau = (119, 181, 254)
    ratee = (173, 204, 255)

    if case == 0:
        pygame.draw.rect(win, eau, pygame.Rect(posx, posy, carre, carre))

    elif case == 1.00:
        win.blit(Bfin, (posx, posy))
    elif case == 1.01:
        image = pygame.transform.rotate(Bfin, 180)
        win.blit(image, (posx, posy))
    elif case == 1.02:
        image = pygame.transform.rotate(Bfin, -90)
        win.blit(image, (posx, posy))
    elif case == 1.03:
        image = pygame.transform.rotate(Bfin, 90)
        win.blit(image, (posx, posy))
    elif case == 1.10:
        win.blit(Bavant, (posx, posy))
    elif case == 1.11:
        image = pygame.transform.rotate(Bavant, 180)
        win.blit(image, (posx, posy))
    elif case == 1.12:
        image = pygame.transform.rotate(Bavant, -90)
        win.blit(image, (posx, posy))
    elif case == 1.13:
        image = pygame.transform.rotate(Bavant, 90)
        win.blit(image, (posx, posy))
    elif case == 1.20:
        win.blit(Bmilieu, (posx, posy))
    elif case == 1.21:
        image = pygame.transform.rotate(Bmilieu, 90)
        win.blit(image, (posx, posy))

    elif case == 2:
        pygame.draw.rect(win, ratee, pygame.Rect(posx, posy, carre, carre))

    elif case == 3.00:
        win.blit(Tfin, (posx, posy))
    elif case == 3.01:
        image = pygame.transform.rotate(Tfin, 180)
        win.blit(image, (posx, posy))
    elif case == 3.02:
        image = pygame.transform.rotate(Tfin, -90)
        win.blit(image, (posx, posy))
    elif round(case, 2) == 3.03:
        image = pygame.transform.rotate(Tfin, 90)
        win.blit(image, (posx, posy))
    elif case == 3.10:
        win.blit(Tavant, (posx, posy))
    elif round(case, 2) == 3.11:
        image = pygame.transform.rotate(Tavant, 180)
        win.blit(image, (posx, posy))
    elif case == 3.12:
        image = pygame.transform.rotate(Tavant, -90)
        win.blit(image, (posx, posy))
    elif case == 3.13:
        image = pygame.transform.rotate(Tavant, 90)
        win.blit(image, (posx, posy))
    elif case == 3.20:
        win.blit(Tmilieu, (posx, posy))
    elif case == 3.21:
        image = pygame.transform.rotate(Tmilieu, 90)
        win.blit(image, (posx, posy))

    elif case == 4.00:
        win.blit(Cfin, (posx, posy))
    elif case == 4.01:
        image = pygame.transform.rotate(Cfin, 180)
        win.blit(image, (posx, posy))
    elif case == 4.02:
        image = pygame.transform.rotate(Cfin, -90)
        win.blit(image, (posx, posy))
    elif case == 4.03:
        image = pygame.transform.rotate(Cfin, 90)
        win.blit(image, (posx, posy))
    elif case == 4.10:
        win.blit(Cavant, (posx, posy))
    elif case == 4.11:
        image = pygame.transform.rotate(Cavant, 180)
        win.blit(image, (posx, posy))
    elif case == 4.12:
        image = pygame.transform.rotate(Cavant, -90)
        win.blit(image, (posx, posy))
    elif case == 4.13:
        image = pygame.transform.rotate(Cavant, 90)
        win.blit(image, (posx, posy))
    elif case == 4.20:
        win.blit(Cmilieu, (posx, posy))
    elif case == 4.21:
        image = pygame.transform.rotate(Cmilieu, 90)
        win.blit(image, (posx, posy))

    elif case == 5:
        win.blit(Croix, (posx, posy))