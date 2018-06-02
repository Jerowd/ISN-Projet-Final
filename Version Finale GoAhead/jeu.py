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
        self.screen = pg.display.set_mode((1280,720))
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.running = True
        self.actual_score = 0
        self.gameoverInstance = Gameover()
        self.compteur_score = 0

        #INITIALISATION DES NIVEAUX
        niv_atteints= [ ]
        self.scene = Scene
        self.lvl1 = Lvl1
        self.lvl2 = Lvl2
        self.lvl3 = Lvl3
        self.lvl4 = Lvl4
        self.lvl5 = Lvl5
        self.lvl6 = Lvl6

    def spawnObjects(self):
        #crÃƒÂ©ation des groupes de sprites
        self.all_sprites = pg.sprite.Group()
        self.player_sprite = pg.sprite.Group()
        self.platforms_sprite = pg.sprite.Group()

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

        if self.scene.currentLevel == 1:
            self.lvl1.start(self)

        elif self.scene.currentLevel == 2:
            self.lvl2.start(self)


        elif self.scene.currentLevel == 3:
            self.lvl3.start(self)

        elif self.scene.currentLevel == 4:
            self.lvl4.start(self)

        elif self.scene.currentLevel == 5:
            self.lvl5.start(self)

        elif self.scene.currentLevel == 6:
            self.lvl6.start(self)

        elif self.scene.currentLevel == 7:
            Outro().loop(screen)

    def new(self):
        self.spawnObjects()
        self.scene.SpawnDefaultWalls(self)
        self.actual_score = 0
        self.run()

    def run(self):
        self.playing = True

        while self.playing:

            self.clock.tick(FPS)
            self.events()
            self.update()
            pg.draw.rect(screen, BLACK, self.POS_RECT_SCORE)
            screen.blit(self.TXT_SCORE, self.POS_TXT_SCORE)
            self.draw()

    def update(self):

        self.actual_score +=1

        #Txt_Score*
        if 2000 - self.actual_score >= 0:
            self.score = 2000 - self.actual_score
        self.POLICE_TXT_SCORE = pg.font.SysFont('arial', int(30), True)
        self.TXT_SCORE = self.POLICE_TXT_SCORE.render('Your score is :' + str(int(self.score)), True, WHITE)

        self.POS_TXT_SCORE = self.TXT_SCORE.get_rect()
        self.POS_TXT_SCORE.centerx = 150
        self.POS_TXT_SCORE.centery = 18

        self.POS_RECT_SCORE = (0, 0 , 1280, 20)

        #Txt_Niveau
        self.POLICE_TXT_NIVEAU = pg.font.SysFont('arial', int(30), True)
        self.TXT_NIVEAU = self.POLICE_TXT_NIVEAU.render('Lvl'+ str(self.scene.currentLevel), True, WHITE)

        self.POS_TXT_NIVEAU = self.TXT_NIVEAU.get_rect()
        self.POS_TXT_NIVEAU.centerx = 1200
        self.POS_TXT_NIVEAU.centery = 15


        #HEAD
        self.head.acc = vec(0,PLAYER_GRAV * 3)
        #player teleportation to head
        keys = pg.key.get_pressed()

        #tir
        if keys[pg.K_e] and self.head.isOn and self.head.press:
            self.head.isOn = False
            self.head.mouse_loc()
            self.head.press = False
            self.head.apply_col = True

        #teleportation du corps sur la tete
        elif keys[pg.K_q] and self.head.isOn == False:
            self.head.apply_col = False
            #self.player.jump()
            self.teleport()
            self.head.press = False

        if self.head.isOn:
            self.on()
        else:
            self.notOn()

        self.head.pressWait()

        #timer tp
        if self.head.timerIsActive:
            self.head.timerTP -= 1
            self.head.vel.y = -5
        if self.head.timerTP < 0:
            self.head.canTp = True
            self.head.timerTP = 10
            self.head.timerIsActive = False

        #teleporation
        if self.head.canTp:
            self.player.pos = self.head.rect.midtop
            self.player.rect.midbottom = self.head.rect.midtop
            self.head.isOn = True
            self.head.canTp = False

        #gestion des boutons dans les niveaux
        if self.scene.currentLevel == 4:
            self.boutonManager()

        if self.scene.currentLevel == 6:
            self.boutonManager_2()

        self.all_sprites.update()

        #tete sur le corps si isnotOn

    def on(self):
        self.head.rect.midbottom = self.player.rect.midtop
        self.head.pos = self.head.rect.midbottom

    def notOn(self):
        #permet au corps d'ÃƒÂªtre soumis ÃƒÂ  la gravitÃƒÂ© quand elle n'est pas au-dessus du corps
        self.head.acc += self.head.vel * PLAYER_FRICTION
        self.head.vel += self.head.acc
        self.head.pos += self.head.vel + 0.5 * self.head.acc

        self.head.rect.midbottom = self.head.pos

    def teleport(self):
        self.head.timerIsActive = True

    def boutonManager(self):
        if self.button_1.btn_1_active:
            self.button_1.btn_1_active = False
            self.platform_button_1 = Ground(820, 160, 120, 20, self)
            self.platforms_sprite.add(self.platform_button_1)
            self.all_sprites.add(self.platform_button_1)

        if self.button_2.btn_2_active:
            self.button_2.btn_2_active = False
            self.platform_button_2 = Ground(100, 280, 80, 450, self)
            self.platforms_sprite.add(self.platform_button_2)
            self.all_sprites.add(self.platform_button_2)
            self.platform_button_3 = Ground(180, 400, 80, 330, self)
            self.platforms_sprite.add(self.platform_button_3)
            self.all_sprites.add(self.platform_button_3)

    def boutonManager_2(self):

        if self.button_7.btn_7_active:
            self.button_7.btn_7_active = False
            self.platform_button_7 = sprites.Ground(510, 600, 240, 30, self)
            self.platforms_sprite.add(self.platform_button_7)
            self.all_sprites.add(self.platform_button_7)

    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                fichier = open("fichier_sauvegarde.txt", "w")

                for i in range(len(niv_atteints)):
                    fichier.write(str(niv_atteints[i]))
                    fichier.write('\n')
                fichier.close()
                pg.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                Gameover().loop(screen)

    def draw(self):
        self.screen.blit(image_background, (0,0))
        self.all_sprites.draw(self.screen)
        pg.draw.rect(screen, BLACK, self.POS_RECT_SCORE)
        screen.blit(self.TXT_SCORE, self.POS_TXT_SCORE)
        screen.blit(self.TXT_NIVEAU, self.POS_TXT_NIVEAU)
        pg.display.flip()

