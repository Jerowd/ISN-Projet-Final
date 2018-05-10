import pygame as pg
from settings import *
from levelsManager import *

class Ground(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.move_ip(0,-20)
        self.rect.x = x
        self.rect.y = y

        self.game = game


class Spikes(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game = game

    def update(self):
        self.mort()

    def mort(self):
        self.hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        if self.hit:
            self.game.new()

class Falling_traps(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, bounderies, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isFalling = False
        self.game = game
        self.w = w
        self.bounderies = bounderies

    def update(self):
        if self.rect.x < self.game.player.pos.x < self.rect.x + self.w or self.rect.x < self.game.head.rect.x < self.rect.x + self.w:
            self.isFalling = True

        self.fall()
        self.mort()

    def fall(self):
        if self.isFalling:
            self.rect.y += FALLSPEEDTRAP

        if self.rect.y > self.bounderies:
            self.rect.y = self.bounderies



    def mort(self):
        self.hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        if self.hit:
            self.game.new()

class Porte(pg.sprite.Sprite):

    def __init__(self,x,y,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.x = x
        self.y = y
        self.w = 40
        self.h = 100
        self.scene = Scene

        self.image = pg.Surface((self.w,self.h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        if hit:
            self.scene.currentLevel += 1
            print(self.scene.currentLevel)
            self.loadNewLevel()

    def loadNewLevel(self):
        self.game.new()


class Laser_horiz(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, game):
         pg.sprite.Sprite.__init__(self)
         self.game = game
         self.x = x
         self.y = y
         self.w = 40
         self.h = 100

         self.image = pg.Surface((self.w,self.h))
         self.image.fill(BLUE)
         self.image = pg.Surface((w, h))
         self.image.fill(ORCHID)
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.game = game
         self.w = w
         self.baselaser = x

    def update(self):
        hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        self.rect.x += LASER_SPEED
        self.contact()



    def contact(self):

        if self.rect.x == 1280:
            self.rect.x = self.baselaser


        self.hit_player = pg.sprite.spritecollide(self, self.game.player_sprite,False)

        if self.hit_player:
            self.game.new()

        self.hit_sprites = pg.sprite.spritecollide(self, self.game.platforms_sprite, False)

        if self.hit_sprites:
            self.rect.x = self.baselaser
