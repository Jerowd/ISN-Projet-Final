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

        self.image_collision = pg.Surface((self.w + 2, self.h + 2))
        self.image_collision.fill(GREEN)
        self.rect_col = self.image_collision.get_rect()

        
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
        if self.canJump:
            self.vel.y = -PLAYER_JUMP

    def limites(self):
        if self.pos.y > HEIGHT:
            self.game.new()

        if self.pos.x > WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y - self.h < 0:
            self.pos.y = self.h

class Player_collision(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.w = 20
        self.h = 30
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(GREEN)
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
        self.image.fill(PINK)
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

        #init pos
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        self.acc = vec(0,PLAYER_GRAV * 3) #gravitÃƒÂ© pour que le personnage tombe

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

    def notOn(self):
        #permet au corps d'ÃƒÂªtre soumis ÃƒÂ  la gravitÃƒÂ© quand elle n'est pas au-dessus du corps
        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos










