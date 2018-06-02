from settings import *
import sprites
vec = pg.math.Vector2

class Scene():
    currentLevel = 1

    #fonctions qui spawn les murs de base
    def SpawnDefaultWalls(self):
        self.grounds = [(0,0,1280, 30),
                        (0, 690, 1280, 30),
                        (0, 0, 30, 720),
                        (1250,0,30,720)]

        for g in self.grounds:
                self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
                self.all_sprites.add(self.ground)
                self.platforms_sprite.add(self.ground)

class Lvl1:
    def start(self):

        self.player.rect.center = (75, 675)
        self.player.pos = vec(75, 675)

        if not "lvl1" in niv_atteints:
            niv_atteints.append("lvl1")

        self.grounds = [(200,660,80,40),
                        (350, 600, 200, 100),
                        (640, 520, 620, 180),
                        (700, 415, 100, 12),
                        (450, 360, 160, 12),
                        (320, 290, 80, 12),
                        (480, 220, 80, 12),
                        (640, 170, 160, 12),
                        (850, 170, 100, 12),
                        (910, 350, 30, 12),
                        (1040, 240, 220, 12),
                        (1080, 210, 180, 30)
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.porte = sprites.Porte(1200, 110, self)
        self.all_sprites.add(self.porte)

class Lvl2:
    def start(self):

        if not "lvl2" in niv_atteints:
            niv_atteints.append("lvl2")

        self.player.rect.center = (40, 120)
        self.player.pos = vec(40, 120)

        #sols la width des deux petits sols étaient de 12 avant
        self.grounds = [(880,360,60, 360, self),
                        (880, 30, 60, 220, self),
                        (30, 160, 140, 30, self),
                        (375, 375, 140, 30, self),
                        (650, 250, 100, 30, self)
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.spikes = [(130,660, 250, 60, self),
                       (380, 660, 250, 60, self),
                       (630, 660, 250, 60, self)
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)

         #porte
        self.porte = sprites.Porte(1200,590,self)
        self.all_sprites.add(self.porte)

class Lvl3:
    def start(self):

        if not "lvl3" in niv_atteints:
            niv_atteints.append("lvl3")

        self.player.rect.center = (40, 640)
        self.player.pos = vec(40, 640)

        self.grounds = [(160,640, 30, 70, self),
                        (280, 640, 240, 50, self),
                        (320, 600, 200, 40, self),
                        (360, 560, 160 , 40, self)
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)


        #Falling Traps
        self.falling_traps_l = [(190, -110, 90, 150, 540, self),
                                (430, -110, 90, 150, 410, self),
                                (520, -110, 90, 150, 540, self),
                                (710, -110, 90, 150, 540, self),
                                (800, -110, 90, 150, 540, self),
                                (890, -110, 90, 150, 540, self)
                                ]

        for f in self.falling_traps_l:
            self.falling_traps = sprites.Falling_traps(f[0], f[1], f[2], f[3], f[4] ,self)
            self.all_sprites.add(self.falling_traps)
            self.platforms_sprite.add(self.falling_traps)

        #porte
        self.porte = sprites.Porte(1200,590,self)
        self.all_sprites.add(self.porte)

class Lvl4:
    def start(self):

        if not "lvl4" in niv_atteints:
            niv_atteints.append("lvl4")

        self.player.rect.center = (1200, 150)
        self.player.pos = vec(1200, 150)

        self.grounds = [(30,160,90, 550, self),
                        (540, 160, 120, 550, self),
                        (1110, 230, 150, 550, self),
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.button_1 = sprites.Button(1110, 210, 40, 20, "button_1", False, self)
        self.all_sprites.add(self.button_1)
        self.platforms_sprite.add(self.button_1)

        self.button_2 = sprites.Button(980, 670, 40, 20, "button_2", False, self)
        self.all_sprites.add(self.button_2)
        self.platforms_sprite.add(self.button_2)

        self.porte = sprites.Porte(40, 60, self)
        self.all_sprites.add(self.porte)

class Lvl5:
    def start(self):

        self.move = False
        if not "lvl5" in niv_atteints:
            niv_atteints.append("lvl5")

        self.player.rect.center = (1230, 100)
        self.player.pos = vec(1230, 100)

        self.grounds = [(1200, 130, 75, 20, self),
                        (740, 130, 75, 20, self),
                        (900, 130, 75, 20, self),
                        (450, 380, 75, 20, self),
                        (500, 550, 75, 20, self),
                        (270, 300, 75, 20, self),
                        (950, 130, 55, 560, self),
                        (625, 465, 75, 20, self),
                        (30, 200, 75, 20, self),
                        (400, 250, 75, 20, self),
                        (280, 600, 20, 90, self),
                        (400, 600, 20, 90, self),
                        (150, 250, 20, 440, self)
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], g[4])
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.spikes = [(420 ,660, 250, 60, self),
                       (670, 660, 250, 60, self)
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)

        self.wall_button_1 = sprites.Ground(815, 30, 85, 120,self)
        self.all_sprites.add(self.wall_button_1)
        self.platforms_sprite.add(self.wall_button_1)

        self.wall_button_2 = sprites.Ground(665, 30, 85, 120,self)
        self.all_sprites.add(self.wall_button_2)
        self.platforms_sprite.add(self.wall_button_2)

        self.wall_button_3 = sprites.Ground(300, 600, 120, 20, self)
        self.all_sprites.add(self.wall_button_3)
        self.platforms_sprite.add(self.wall_button_3)

        self.wall_button_4 = sprites.Ground(30, 250, 120, 20, self)
        self.all_sprites.add(self.wall_button_4)
        self.platforms_sprite.add(self.wall_button_4)

        self.buttons = [(900, 110, 40, 20, "button_3", True, self),
                        (1210, 670, 40, 20, "button_4", True, self),
                        (30, 180, 40, 20, "button_5", True, self),
                        (330, 670, 40, 20, "button_6", True, self)
                        ]

        for b in self.buttons:
            self.button = sprites.Button(b[0], b[1], b[2], b[3], b[4], b[5], self)
            self.all_sprites.add(self.button)
            self.platforms_sprite.add(self.button)

        self.porte = sprites.Porte(40, 590,self)
        self.all_sprites.add(self.porte)

class Lvl6:
    def start(self):

        if not "lvl6" in niv_atteints:
            niv_atteints.append("lvl6")

        #position du joueur
        self.player.rect.center = (1210, 640)
        self.player.pos = vec(1210, 640)

        #sols
        self.grounds = [(30,30, 120, 160, self),
                        (70 , 270, 80, 320, self),
                        (260, 270, 40, 420, self),
                        (460, 270, 40, 200, self),
                        (460, 550, 40, 200, self),
                        (510, 30, 40, 180, self),
                        (750, 150, 40, 550, self),
                        (970, 150, 40, 470, self),
                        (300, 370, 40, 20, self),
                        (300, 530, 40, 20, self),
                        (420, 450, 40, 20, self),
                        (420, 630, 40, 20, self),
                        (420, 270, 40, 20, self),
                        (790, 250, 40, 20, self),
                        (790, 370, 40, 20, self),
                        (790, 510, 40, 20, self),
                        (790, 670, 40, 20, self),
                        (930, 270, 40, 20, self),
                        (930, 430, 40, 20, self),
                        (930, 600, 40, 20, self),
                        (550, 190, 40, 20, self)
                        ]

        self.wall_button_5 = sprites.Ground(30, 270, 40, 320, self)
        self.all_sprites.add(self.wall_button_5)
        self.platforms_sprite.add(self.wall_button_5)

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.falling_traps_l = [(150,-180, 90, 150, 540 , self),
                                (1050, -180, 90, 150, 540, self)]

        for f in self.falling_traps_l:
            self.falling_traps = sprites.Falling_traps(f[0], f[1], f[2], f[3], f[4] ,self)
            self.all_sprites.add(self.falling_traps)
            self.platforms_sprite.add(self.falling_traps)

        self.spikes = [(500 , 660, 250, 60, self),
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)

        #buttons
        self.buttons = [(90, 250 , 40, 20, "button_8", False, self)
                        ]

        for b in self.buttons:
            self.button = sprites.Button(b[0], b[1], b[2], b[3], b[4], b[5], self)
            self.all_sprites.add(self.button)
            self.platforms_sprite.add(self.button)

        self.button_7 = sprites.Button(550, 170, 40, 20, "button_7", False, self)
        self.all_sprites.add(self.button_7)
        self.platforms_sprite.add(self.button_7)

        self.porte = sprites.Porte(40, 590,self)
        self.all_sprites.add(self.porte)
