from settings import *
import sprites

vec = pg.math.Vector2

class Scene():
    currentLevel = 4

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

class Lvl0:
    def start(self):


        if not "lvl0" in niv_atteints:
            niv_atteints.append("lvl0")

        print(niv_atteints)

        self.player.rect.center = (20,20)


        self.grounds = [(110,660,160,40),
                        (400, 600, 160, 100),
                        (640, 520, 620, 180),
                        (640, 415, 40, 12),
                        (760, 415, 40, 12),
                        (400, 360, 160, 12),
                        (320, 290, 80, 12),
                        (480, 220, 80, 12),
                        (640, 170, 160, 12),
                        (880, 120, 80, 12),
                        (950, 120, 80, 12),
                        (1130, 120, 160, 12),
                        (910, 320, 15, 12),
                        (1040, 240, 220, 12),
                        (1080, 210, 180, 30)]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.porte = sprites.Porte(1200, 20,self)
        self.all_sprites.add(self.porte)

class Lvl1:
    def start(self):
        print(niv_atteints)

        if not "lvl1" in niv_atteints:
            niv_atteints.append("lvl1")

        self.player.rect.center = (20, 300)

        #sols
        self.grounds = [(880,360,60, 360, self),
                        (880, 20, 60, 220, self),
                        (20, 160, 140, 12, self),
                        (480, 160, 140 , 12, self),
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.spikes = [(20,660,250, 60, self),
                       (370, 660, 250, 60, self),
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)

         #porte
        self.porte = sprites.Porte(1200,620,self)
        self.all_sprites.add(self.porte)

class Lvl2:
    def start(self):

        if not "lvl2" in niv_atteints:
            niv_atteints.append("lvl2")

        print(niv_atteints)

        #position du joueur
        self.player.rect.center = (20, 680)

        #sols
        self.grounds = [(160,640,30, 70, self),
                        (280, 640, 30, 70, self),
                        (310, 600, 50, 110, self),
                        (360, 560, 40 , 150, self),
                        (400, 520, 120, 190, self)
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)


        #Falling Traps
        self.falling_traps_l = [(190,-110,90, 150,560, self),
                                (430, -110, 90, 150, 370, self),
                                (520, -110, 90, 150, 560, self),
                                (800, -410, 270, 450, 250, self)
                                ]

        for f in self.falling_traps_l:
            self.falling_traps = sprites.Falling_traps(f[0], f[1], f[2], f[3], f[4] ,self)
            self.all_sprites.add(self.falling_traps)
            self.platforms_sprite.add(self.falling_traps)

        self.spikes = [(630,690,55, 20, self)
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)


                #porte
        self.porte = sprites.Porte(1200,620,self)
        self.all_sprites.add(self.porte)


class Lvl3:
    def start(self):

        if not "lvl3" in niv_atteints:
            niv_atteints.append("lvl3")

        print(niv_atteints)

        #position du joueur
        self.player.rect.center = (20, 680)

        #sols
        self.grounds = [(20,160,90, 550, self),
                        (540, 160, 120, 550, self),
                        (1110, 160, 150, 550, self),
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)


        #buttons
        self.buttons = [(1110, 150, 40, 10, "button_1", False, self),
                        (980, 680, 40, 10, "button_2", False, self)
                        ]

        for b in self.buttons:
            self.button = sprites.Button(b[0], b[1], b[2], b[3], b[4], b[5], self)
            self.all_sprites.add(self.button)
            self.platforms_sprite.add(self.button)

        self.porte = sprites.Porte(1200, 30,self)
        self.all_sprites.add(self.porte)


        print(niv_atteints)

class Lvl4:
    def start(self):

        self.move = False
        if not "lvl4" in niv_atteints:
            niv_atteints.append("lvl4")

        print(niv_atteints)

        #position du joueur
        self.player.rect.center = (1230, 100)

        #sols
        self.grounds = [(950, 480, 125, 250, self),
                        (1200, 130, 75, 20, self),
                        (950, 480, 125, 250, self),
                        (740, 130, 75, 20, self),
                        (900, 130, 75, 20, self),
                        (150, 160, 75, 20, self),
                        (600, 160, 75, 20, self),
                        (500, 380, 75, 20, self),
                        (500, 550, 75, 20, self),
                        (270, 300, 75, 20, self),
                        (950, 130, 55, 380, self),
                        (625, 465, 75, 20, self),
                        (30, 100, 75, 20, self),
                        (400, 250, 75, 20, self),
                        (280, 600, 20, 90, self),
                        (400, 600, 20, 90, self),
                        (150, 250, 20, 440, self)
                        ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], g[4])
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

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
        #pièges
        self.falling_traps_l = [(1075,-110,90, 150, 540 , self)
                                ]

        for f in self.falling_traps_l:
            self.falling_traps = sprites.Falling_traps(f[0], f[1], f[2], f[3], f[4] ,self)
            self.all_sprites.add(self.falling_traps)
            self.platforms_sprite.add(self.falling_traps)

        self.spikes = [(750 ,670, 200, 20, self),
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)



                    #buttons
        self.buttons = [(900, 120, 40, 10, "button_3", True, self),
                        (1210, 680, 40, 10, "button_4", True, self),
                        (30, 90, 40, 10, "button_5", True, self),
                        (330, 680, 40, 10, "button_6", True, self)
                        ]

        for b in self.buttons:
            self.button = sprites.Button(b[0], b[1], b[2], b[3], b[4], b[5], self)
            self.all_sprites.add(self.button)
            self.platforms_sprite.add(self.button)

