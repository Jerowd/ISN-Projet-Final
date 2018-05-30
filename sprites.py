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
            self.game.head.rect.bottom = self.head.top
            self.game.head.pos = self.game.player.head.midbottom
            self.game.head.vel.y = 0

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
            self.game.gameoverInstance.loop(screen)

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

        self.highscore_lvl0 = highscore_lvl0
        self.highscore_lvl1 = highscore_lvl1
        self.highscore_lvl2 = highscore_lvl2
        self.highscore_lvl3 = highscore_lvl3

        self.image = pg.Surface((self.w,self.h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        hit = pg.sprite.spritecollide(self, self.game.player_sprite,False)
        self.score = 5000 - self.game.compteur_score
        if pg.sprite.spritecollide(self, self.game.player_sprite,False):
            if self.game.scene.currentLevel == 0 and self.score > self.highscore_lvl0:
                self.highscore_lvl0 = (self.score)
            if self.game.scene.currentLevel == 1 and self.score > self.highscore_lvl1:
                self.highscore_lvl1 = (self.score)
            if self.game.scene.currentLevel == 2 and self.score > self.highscore_lvl2:
                self.highscore_lvl2 = (self.score)
            if self.game.scene.currentLevel == 3 and self.score > self.highscore_lvl3:
                self.highscore_lvl3 = (self.score)
            self.scene.currentLevel += 1

            print(self.scene.currentLevel)

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
         self.image = pg.Surface((self.w,self.h))
         self.image.fill(RED)
         self.rect = self.image.get_rect()
         self.rect.x = self.x
         self.rect.y = self.y
         self.game = game
         self.compteur = 0


    def update(self):
        if self.activated:
            self.image.fill(GREEN)
        else:
            self.image.fill(RED)
        self.contact()
        if self.activated and self.perma:
            self.compteur += 1
        if self.compteur >= 500:
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
            self.image.fill(GREEN)

            #Quelle action va effectuer le bouton ?

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

    #actions des boutons

    def channel_button_1(self):
        self.platform_button_1 = Ground(820, 160, 120, 20, self)
        self.game.platforms_sprite.add(self.platform_button_1)
        self.game.all_sprites.add(self.platform_button_1)

    def channel_button_2(self):
        self.platform_button_2 = Ground(100, 280, 80, 450, self)
        self.game.platforms_sprite.add(self.platform_button_2)
        self.game.all_sprites.add(self.platform_button_2)
        self.platform_button_3 = Ground(180, 400, 80, 330, self)
        self.game.platforms_sprite.add(self.platform_button_3)
        self.game.all_sprites.add(self.platform_button_3)

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
