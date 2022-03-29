import pygame
from Placement import recommencer


class Game:

    def __init__(self, width, height, taille, fps):
        self.width = width
        self.height = height
        self.taille = taille
        self.FPS = fps
        self.win = None

        self.debut = True
        self.placement = False
        self.tir = False
        self.running = True
        self.changement = False

        self.ecart_width = (width - taille) // 2
        self.ecart_height = (height - taille) // 2
        self.carre = taille // 10
        rate = pygame.image.load("image/rate.png")
        touche = pygame.image.load("image/explosion.png")
        lancement = pygame.image.load("image/lancement.png")
        placement = pygame.image.load("image/placement.png")
        tir = pygame.image.load("image/tir.png")
        fin = pygame.image.load("image/fin.png")

        self.images = [rate, touche, lancement, placement, tir, fin]

        self.joueur1 = {"boat": 0, "tour": True}
        self.joueur2 = {"boat": 0, "tour": False}
        self.gagnant = False
        self.perdant = False

    def init_valeur(self, armee1, armee2, plateau1, plateau2, win):
        self.joueur1["armee"] = armee1
        self.joueur2["armee"] = armee2
        self.joueur1["plateau"] = plateau1
        self.joueur2["plateau"] = plateau2
        self.win = win

    def changer_phase(self):
        self.placement = False
        self.tir = True

        ecart_w_gauche = (self.width - self.taille * 2) // 3
        ecart_w_droit = self.width - self.taille - ((self.width - self.taille * 2) // 3)
        self.ecart_width = (ecart_w_gauche, ecart_w_droit)

    def changer_tour(self):
        pygame.time.delay(1000)
        self.changement = False

        self.joueur1["tour"], self.joueur2["tour"] = self.joueur2["tour"], self.joueur1["tour"]

    def background(self):
        if self.debut:
            self.win.blit(self.images[2], (0, 0))
        elif self.placement:
            self.win.blit(self.images[3], (0, 0))
        elif self.tir:
            self.win.blit(self.images[4], (0, 0))
        else:
            self.win.blit(self.images[5], (0, 0))

    def debuter(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.debut = False
                    self.placement = True

    def finir(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ecart_width = (self.width - self.taille) // 2
                    self.debut = True
                    self.joueur1["armee"], self.joueur1["plateau"], self.joueur2["armee"], self.joueur2["plateau"] = recommencer(self)
                    self.joueur1["boat"] = 0
                    self.joueur2["boat"] = 0
                    self.joueur1["tour"] = True

    def victoire(self, gagnant, perdant):
        self.tir = False
        self.joueur1["tour"] = False
        self.joueur2["tour"] = False

        self.gagnant = gagnant
        self.perdant = perdant
