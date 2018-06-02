import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, game):
        self.w = 40
        self.h = 52
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = image_corps
        self.rect = self.image.get_rect()
        self.rect.center = (-20, -20)
        self.pos = vec(-20, -20)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.canJump = False
        self.timer = JUMP_TIMER

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

        elif keys[pg.K_d]:
            self.acc.x = PLAYER_ACC

        else:
            self.acc.x = 0
            self.vel.x = 0

        if keys[pg.K_SPACE] and self.canJump:
            self.jump()
        self.move()

    def jump(self):
        self.jumping = True
        self.vel.y = -PLAYER_JUMP

class Player_collision(pg.sprite.Sprite):

    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.w = 40
        self.h = 66
        self.image = pg.Surface((self.w, self.h))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = self.game.player.rect.center

        if pg.sprite.spritecollide(self, self.game.platforms_sprite, False):
            self.game.player.canJump = True
        else:
            self.game.player.canJump = False

class Head_collision(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.w = 22
        self.h = 25
        self.image = pg.Surface((self.w, self.h))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = self.game.head.rect.center

class Head(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.isOn = True
        self.press = True
        self.timer = COOLDOWN_HEAD
        self.w = 20
        self.h = 20
        self.x = self.game.player.rect.x + 0.5 * self.game.player.rect.w
        self.y = self.game.player.rect.y - 0.5 * self.game.player.rect.h - 10
        self.image = image_head
        self.rect = self.image.get_rect()
        self.mouse_raw = pg.mouse.get_pos()
        self.apply_col = False
        self.timerTP = 10
        self.timerIsActive = False
        self.canTp = False
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def mouse_loc(self):
        self.mouse_raw = pg.mouse.get_pos()
        self.mouse_pos = vec(self.mouse_raw[0], self.mouse_raw[1])
        self.acc = self.mouse_pos - self.pos
        self.acc.scale_to_length(SHOOT_FORCE)

    def pressWait(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = COOLDOWN_HEAD
            self.press = True
