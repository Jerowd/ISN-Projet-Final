import sys
import random
import pygame as pg
from jeu import*
from settings import*
from pygame.locals import *
from levelsManager import *


#classe qui gÃƒÆ’Ã‚Â¨re pluie en fond
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

#classe qui gÃƒÆ’Ã‚Â¨re l'affichage du menu
class Menu():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()

    #boucle principale du menu
    def loop(self, screen):
        while True:
            delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_JOUER.collidepoint(event.pos):
                        niv_atteints.clear()
                        Game().new()

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
                        print('QUITTER')
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

#classe qui gÃƒÆ’Ã‚Â¨re les options
class Option():
    def __init__(self):
        self.clock = pg.time.Clock()

    #creer les gouttes
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



                            print(volume)
                            MUSIC.set_volume(volume)

                            clickable_area = pg.Rect((x_cube, y_cube), (80, 20))
                            rect_screen = pg.Surface(clickable_area.size)
                            rect_screen.fill(WHITE)

            screen.fill(BLACK)

            #afficher les gouttes
            for i in range(int(len(whitedrops))):
                whitedrops[i].draw(screen, WHITE)
                whitedrops[i].y += whitedrops[i].speed
                whitedrops[i].impact_sol()

            pg.draw.rect(screen, BLACK, (345, 525, 590, 30))

            pg.draw.rect(screen, WHITE, POS_CADRE_1)
            pg.draw.rect(screen, WHITE, POS_CADRE_2)
            pg.draw.rect(screen, WHITE, POS_CADRE_3)
            pg.draw.rect(screen, WHITE, POS_CADRE_4)

            screen.blit(rect_screen, clickable_area)

            pg.draw.rect(screen, BLACK, (0,0, 1280, 23))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            pg.draw.rect(screen, WHITE, POS_RECT_5)
            screen.blit(TXT_6, POS_TXT_5)

            pg.display.flip()
            pg.display.update()

#classe qui gÃƒÆ’Ã‚Â¨re le choix des niveaux
class Niveau():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.scene = Scene

    #boucle principale du menu
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

            pg.draw.rect(screen, WHITE, POS_RECT_10)
            pg.draw.rect(screen, WHITE, POS_RECT_11)
            pg.draw.rect(screen, WHITE, POS_RECT_12)
            pg.draw.rect(screen, WHITE, POS_RECT_13)
            pg.draw.rect(screen, WHITE, POS_RECT_14)
            pg.draw.rect(screen, WHITE, POS_RECT_15)

            pg.draw.rect(screen, WHITE, POS_RECT_5)
            screen.blit(TXT_6, POS_TXT_5)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_QUITTER.collidepoint(event.pos):
                        return

                if ZONE_LVL0.collidepoint(pg.mouse.get_pos()):
                    pg.draw.rect(screen, RED, POS_RECT_10)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL0.collidepoint(event.pos):
                        self.scene.currentLevel = 0
                        Game().new()

                if ZONE_LVL1.collidepoint(pg.mouse.get_pos()):
                    pg.draw.rect(screen, RED, POS_RECT_11)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL0.collidepoint(event.pos):
                        self.scene.currentLevel = 1
                        Game().new()

                if ZONE_LVL2.collidepoint(pg.mouse.get_pos()):
                    pg.draw.rect(screen, RED, POS_RECT_12)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL0.collidepoint(event.pos):
                        self.scene.currentLevel = 2
                        Game().new()

                    if ZONE_LVL3.collidepoint(pg.mouse.get_pos()):
                        pg.draw.rect(screen, RED, POS_RECT_13)
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_LVL0.collidepoint(event.pos):
                        self.scene.currentLevel = 3
                        Game().new()

            pg.display.flip()
            pg.display.update()
################### CORE

#creer les gouttes
for i in range(NBGOUTTES):
            whitedrops.append(Rain())

MUSIC.play(loops=-1, fade_ms=5000)
MUSIC.set_volume(0.5)
Menu().loop(screen)
pg.quit()
