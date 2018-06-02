import sys
import random
import pygame as pg
from jeu import*
from settings import*
from pygame.locals import *
from levelsManager import *

class Rain():

    def __init__(self):
        self.x = random.randint( -10, 1290)
        self.y = random.randint( -745 , -25)
        self.w = 5
        self.h = random.randint( 25, 50)
        self.speed = random.randint( 8, 10)
        self.color = color

    def draw(self, screen, color):
        self.drop = pg.draw.rect( screen, color, ( self.x, self.y, self.w, self.h))

    def impact_sol(self):
        if self.y > 720 +self.h:
            self.y = -25

class Menu():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()

    def loop(self, screen):

        while True:
            delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_JOUER.collidepoint(event.pos):
                        niv_atteints.clear()
                        Intro().loop(screen)

                    if ZONE_NIVEAU.collidepoint(event.pos):
                        if not "lvl0" in niv_atteints:
                            with open("fichier_sauvegarde.txt", "r") as f:
                                for line in f:
                                    niv_atteints.append(line[:4])
                        Niveau().loop(screen)

                    if ZONE_OPTION.collidepoint(event.pos):
                        Option().loop(screen)
                        return

                    if ZONE_QUITTER.collidepoint(event.pos):
                        return

            screen.fill(BLACK)

            #afficher les gouttes
            for i in range(int(len(whitedrops))):
                whitedrops[i].draw(screen,WHITE)
                whitedrops[i].y += whitedrops[i].speed
                whitedrops[i].impact_sol()

            #afficher les rectangles blancs et les textes
            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            pg.draw.rect(screen, WHITE, POS_RECT_2)
            screen.blit(TXT_2, POS_TXT_2)

            pg.draw.rect(screen, WHITE, POS_RECT_3)
            screen.blit(TXT_3, POS_TXT_3)

            pg.draw.rect(screen, WHITE, POS_RECT_4)
            screen.blit(TXT_4, POS_TXT_4)

            pg.draw.rect(screen, WHITE, POS_RECT_5)
            screen.blit(TXT_5, POS_TXT_5)

            pg.display.flip()
            pg.display.update()

class Option():

    def __init__(self):
        self.clock = pg.time.Clock()

    def loop(self, screen):

        clickable_area = pg.Rect((600, 530), (80, 20))
        rect_screen = pg.Surface(clickable_area.size)
        rect_screen.fill(WHITE)

        Mouse_x, Mouse_y = pg.mouse.get_pos()

        x_cube = 620
        y_cube = 530

        while True:
            delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_QUITTER.collidepoint(event.pos):
                        Menu().loop(screen)
                        return

                if pg.mouse.get_pressed()[0]:
                    if clickable_area.collidepoint(pg.mouse.get_pos()):
                        if POS_VOLUME.collidepoint(pg.mouse.get_pos()):

                            Mouse_x, Mouse_y = pg.mouse.get_pos()
                            x_cube = Mouse_x - 40
                            volume = (Mouse_x -380)/ 500
                            MUSIC.set_volume(volume)

                            clickable_area = pg.Rect((x_cube, y_cube), (80, 20))
                            rect_screen = pg.Surface(clickable_area.size)
                            rect_screen.fill(WHITE)

            screen.fill(BLACK)
            pg.draw.rect(screen, BLACK, (345, 525, 590, 30))

            pg.draw.rect(screen, WHITE, POS_CADRE_1)
            pg.draw.rect(screen, WHITE, POS_CADRE_2)
            pg.draw.rect(screen, WHITE, POS_CADRE_3)
            pg.draw.rect(screen, WHITE, POS_CADRE_4)

            screen.blit(rect_screen, clickable_area)

            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            screen.blit(TXT_18, POS_TXT_18)
            screen.blit(TXT_19, POS_TXT_19)
            screen.blit(TXT_20, POS_TXT_20)
            screen.blit(TXT_21, POS_TXT_21)
            screen.blit(TXT_22, POS_TXT_22)

            pg.draw.rect(screen, WHITE, POS_RECT_5)
            screen.blit(TXT_6, POS_TXT_6)

            pg.display.flip()
            pg.display.update()