class Lvl5:
    def start(self):

        if not "lvl5" in niv_atteints:
            niv_atteints.append("lvl5")



        #position du joueur
        self.player.pos = vec(20, 680)

        #sols
        self.grounds = [(30,30, 120, 160, self),
                        (70 , 270, 80, 320, self),
                        (270, 270, 40, 420, self),
                        (390, 270, 40, 200, self),
                        (390, 550, 40, 200, self),
                        (510, 30, 40, 180, self),
                        (750, 150, 40, 550, self),
                        (910, 150, 40, 470, self),
                        (310, 370, 20, 20, self),
                        (310, 530, 20, 20, self),
                        (370, 450, 20, 20, self),
                        (370, 630, 20, 20, self),
                        (370, 270, 20, 20, self),
                        (790, 250, 20, 20, self),
                        (790, 370, 20, 20, self),
                        (790, 510, 20, 20, self),
                        (790, 670, 20, 20, self),
                        (890, 270, 40, 20, self),
                        (890, 430, 40, 20, self),
                        (890, 600, 40, 20, self),]

        self.wall_button_5 = sprites.Ground(30, 270, 40, 320, self)
        self.all_sprites.add(self.wall_button_5)
        self.platforms_sprite.add(self.wall_button_5)

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)

        self.falling_traps_l = [(150,-180, 120, 200, 490 , self),
                                (1000, -180, 120, 200, 490, self)]

        for f in self.falling_traps_l:
            self.falling_traps = sprites.Falling_traps(f[0], f[1], f[2], f[3], f[4] ,self)
            self.all_sprites.add(self.falling_traps)
            self.platforms_sprite.add(self.falling_traps)

        self.spikes = [(510 , 670, 240, 20, self),
                       ]

        for s in self.spikes:
            self.spike = sprites.Spikes(s[0], s[1], s[2], s[3], self)
            self.all_sprites.add(self.spike)
            self.platforms_sprite.add(self.spike)

        #buttons
        self.buttons = [(550, 70, 20, 40, "button_7", False, self),
                        (90, 250 , 40, 20, "button_8", False, self)
                        ]

        for b in self.buttons:
            self.button = sprites.Button(b[0], b[1], b[2], b[3], b[4], b[5], self)
            self.all_sprites.add(self.button)
            self.platforms_sprite.add(self.button)



