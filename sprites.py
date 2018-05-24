import pygame as pg
from settings import *
from levelsManager import *

class Ground(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        #self.rect.move_ip(0,-20)
        self.rect.x = x
        self.rect.y = y
        self.timer = 10
       

        self.collision_player = [False] * 9
        self.collision_head = [False] * 9

        self.game = game

    def check_collision_player(self):
        self.collision_player[0] = self.rect.collidepoint(self.game.player_col.rect.topleft)
        self.collision_player[1] = self.rect.collidepoint(self.game.player_col.rect.topright)
        self.collision_player[2] = self.rect.collidepoint(self.game.player_col.rect.bottomleft)
        self.collision_player[3] = self.rect.collidepoint(self.game.player_col.rect.bottomright)
        self.collision_player[4] = self.rect.collidepoint(self.game.player_col.rect.midleft)
        self.collision_player[5] = self.rect.collidepoint(self.game.player_col.rect.midright)
        self.collision_player[6] = self.rect.collidepoint(self.game.player_col.rect.midtop)
        self.collision_player[7] = self.rect.collidepoint(self.game.player_col.rect.midbottom)
        self.collision_player[8] = self.rect.collidepoint(self.game.player_col.rect.center)


    def apply_collision_player(self):
        if self.collision_player[7]:
            self.game.player.rect.bottom = self.rect.top
            self.game.player.pos = self.game.player.rect.midbottom
            self.game.player.vel.y = 0
            self.game.player.acc.y = 0

        if self.collision_player[5]:
            self.game.player.rect.right = self.rect.left
            self.game.player.pos = self.game.player.rect.midbottom
            self.game.player.vel.x = 0
            

        if self.collision_player[4]:
            self.game.player.rect.left = self.rect.right
            self.game.player.pos = self.game.player.rect.midbottom
            self.game.player.vel.x = 0

        
    def check_collision_head(self):
        self.collision_head[0] = self.rect.collidepoint(self.game.head_col.rect.topleft)
        self.collision_head[1] = self.rect.collidepoint(self.game.head_col.rect.topright)
        self.collision_head[2] = self.rect.collidepoint(self.game.head_col.rect.bottomleft)
        self.collision_head[3] = self.rect.collidepoint(self.game.head_col.rect.bottomright)
        self.collision_head[4] = self.rect.collidepoint(self.game.head_col.rect.midleft)
        self.collision_head[5] = self.rect.collidepoint(self.game.head_col.rect.midright)
        self.collision_head[6] = self.rect.collidepoint(self.game.head_col.rect.midtop)
        self.collision_head[7] = self.rect.collidepoint(self.game.head_col.rect.midbottom)
        self.collision_head[8] = self.rect.collidepoint(self.game.head_col.rect.center)

    def apply_collision_head(self):
        if self.collision_head[7] and self.game.head.apply_col:
            self.game.head.pos = (self.game.head.pos.x, self.rect.top)
            self.game.head.rect.bottom = self.rect.top
            self.game.head.vel.y = 0

        if self.collision_head[5]:
            self.game.head.rect.right = self.rect.left
            self.game.head.vel.x = 0

        if self.collision_head[4]:
            self.game.head.rect.left = self.rect.right
            self.game.head.vel.x = 0

    def jump_collision(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 10
        if self.collision_player[7]:
            self.game.player.canJump = True
        if self.game.player.canJump and self.timer < 2:
            self.game.player.canJump = False

        
        
            

    def update(self):
        self.check_collision_player()
        self.apply_collision_player()
        self.check_collision_head() 
        self.apply_collision_head()
        self.jump_collision()


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

        if self.rect.x == WIDTH:
            self.rect.x = self.baselaser


        self.hit_player = pg.sprite.spritecollide(self, self.game.player_sprite,False)

        if self.hit_player:
            self.game.new()

        self.hit_sprites = pg.sprite.spritecollide(self, self.game.platforms_sprite, False)

        if self.hit_sprites:
            self.rect.x = self.baselaser


