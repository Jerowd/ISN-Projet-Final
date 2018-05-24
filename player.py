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
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2,HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.canJump = False

        
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

    
    def jump(self):
        if self.canJump:
            self.vel.y = -PLAYER_JUMP


class Player_collision(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.w = 20
        self.h = 30
        self.image = pg.Surface((self.w, self.h))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.midbottom = self.game.player.pos

class Head_collision(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.w = 22
        self.h = 26
        self.image = pg.Surface((self.w, self.h))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.midbottom = self.game.head.pos 
    
        


class Head(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.isOn = True
        self.press = True
        self.timer = COOLDOWN_HEAD #timer pour empecher le spam de la tete
        self.w = 20
        self.h = 20
        self.x = self.game.player.rect.x + 0.5 * self.game.player.rect.w
        self.y = self.game.player.rect.y - 0.5 * self.game.player.rect.h - 10
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.apply_col = False
        self.timerTP = 2
        self.timerIsActive = False
        self.canTp = False

        #init pos
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def mouse_loc(self):
        #dÃƒÂ©tecte la position de la souris et permet de tirer la tÃƒÂªte
        self.mouse_raw = pg.mouse.get_pos()
        self.mouse_pos = vec(self.mouse_raw[0], self.mouse_raw[1])
        self.acc = self.mouse_pos - self.pos
        self.acc.scale_to_length(SHOOT_FORCE)

    def pressWait(self):
        #EmpÃƒÂªche de pouvoir spam l'envoie de la tÃƒÂªte
        self.timer -= 1
        if self.timer < 0:
            self.timer = COOLDOWN_HEAD 
            self.press = True

  










