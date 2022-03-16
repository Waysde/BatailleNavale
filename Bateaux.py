class Bateau:

    def __init__(self, x, y, Vx, Vy):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.degat = 0
        self.longueur = Vx+1
        self.etat = "safe"

    def damage(self):
        self.degat += 1

    def get_sens(self):
        if self.Vx != 0:
            return 'horizontal'
        else:
            return 'vertical'

    def move_backward(self, plateau):
        sens = self.get_sens()
        if sens == "horizontal":
            if self.Vx > 0:
                if self.x > 0:
                    if plateau[self.y][self.x - 1] == 0:
                        self.x -= 1
            else:
                if self.x < 9:
                    if plateau[self.y][self.x + 1] == 0:
                        self.x += 1

        else:
            if self.Vy > 0:
                if self.y > 0:
                    if plateau[self.y - 1][self.x] == 0:
                        self.y -= 1
            else:
                if self.y < 9:
                    if plateau[self.y + 1][self.x] == 0:
                        self.y += 1

    def move_forward(self, plateau):
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

    def turn_right(self, plateau):
        sens = self.get_sens()
        if sens == "horizontal":
            if self.Vx > 0:
                if self.y + self.Vx <= 9:
                    good = True
                    for y in range(self.y+1, self.y + self.Vx + 1):
                        if plateau[y][self.x] != 0:
                            good = False
                    if good:
                        self.Vy, self.Vx = self.Vx, 0
            else:
                if self.y + self.Vx >= 0:
                    good = True
                    for y in range(self.y-1, self.y+self.Vx-1, -1):
                        if plateau[y][self.x] != 0:
                            good = False
                    if good:
                        self.Vy, self.Vx = self.Vx, 0

        else:
            if self.Vy < 0:
                if self.x - self.Vy <= 9:
                    good = True
                    for x in range(self.x+1, self.x-self.Vy+1):
                        if plateau[self.y][x] != 0:
                            good = False
                    if good:
                        self.Vx, self.Vy = -self.Vy, 0
            else:
                if self.x - self.Vy >= 0:
                    good = True
                    for x in range(self.x-1, self.x-self.Vy-1, -1):
                        if plateau[self.y][x] != 0:
                            good = False
                    if good:
                        self.Vx, self.Vy = -self.Vy, 0

    def turn_left(self, plateau):
        sens = self.get_sens()
        if sens == "horizontal":
            if self.Vx > 0:
                if self.y - self.Vx >= 0:
                    good = True
                    for y in range(self.y - 1, self.y-self.Vx-1, -1):
                        if plateau[y][self.x] != 0:
                            good = False
                    if good:
                        self.Vy, self.Vx = -self.Vx, 0
            else:
                if self.y - self.Vx <= 9:
                    good = True
                    for y in range(self.y+1, self.y - self.Vx + 1):
                        if plateau[y][self.x] != 0:
                            good = False
                    if good:
                        self.Vy, self.Vx = -self.Vx, 0

        else:
            if self.Vy < 0:
                if self.x + self.Vy >= 0:
                    good = True
                    for x in range(self.x-1, self.x+self.Vy-1, -1):
                        if plateau[self.y][x] != 0:
                            good = False
                    if good:
                        self.Vx, self.Vy = self.Vy, 0
            else:
                if self.x + self.Vy <= 9:
                    good = True
                    for x in range(self.x+1, self.x+self.Vy+1):
                        if plateau[self.y][x] != 0:
                            good = False
                    if good:
                        self.Vx, self.Vy = self.Vy, 0

    def coller(self, plateau):
        contact = 0
        if self.Vx != 0:
            if self.Vx > 0:
                for x in range(self.x, self.x + self.Vx + 1):
                    if self.y > 0:
                        if 1 <= plateau[self.y - 1][x] < 2:
                            contact += 1
                    if self.y < 9:
                        if 1 <= plateau[self.y + 1][x] < 2:
                            contact += 1
                if self.x + self.Vx < 9:
                    if 1 <= plateau[self.y][self.x + self.Vx + 1] < 2:
                        contact += 1
                    if self.y > 0:
                        if 1 <= plateau[self.y - 1][self.x + self.Vx + 1] < 2:
                            contact += 1
                    if self.y < 9:
                        if 1 <= plateau[self.y + 1][self.x + self.Vx + 1] < 2:
                            contact += 1
                if self.x > 0:
                    if 1 <= plateau[self.y][self.x - 1] < 2:
                        contact += 1
                    if self.y > 0:
                        if 1 <= plateau[self.y - 1][self.x - 1] < 2:
                            contact += 1
                    if self.y < 9:
                        if 1 <= plateau[self.y + 1][self.x - 1] < 2:
                            contact += 1

            else:
                for x in range(self.x, self.x + self.Vx - 1, -1):
                    if self.y > 0:
                        if 1 <= plateau[self.y - 1][x] < 2:
                            contact += 1
                    if self.y < 9:
                        if 1 <= plateau[self.y + 1][x] < 2:
                            contact += 1
                if self.x < 9:
                    if 1 <= plateau[self.y][self.x + 1] < 2:
                        contact += 1
                    if self.y > 0:
                        if 1 <= plateau[self.y - 1][self.x + 1] < 2:
                            contact += 1
                    if self.y < 9:
                        if 1 <= plateau[self.y + 1][self.x + 1] < 2:
                            contact += 1
                if self.x + self.Vx > 0:
                    if 1 <= plateau[self.y][self.x + self.Vx - 1] < 2:
                        contact += 1
                    if self.y > 0:
                        if 1 <= plateau[self.y - 1][self.x + self.Vx - 1] < 2:
                            contact += 1
                    if self.y < 9:
                        if 1 <= plateau[self.y + 1][self.x + self.Vx - 1] < 2:
                            contact += 1

        else:
            if self.Vy > 0:
                for y in range(self.y, self.y + self.Vy + 1):
                    if self.x > 0:
                        if 1 <= plateau[y][self.x - 1] < 2:
                            contact += 1
                    if self.x < 9:
                        if 1 <= plateau[y][self.x + 1] < 2:
                            contact += 1
                if self.y + self.Vy < 9:
                    if 1 <= plateau[self.y + self.Vy + 1][self.x] < 2:
                        contact += 1
                    if self.x > 0:
                        if 1 <= plateau[self.y + self.Vy + 1][self.x - 1] < 2:
                            contact += 1
                    if self.x < 9:
                        if 1 <= plateau[self.y + self.Vy + 1][self.x + 1] < 2:
                            contact += 1
                if self.y > 0:
                    if 1 <= plateau[self.y - 1][self.x] < 2:
                        contact += 1
                    if self.x > 0:
                        if 1 <= plateau[self.y - 1][self.x - 1] < 2:
                            contact += 1
                    if self.x < 9:
                        if 1 <= plateau[self.y - 1][self.x + 1] < 2:
                            contact += 1
            else:
                for y in range(self.y, self.y + self.Vy - 1, -1):
                    if self.x > 0:
                        if 1 <= plateau[y][self.x - 1] < 2:
                            contact += 1
                    if self.x < 9:
                        if 1 <= plateau[y][self.x + 1] < 2:
                            contact += 1
                if self.y < 9:
                    if 1 <= plateau[self.y + 1][self.x] < 2:
                        contact += 1
                    if self.x > 0:
                        if 1 <= plateau[self.y + 1][self.x - 1] < 2:
                            contact += 1
                    if self.x < 9:
                        if 1 <= plateau[self.y + 1][self.x + 1] < 2:
                            contact += 1
                if self.y + self.Vy > 0:
                    if 1 <= plateau[self.y + self.Vy - 1][self.x] < 2:
                        contact += 1
                    if self.x > 0:
                        if 1 <= plateau[self.y + self.Vy - 1][self.x - 1] < 2:
                            contact += 1
                    if self.x < 9:
                        if 1 <= plateau[self.y + self.Vy - 1][self.x + 1] < 2:
                            contact += 1
        return contact
