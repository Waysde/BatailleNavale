import pygame
from Placement import recommencer


class Game:

    def __init__(self, width, fps):
        self.width = width
        self.height = (width * 9)//16
        self.taille = (width * 25)//64
        self.FPS = fps
        self.win = None

        self.debut = True
        self.placement = False
        self.tir = False
        self.running = True
        self.changement = False

        self.ecart_width = (width - self.taille) // 2
        self.ecart_height = (self.height - self.taille) // 2
        self.carre = self.taille // 10

        self.images = []

        self.joueur1 = {"boat": 0, "tour": True}
        self.joueur2 = {"boat": 0, "tour": False}
        self.gagnant = False
        self.perdant = False

    def image(self):
        rate = pygame.transform.scale(pygame.image.load("image/rate.png"), (self.carre, self.carre))
        touche = pygame.transform.scale(pygame.image.load("image/explosion.png"), (self.carre, self.carre))
        lancement = pygame.transform.scale(pygame.image.load("image/lancement.png"), (self.width, self.height))
        placement = pygame.transform.scale(pygame.image.load("image/placement.png"), (self.width, self.height))
        tir = pygame.transform.scale(pygame.image.load("image/tir.png"), (self.width, self.height))
        fin = pygame.transform.scale(pygame.image.load("image/fin.png"), (self.width, self.height))
        b5 = pygame.transform.scale(pygame.image.load("image/5 cases.png"), (5*self.carre, self.carre))
        b4 = pygame.transform.scale(pygame.image.load("image/4 cases.png"), (4*self.carre, self.carre))
        b3 = pygame.transform.scale(pygame.image.load("image/3 cases.png"), (3*self.carre, self.carre))
        b2 = pygame.transform.scale(pygame.image.load("image/2 cases.png"), (2*self.carre, self.carre))
        b5coule = pygame.transform.scale(pygame.image.load("image/5 casesCoule.png"), (5*self.carre, self.carre))
        b4coule = pygame.transform.scale(pygame.image.load("image/4 casesCoule.png"), (4*self.carre, self.carre))
        b3coule = pygame.transform.scale(pygame.image.load("image/3 casesCoule.png"), (3*self.carre, self.carre))
        b2coule = pygame.transform.scale(pygame.image.load("image/2 casesCoule.png"), (2*self.carre, self.carre))

        self.images = [rate, touche, b2coule, b3coule, b4coule, b5coule, lancement, placement, tir, fin, b2, b3, b4, b5]

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
            self.win.blit(self.images[6], (0, 0))
        elif self.placement:
            self.win.blit(self.images[7], (0, 0))
        elif self.tir:
            self.win.blit(self.images[8], (0, 0))
        else:
            self.win.blit(self.images[9], (0, 0))

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
