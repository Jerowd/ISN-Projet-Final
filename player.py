import pygame as pg
from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.w = 20
        self.h = 20
        self.game = game

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.w,self.h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)
        self.pos = vec(640,360)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC

        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC

        if keys[pg.K_SPACE]:
            self.jump()

        self.move()
        self.limites()

    def jump(self):
        player_hit = pg.sprite.spritecollide(self, self.game.platforms_sprite,False)
        if player_hit:
            self.vel.y = -PLAYER_JUMP

    def limites(self):
        if self.pos.y > 720:
            self.game.new()

        if self.pos.x > 1280:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = 1280

        if self.pos.y - self.h < 0:
            self.pos.y = self.h

class Head(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.isOn = True
        self.press = True

        self.w = 20
        self.h = 20
        self.x = self.game.player.rect.x + 0.5 * self.game.player.rect.w
        self.y = self.game.player.rect.y - 0.5 * self.game.player.rect.h - 10
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        #init pos
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        self.debug()

        self.acc = vec(0,PLAYER_GRAV * 3) #gravitÃƒÂ© pour que le personnage tombe
        keys = pg.key.get_pressed()

        if keys[pg.K_e] and self.isOn and self.press:
            self.isOn = False
            self.mouse_loc()
            self.press = False

        elif keys[pg.K_q] and self.isOn == False and self.press:
            self.teleport()
            self.press = False

        if self.isOn:
            self.on()
            self.image.fill(RED)
        else:
            self.notOn()
            self.image.fill(GREEN)

        self.pressWait()

    def teleport(self):
        self.isOn = True
        self.game.player.pos = self.pos

    def mouse_loc(self):
        #dÃƒÂ©tecte la position de la souris et permet de tirer la tÃƒÂªte
        self.mouse_raw = pg.mouse.get_pos()
        self.mouse_pos = vec(self.mouse_raw[0], self.mouse_raw[1])
        self.acc = self.mouse_pos - self.pos
        self.acc.scale_to_length(SHOOT_FORCE)

    def pressWait(self):
        #EmpÃƒÂªche de pouvoir spam l'envoie de la tÃƒÂªte
        self.hit = pg.sprite.spritecollide(self, self.game.platforms_sprite,False)
        if self.hit:
            self.press = True
        elif self.rect.center == self.pos:
            self.press = True

    def on(self):
        #permet ÃƒÂ  la tÃƒÂªte d'ÃƒÂªtre au dessus du corps
        self.x = self.game.player.rect.x + 0.5 * self.game.player.rect.w
        self.y = self.game.player.rect.y - 0.5 * self.game.player.rect.h - 10
        self.pos = (self.x, self.y)
        self.rect.center = (self.x, self.y)

    def notOn(self):
        #permet au corps d'ÃƒÂªtre soumis ÃƒÂ  la gravitÃƒÂ© quand elle n'est pas au-dessus du corps
        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def debug(self):
        pass
