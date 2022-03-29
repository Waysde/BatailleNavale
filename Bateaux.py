import pygame


class Bateau(pygame.sprite.Sprite):

    def __init__(self, x, y, Vx, Vy, image, carre, ecart_height, ecart_width):
        super().__init__()
        self.x = x              # int = la colonne où se trouve l'arrière du bateau
        self.y = y              # int = la ligne où se trouve l'arrière du bateau
        self.Vx = Vx            # int = le nombre de cases à parcourir horizontalement depuis l'arrière du bateau pour arriver à l'avant du bateau
        self.Vy = Vy            # Meme chose mais verticalement
        self.degat = 0          # int = Le nombre de fois que le bateau c'est fait toucher
        self.longueur = Vx + 1    # int = Longueur de bateau
        self.safe = True        # bool = True si le bateau est en vie et False s'il est coulé

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = carre * self.x + ecart_width
        self.rect.y = carre * self.y + ecart_height
        self.origin_image = self.image
        self.angle = 0

    def bouger(self, jeu, ecart_width):

        if self.angle == 0 or self.angle == -90:
            self.rect.x = jeu.carre*self.x + ecart_width
            self.rect.y = jeu.carre*self.y + jeu.ecart_height
        else:
            self.rect.x = jeu.carre*(self.x+self.Vx) + ecart_width
            self.rect.y = jeu.carre*(self.y+self.Vy) + jeu.ecart_height

    def tourner(self):
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)

    def damage(self):
        # augmente-les dégâts pris par le bateau de 1
        self.degat += 1

    def get_sens(self):
        # Permet de savoir l'orientation du bateau
        if self.Vx != 0:
            return 'horizontal'
        else:
            return 'vertical'

    def verif_reculer(self, plateau):
        # Permet de bouger le bateau vers l'arrière
        sens = self.get_sens()
        if sens == "horizontal":  # Si le bateau est horizontal
            if self.Vx > 0:  # Si il regarde vers la droite
                if self.x > 0:  # On vérifie que l'arrière de bateau ne se trouve pas sur la dernière case
                    if plateau[self.y][self.x - 1] == 0:  # On vérifie que la case derrière lui n'est pas occupé
                        self.x -= 1  # Puis on recule le bateau
            else:  # Même chose quand le bateau regarde vers la droite
                if self.x < 9:
                    if plateau[self.y][self.x + 1] == 0:
                        self.x += 1

        else:  # Même chose quand le bateau est vertical
            if self.Vy > 0:
                if self.y > 0:
                    if plateau[self.y - 1][self.x] == 0:
                        self.y -= 1
            else:
                if self.y < 9:
                    if plateau[self.y + 1][self.x] == 0:
                        self.y += 1

    def verif_avancer(self, plateau):
        # Permet de bouger le bateau vers l'avant
        # Même principe que pour bouger vers l'arrière
        sens = self.get_sens()
        if sens == "horizontal":
            if self.Vx > 0:
                if self.x + self.Vx < 9:
                    if plateau[self.y][self.x + self.Vx + 1] == 0:
                        self.x += 1
            else:
                if self.x + self.Vx > 0:
                    if plateau[self.y][self.x + self.Vx - 1] == 0:
                        self.x -= 1

        else:
            if self.Vy > 0:
                if self.y + self.Vy < 9:
                    if plateau[self.y + self.Vy + 1][self.x] == 0:
                        self.y += 1
            else:
                if self.y + self.Vy > 0:
                    if plateau[self.y + self.Vy - 1][self.x] == 0:
                        self.y -= 1

    def verif_droite(self, plateau, jeu):
        # Permet de bouger vers l'avant
        sens = self.get_sens()
        if sens == "horizontal":  # Si le bateau est horizontal
            if self.Vx > 0:  # Et qu'il regarde vers la droite
                if self.y + self.Vx <= 9:  # On vérifie que si on prend la colonne du bateau et qu'on y ajoute
                    good = True
                    for y in range(self.y+1, self.y + self.Vx + 1):  # On fait comme si on avait tourné
                        if plateau[y][self.x] != 0:  # Et on regarde si toutes les cases sont libres
                            good = False
                            break
                    if good:
                        self.Vy, self.Vx = self.Vx, 0  # Dans ce cas on échange Vy et Vx
                        self.angle = -90
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)
            else:  # Même principe pour toutes les directions
                if self.y + self.Vx >= 0:
                    good = True
                    for y in range(self.y-1, self.y+self.Vx-1, -1):
                        if plateau[y][self.x] != 0:
                            good = False
                            break
                    if good:
                        self.Vy, self.Vx = self.Vx, 0
                        self.angle = 90
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)

        else:
            if self.Vy < 0:
                if self.x - self.Vy <= 9:
                    good = True
                    for x in range(self.x+1, self.x-self.Vy+1):
                        if plateau[self.y][x] != 0:
                            good = False
                            break
                    if good:
                        self.Vx, self.Vy = -self.Vy, 0
                        self.angle = 0
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)
            else:
                if self.x - self.Vy >= 0:
                    good = True
                    for x in range(self.x-1, self.x-self.Vy-1, -1):
                        if plateau[self.y][x] != 0:
                            good = False
                            break
                    if good:
                        self.Vx, self.Vy = -self.Vy, 0
                        self.angle = 180
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)

    def verif_gauche(self, plateau, jeu):
        # Même principe que pour tourner à droite
        sens = self.get_sens()
        if sens == "horizontal":
            if self.Vx > 0:
                if self.y - self.Vx >= 0:
                    good = True
                    for y in range(self.y - 1, self.y-self.Vx-1, -1):
                        if plateau[y][self.x] != 0:
                            good = False
                            break
                    if good:
                        self.Vy, self.Vx = -self.Vx, 0
                        self.angle = 90
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)
            else:
                if self.y - self.Vx <= 9:
                    good = True
                    for y in range(self.y+1, self.y - self.Vx + 1):
                        if plateau[y][self.x] != 0:
                            good = False
                            break
                    if good:
                        self.Vy, self.Vx = -self.Vx, 0
                        self.angle = -90
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)

        else:
            if self.Vy < 0:
                if self.x + self.Vy >= 0:
                    good = True
                    for x in range(self.x-1, self.x+self.Vy-1, -1):
                        if plateau[self.y][x] != 0:
                            good = False
                            break
                    if good:
                        self.Vx, self.Vy = self.Vy, 0
                        self.angle = 180
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)
            else:
                if self.x + self.Vy <= 9:
                    good = True
                    for x in range(self.x+1, self.x+self.Vy+1):
                        if plateau[self.y][x] != 0:
                            good = False
                            break
                    if good:
                        self.Vx, self.Vy = self.Vy, 0
                        self.angle = 0
                        self.tourner()
                        self.bouger(jeu, jeu.ecart_width)

    def coller(self, plateau):
        # On vérifie que le bateau n'est collé à aucun autre bateau
        sens = self.get_sens()
        if sens == "horizontal":  # Si le bateau est horizontal
            if self.Vx > 0:  # Et regarde vers la droite
                for x in range(self.x, self.x + self.Vx + 1):
                    if self.y > 0:
                        if not plateau[self.y - 1][x] == 0:
                            return True  # On return True si le bateau est collé avec un autre bateau
                    if self.y < 9:
                        if not plateau[self.y + 1][x] == 0:
                            return True
                if self.x + self.Vx < 9:
                    if not plateau[self.y][self.x + self.Vx + 1] == 0:
                        return True
                    if self.y > 0:
                        if not plateau[self.y - 1][self.x + self.Vx + 1] == 0:
                            return True
                    if self.y < 9:
                        if not plateau[self.y + 1][self.x + self.Vx + 1] == 0:
                            return True
                if self.x > 0:
                    if not plateau[self.y][self.x - 1] == 0:
                        return True
                    if self.y > 0:
                        if not plateau[self.y - 1][self.x - 1] == 0:
                            return True
                    if self.y < 9:
                        if not plateau[self.y + 1][self.x - 1] == 0:
                            return True

            else:
                for x in range(self.x, self.x + self.Vx - 1, -1):
                    if self.y > 0:
                        if not plateau[self.y - 1][x] == 0:
                            return True
                    if self.y < 9:
                        if not plateau[self.y + 1][x] == 0:
                            return True
                if self.x < 9:
                    if not plateau[self.y][self.x + 1] == 0:
                        return True
                    if self.y > 0:
                        if not plateau[self.y - 1][self.x + 1] == 0:
                            return True
                    if self.y < 9:
                        if not plateau[self.y + 1][self.x + 1] == 0:
                            return True
                if self.x + self.Vx > 0:
                    if not plateau[self.y][self.x + self.Vx - 1] == 0:
                        return True
                    if self.y > 0:
                        if not plateau[self.y - 1][self.x + self.Vx - 1] == 0:
                            return True
                    if self.y < 9:
                        if not plateau[self.y + 1][self.x + self.Vx - 1] == 0:
                            return True

        else:
            if self.Vy > 0:
                for y in range(self.y, self.y + self.Vy + 1):
                    if self.x > 0:
                        if not plateau[y][self.x - 1] == 0:
                            return True
                    if self.x < 9:
                        if not plateau[y][self.x + 1] == 0:
                            return True
                if self.y + self.Vy < 9:
                    if not plateau[self.y + self.Vy + 1][self.x] == 0:
                        return True
                    if self.x > 0:
                        if not plateau[self.y + self.Vy + 1][self.x - 1] == 0:
                            return True
                    if self.x < 9:
                        if not plateau[self.y + self.Vy + 1][self.x + 1] == 0:
                            return True
                if self.y > 0:
                    if not plateau[self.y - 1][self.x] == 0:
                        return True
                    if self.x > 0:
                        if not plateau[self.y - 1][self.x - 1] == 0:
                            return True
                    if self.x < 9:
                        if not plateau[self.y - 1][self.x + 1] == 0:
                            return True
            else:
                for y in range(self.y, self.y + self.Vy - 1, -1):
                    if self.x > 0:
                        if not plateau[y][self.x - 1] == 0:
                            return True
                    if self.x < 9:
                        if not plateau[y][self.x + 1] == 0:
                            return True
                if self.y < 9:
                    if not plateau[self.y + 1][self.x] == 0:
                        return True
                    if self.x > 0:
                        if not plateau[self.y + 1][self.x - 1] == 0:
                            return True
                    if self.x < 9:
                        if not plateau[self.y + 1][self.x + 1] == 0:
                            return True
                if self.y + self.Vy > 0:
                    if not plateau[self.y + self.Vy - 1][self.x] == 0:
                        return True
                    if self.x > 0:
                        if not plateau[self.y + self.Vy - 1][self.x - 1] == 0:
                            return True
                    if self.x < 9:
                        if not plateau[self.y + self.Vy - 1][self.x + 1] == 0:
                            return True
        return False  # Si le bateau n'est collé avec aucun bateau on return False