class Niveau():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.scene = Scene

    def loop(self, screen):
        while True:
            delta_t = self.clock.tick( FPS )

            screen.fill(BLACK)

            for i in range(int(len(whitedrops))):
                whitedrops[i].draw(screen, WHITE)
                whitedrops[i].y += whitedrops[i].speed
                whitedrops[i].impact_sol()

            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            if "lvl1" in niv_atteints:
                screen.blit(image_LVL1, POS_RECT_10)
            else:
                pg.draw.rect(screen, WHITE, POS_RECT_10)

            if "lvl2" in niv_atteints:
                screen.blit(image_LVL2, POS_RECT_11)
            else:
                pg.draw.rect(screen, WHITE, POS_RECT_11)

            if "lvl3" in niv_atteints:
                screen.blit(image_LVL3, POS_RECT_12)
            else:
                pg.draw.rect(screen, WHITE, POS_RECT_12)

            if "lvl4" in niv_atteints:
                screen.blit(image_LVL4, POS_RECT_13)
            else:
                pg.draw.rect(screen, WHITE, POS_RECT_13)

            if "lvl5" in niv_atteints:
                screen.blit(image_LVL5, POS_RECT_14)
            else:
                pg.draw.rect(screen, WHITE, POS_RECT_14)

            if "lvl6" in niv_atteints:
                screen.blit(image_LVL6, POS_RECT_15)
            else:
                pg.draw.rect(screen, WHITE, POS_RECT_15)


            screen.blit(TXT_24, POS_TXT_24)
            screen.blit(TXT_25, POS_TXT_25)
            screen.blit(TXT_26, POS_TXT_26)
            screen.blit(TXT_27, POS_TXT_29)
            screen.blit(TXT_28, POS_TXT_28)
            screen.blit(TXT_29, POS_TXT_27)

            pg.draw.rect(screen, WHITE, POS_RECT_5)
            screen.blit(TXT_6, POS_TXT_5)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_QUITTER.collidepoint(event.pos):
                        return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL1.collidepoint(event.pos) and "lvl1" in niv_atteints:
                        self.scene.currentLevel = 1
                        Game().new()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL2.collidepoint(event.pos) and "lvl2" in niv_atteints:
                        self.scene.currentLevel = 2
                        Game().new()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL3.collidepoint(event.pos) and "lvl3" in niv_atteints:
                        self.scene.currentLevel = 3
                        Game().new()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL4.collidepoint(event.pos) and "lvl4" in niv_atteints:
                        self.scene.currentLevel = 4
                        Game().new()


                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL5.collidepoint(event.pos) and "lvl5" in niv_atteints:
                        self.scene.currentLevel = 5
                        Game().new()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL6.collidepoint(event.pos) and "lvl6" in niv_atteints:
                        self.scene.currentLevel = 6
                        Game().new()

            pg.display.flip()
            pg.display.update()

class Intro():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()

    def loop(self, screen):
        while True:
            delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_QUITTER.collidepoint(event.pos):
                        Game().new()

            screen.fill(BLACK)
            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            pg.draw.rect(screen, WHITE, POS_RECT_5)
            screen.blit(TXT_10, POS_TXT_10)
            screen.blit(TXT_11, POS_TXT_11)
            screen.blit(TXT_12, POS_TXT_12)
            screen.blit(TXT_13, POS_TXT_13)
            screen.blit(TXT_14, POS_TXT_14)
            screen.blit(TXT_15, POS_TXT_15)
            screen.blit(TXT_16, POS_TXT_16)
            screen.blit(TXT_17, POS_TXT_17)

            pg.display.flip()
            pg.display.update()

for i in range(NBGOUTTES):
            whitedrops.append(Rain())

MUSIC.play(loops=-1, fade_ms=5000)
MUSIC.set_volume(0.5)
Menu().loop(screen)
pg.quit()
