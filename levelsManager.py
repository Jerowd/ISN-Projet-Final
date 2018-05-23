from settings import *
import sprites



class Scene():
    currentLevel = 0
        
    #fonctions qui spawn les murs de base
    def SpawnDefaultWalls(self):
        self.grounds = [(0,0,WIDTH, 30),
                        (0, HEIGHT-30, WIDTH, 30),
                        (0, 0, 30, HEIGHT),
                        [WIDTH - 30,0,30,HEIGHT]]
        
        for g in self.grounds:
                self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
                self.all_sprites.add(self.ground)
                self.platforms_sprite.add(self.ground)
 
        


class Lvl0:
    def start(self):
        self.grounds = [(2*WIDTH/3,2*HEIGHT/3,2*WIDTH/3,HEIGHT/3)]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)


        





class Lvl1:
    def start(self):
        #sols
        self.grounds = [(0,HEIGHT-100,WIDTH-150, 100, self),
                        (0, HEIGHT-140, 200, 40, self),
                        (300, HEIGHT-350, 300, 40, self),
                        (700, HEIGHT - 540, 300 , 40, self)
                         ]

        for g in self.grounds:
            self.ground = sprites.Ground(g[0], g[1], g[2], g[3], self)
            self.all_sprites.add(self.ground)
            self.platforms_sprite.add(self.ground)



        #pieges
        self.piegesTombent = [(WIDTH - 250, -20, 50,50, HEIGHT-150, self),
                               (WIDTH - 350, -20, 50,50, HEIGHT-150, self)]

        for p in self.piegesTombent:
            self.piege = sprites.Falling_traps(p[0], p[1], p[2], p[3], p[4], self)
            self.all_sprites.add(self.piege)
            self.platforms_sprite.add(self.piege)


        #porte
        self.porte = sprites.Porte(720,HEIGHT-640,self)
        self.all_sprites.add(self.porte)

