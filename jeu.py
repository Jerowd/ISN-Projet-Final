import pygame as pg
import sys
import random
from settings import *
from player import *
from sprites import *
from levelsManager import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.running = True

        #INITIALISATION DES NIVEAUX
        self.scene = Scene
        self.lvl0 = Lvl0
        self.lvl1 = Lvl1


    def spawnObjects(self):
        #crÃƒÂ©ation des groupes de sprites
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.platforms_sprite = pg.sprite.Group()

        if self.scene.currentLevel == 0:
            self.lvl0.start(self)
        else:
            self.lvl1.start(self)

        #crÃƒÂ©ation du joueur
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.player_sprite.add(self.player)

        #collision joueur
        self.player_col = Player_collision(self)
        self.all_sprites.add(self.player_col)
        self.head_col = Head_collision(self)
        self.all_sprites.add(self.head_col)

        #crÃƒÂ©ation de la tÃƒÂªte
        self.head = Head(self)
        self.all_sprites.add(self.head)
        self.player_sprite.add(self.head)


    def new(self):
        self.spawnObjects()
        self.scene.SpawnDefaultWalls(self)
        self.run()


    def run(self):
        self.playing = True

        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            self.lateUpdate()

    def lateUpdate(self):
        self.head.pos = self.head.rect.midbottom
        self.player.pos = self.player.rect.midbottom

    def update(self):
        self.all_sprites.update()

        self.debug()
        
        #HEAD
        #player teleportation to head
        keys = pg.key.get_pressed()

        #tir
        if keys[pg.K_e] and self.head.isOn and self.head.press:
            self.head.isOn = False
            self.head.mouse_loc()
            self.head.press = False

        #teleportation du corps sur la tete
        elif keys[pg.K_q] and self.head.isOn == False and self.head.press:
            self.teleport()
            self.head.press = False

        if self.head.isOn:
            self.on()
            self.head.image.fill(RED)
        else:
            self.head.notOn()   
            self.head.image.fill(RED)

        self.head.pressWait()

        #tete sur le corps si isnotOn
    def on(self):
        self.head.rect.midbottom = self.player.rect.midtop
        self.head.pos = self.head.rect.midbottom


    def teleport(self):
        self.player.rect = self.head.rect 
        self.player.rect.y -= 100
        self.player.pos = self.player.rect.midbottom
        self.head.isOn = True


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False

                self.running = False
                pg.quit()
                sys.exit()


    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def debug(self):
        """
        print(self.head.rect)
        print(self.head.pos)
        print(" ")
        """
        print(self.player.vel)

gameInstance = Game()
while gameInstance.running:
    gameInstance.new()