class Gameover():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()

    def loop(self, screen):
        while True:
            self.delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:

                    fichier = open("fichier_sauvegarde.txt", "w")
                    for i in range(len(niv_atteints)):
                        fichier.write(str(niv_atteints[i]))
                        fichier.write("\n")
                    fichier.close()

                    pg.quit()
                    sys.exit()
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_REVIVE.collidepoint(event.pos):
                        Game().new()


            screen.fill(BLACK)

            #afficher les gouttes
            for i in range(int(len(whitedrops))):
                whitedrops[i].draw(screen, RED)
                whitedrops[i].y += whitedrops[i].speed
                whitedrops[i].impact_sol()

            #afficher les rectangles blancs et les textes
            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, RED, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            pg.draw.rect(screen, RED, POS_RECT_0)
            screen.blit(TXT_7, POS_TXT_7)

            screen.blit(TXT_9, POS_TXT_9)

            pg.display.flip()
            pg.display.update()

class Outro():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.x_perso = 1280

    def loop(self, screen):
        while True:

            self.x_perso-=5

            self.delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    fichier = open("fichier_sauvegarde.txt", "w")
                    for i in range(len(niv_atteints)):
                        fichier.write(str(niv_atteints[i]))
                        fichier.write("\n")
                    fichier.close()

                    pg.quit()
                    sys.exit()
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    fichier = open("fichier_sauvegarde.txt", "w")
                    for i in range(len(niv_atteints)):
                        fichier.write(str(niv_atteints[i]))
                        fichier.write("\n")
                    fichier.close()

                    pg.quit()
                    sys.exit()
                    return

            screen.fill(BLACK)
            #afficher les gouttes
            for i in range(int(len(whitedrops))):
                whitedrops[i].draw(screen, WHITE)
                whitedrops[i].y += whitedrops[i].speed
                whitedrops[i].impact_sol()
            #afficher les rectangles blancs et les textes
            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            screen.blit(image_head, (self.x_perso + 8,575))
            screen.blit(image_corps, (self.x_perso,600))
            pg.draw.rect(screen, WHITE, (0,650, 1280, 90))

            if self.x_perso <= 640:
                screen.blit(TXT_23, POS_TXT_23)

            pg.display.flip()
            pg.display.update()
