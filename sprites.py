import pygame as pg
from settings import *
from levelsManager import *

class Ground(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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

        if self.collision_player[7] and self.game.player.jumping == False:
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

        if self.collision_player[6]:
            self.game.player.rect.top = self.rect.bottom + 20
            self.game.player.pos = self.game.player.rect.midbottom
            self.game.player.vel.y = 0

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
            self.game.head.pos = (self.game.head.rect.center[0], self.rect.top)
            self.game.head.rect.bottom = self.rect.top
            self.game.head.vel.y = 0
            self.game.head.vel.x = 0

        if self.collision_head[5]:
            self.game.head.rect.right = self.rect.left
            self.game.head.vel.x = 0

        if self.collision_head[4]:
            self.game.head.rect.left = self.rect.right
            self.game.head.vel.x = 0

        if self.collision_player[6]:
            self.game.head.rect.top = self.rect.bottom + 20
            self.game.head.pos = self.game.head.rect.midbottom
            self.game.head.vel.y = 0

    def jump_collision(self):
        if self.game.player.jumping == True and self.collision_player[7] == False:
            self.game.player.jumping = False

    def update(self):
        self.check_collision_player()
        self.apply_collision_player()
        self.check_collision_head()
        self.apply_collision_head()
        self.jump_collision()

class Spikes(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, game):
        pg.sprite.Sprite.__init__(self)
        self.image = image_Spikes
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game = game

    def update(self):
        self.mort()

    def mort(self):
        self.hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        if self.hit:
            self.game.gameoverInstance.loop(screen)

class Falling_traps(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, bounderies, game):
        pg.sprite.Sprite.__init__(self)
        self.image = image_Tchomp
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isFalling = False
        self.game = game
        self.w = w
        self.bounderies = bounderies

    def update(self):

        if self.rect.x < self.game.player.rect.x < self.rect.x + self.w or self.rect.x < self.game.head.rect.x < self.rect.x + self.w:
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
            self.game.gameoverInstance.loop(screen)

class Porte(pg.sprite.Sprite):

    def __init__(self,x,y, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.x = x
        self.y = y
        self.w = 40
        self.h = 100
        self.scene = Scene
        self.image = image_porte
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        self.score = 5000 - self.game.compteur_score

        if pg.sprite.spritecollide(self, self.game.player_sprite,False):
            self.scene.currentLevel += 1
            self.loadNewLevel()

    def loadNewLevel(self):
        self.game.new()

class Laser_horiz(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, sens, game):
         pg.sprite.Sprite.__init__(self)
         self.game = game
         self.x = x
         self.y = y
         self.w = 40
         self.h = 100
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

        if self.sens == "right":
            self.rect.x += LASER_SPEED

        else:
            self.rect.x -= LASER_SPEED
        self.contact()

    def contact(self):

        if self.rect.x == 1280:
            self.rect.x = self.baselaser
        self.hit_player = pg.sprite.spritecollide(self, self.game.player_sprite,False)

        if self.hit_player:
            self.game.gameoverInstance.loop(screen)
        self.hit_sprites = pg.sprite.spritecollide(self, self.game.platforms_sprite, False)

        if self.hit_sprites:
            self.rect.x = self.baselaser

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, nom_channel, perma, game):
         pg.sprite.Sprite.__init__(self)
         self.game = game
         self.x = x
         self.y = y
         self.w = w
         self.h = h
         self.perma = perma  #Permet de savoir si le bouton reste activÃ© pour toujours
         self.channel = nom_channel
         self.activated = False
         self.image = image_Buttons
         self.rect = self.image.get_rect()
         self.rect.x = self.x
         self.rect.y = self.y
         self.game = game
         self.compteur = 0
         self.btn_1_active = False
         self.btn_2_active = False
         self.btn_7_active = False

    def update(self):
        if self.activated:
            self.image = image_Buttons_2
        else:
            self.image = image_Buttons
        self.contact()

        if self.activated and self.perma:
            self.compteur += 1

        if self.compteur >= 300:
            self.activated = False
            self.compteur = 0

            if self.channel == "button_3":
                self.channel_button_3_undo()

            if self.channel == "button_4":
                self.channel_button_4_undo()

            if self.channel == "button_5":
                self.channel_button_5_undo()

            if self.channel == "button_6":
                self.channel_button_6_undo()

    def contact(self):
        self.hit_player = pg.sprite.spritecollide(self, self.game.player_sprite,False)

        if self.hit_player:
            self.game.player.rect.y = self.hit_player[0].rect.top
            self.game.player.pos = self.game.player.rect.midbottom
            self.activated = True
            self.image = image_Buttons_2

            if self.channel == "button_1" and self.activated:
                self.channel_button_1()

            if self.channel == "button_2" and self.activated:
                self.channel_button_2()

            if self.channel == "button_3" and self.activated:
                self.channel_button_3()

            if self.channel == "button_4" and self.activated:
                self.channel_button_4()

            if self.channel == "button_5" and self.activated:
                self.channel_button_5()

            if self.channel == "button_6" and self.activated:
                self.channel_button_6()

            if self.channel == "button_7" and self.activated:
                self.channel_button_7()

            if self.channel == "button_8" and self.activated:
                self.channel_button_8()

    def channel_button_1(self):
        self.btn_1_active = True

    def channel_button_2(self):
        self.btn_2_active = True

    def channel_button_3(self):
        self.game.all_sprites.remove(self.game.wall_button_1)
        self.game.platforms_sprite.remove(self.game.wall_button_1)

    def channel_button_3_undo(self):
        self.game.all_sprites.add(self.game.wall_button_1)
        self.game.platforms_sprite.add(self.game.wall_button_1)

    def channel_button_4(self):
        self.game.all_sprites.remove(self.game.wall_button_2)
        self.game.platforms_sprite.remove(self.game.wall_button_2)

    def channel_button_4_undo(self):
        self.game.all_sprites.add(self.game.wall_button_2)
        self.game.platforms_sprite.add(self.game.wall_button_2)

    def channel_button_5(self):
        self.game.all_sprites.remove(self.game.wall_button_3)
        self.game.platforms_sprite.remove(self.game.wall_button_3)

    def channel_button_5_undo(self):
        self.game.all_sprites.add(self.game.wall_button_3)
        self.game.platforms_sprite.add(self.game.wall_button_3)

    def channel_button_6(self):
        self.game.all_sprites.remove(self.game.wall_button_4)
        self.game.platforms_sprite.remove(self.game.wall_button_4)

    def channel_button_6_undo(self):
        self.game.all_sprites.add(self.game.wall_button_4)
        self.game.platforms_sprite.add(self.game.wall_button_4)

    def channel_button_7(self):
        self.btn_7_active = True

    def channel_button_8(self):
        self.game.all_sprites.remove(self.game.wall_button_5)
        self.game.platforms_sprite.remove(self.game.wall_button_5)
