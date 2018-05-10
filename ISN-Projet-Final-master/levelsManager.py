from settings import *
import sprites

class Scene():
    currentLevel = 0

    #fonctions qui spawn les murs de base
    def SpawnDefaultWalls(self):
        self.grounds = [(0,0,1280, 30),
                        (0, 690, 1280, 30),
                        (0, 0, 30, 720),
                        [1250,0,30,720]]

        for g in self.grounds:
                self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
                self.all_sprites.add(self.ground)
                self.platforms_sprite.add(self.ground)

class Lvl0:
    def start(self):
        self.grounds = [(855,480,855,240)]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.porte = sprites.Porte(1255, 260,self)
        self.all_sprites.add(self.porte)

        self.lasers = [(40, 580, 50, 5, self)]

        for l in self.lasers:
            self.laser = sprites.Laser_horiz(l[0], l[1], l[2], l[3], self)
            self.all_sprites.add(self.laser)

class Lvl1:
    def start(self):
        #sols
        self.grounds = [(0,620,1130, 100, self),
                        (0, 580, 200, 40, self),
                        (300, 370, 300, 40, self),
                        (700, 180, 300 , 40, self)
                         ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        #pieges
        self.piegesTombent = [(1030, -20, 50,50, 570, self),
                               (930, -20, 50,50, 570, self)]

        for p in self.piegesTombent:
            self.piege = sprites.Falling_traps(p[0], p[1], p[2], p[3], p[4], self)
            self.all_sprites.add(self.piege)
            self.platforms_sprite.add(self.piege)

        #porte
        self.porte = sprites.Porte(720,80,self)
        self.all_sprites.add(self.porte)
