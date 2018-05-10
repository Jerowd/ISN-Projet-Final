import sys
import random
import pygame as pg
from jeu import *
from settings import *
from pygame.locals import *


#classe qui gère pluie en fond
class Drops():
    def __init__(self):
        self.x = random.randint( -10, WIDTH +10)
        self.y = random.randint( -HEIGHT - 25 , -25)
        self.w = 5
        self.h = random.randint( 25, 50)
        self.speed = random.randint( 8, 10)

    def draw(self, screen):
        self.drop = pg.draw.rect( screen, WHITE, ( self.x, self.y, self.w, self.h))

    def impact_sol(self):
        if self.y > HEIGHT +self.h:
            self.y = -25

#classe qui gère l'affichage du menu
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
                        Game().new()

                    if ZONE_OPTION.collidepoint(event.pos):
                        Option().loop(screen)
                        return

                    if ZONE_QUIT.collidepoint(event.pos):
                        print('QUITTER')
                        return

            screen.fill(BLACK)

            #afficher les gouttes
            for i in range(int(len(drops))):
                drops[i].draw(screen)
                drops[i].y += drops[i].speed
                drops[i].impact_sol()

            #afficher les rectangles blancs et les textes
            pg.draw.rect(screen, BLACK, (0,0, WIDTH, HEIGHT /32))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            pg.draw.rect(screen, WHITE, POS_RECT_2)
            screen.blit(TXT_2, POS_TXT_2)

            pg.draw.rect(screen, WHITE, POS_RECT_3)
            screen.blit(TXT_3, POS_TXT_3)

            pg.draw.rect(screen, WHITE, POS_RECT_4)
            screen.blit(TXT_4, POS_TXT_4)

            pg.display.flip()
            pg.display.update()

#classe qui gère les options
class Option():
    def __init__(self):
        self.clock = pg.time.Clock()

    #creer les gouttes
    def loop(self, screen):

        clickable_area = pg.Rect((WIDTH /2 - OPTION_RECT_VOL_WIDTH /2, 2*HEIGHT /3 +OPTION_RECT_VOL_HEIGHT/2 +15), (OPTION_RECT_VOL_HEIGHT, OPTION_RECT_VOL_WIDTH))
        rect_screen = pg.Surface(clickable_area.size)
        rect_screen.fill(WHITE)

        Mouse_x, Mouse_y = pg.mouse.get_pos()
        x_cube = WIDTH /2 - OPTION_RECT_VOL_HEIGHT /2
        y_cube = 2*HEIGHT /3 +OPTION_RECT_VOL_HEIGHT/2 +15

        while True:
            delta_t = self.clock.tick( FPS )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if ZONE_OPTION.collidepoint(event.pos):
                        Menu().loop(screen)
                        return
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if clickable_area.collidepoint(pg.mouse.get_pos()):
                        if POS_VOLUME.collidepoint(pg.mouse.get_pos()):

                            Mouse_x, Mouse_y = pg.mouse.get_pos()
                            x_cube = Mouse_x - OPTION_RECT_VOL_HEIGHT/2
                            x_vol = Mouse_x - (WIDTH /4 + 50)
                            MUSIC.set_volume((x_vol/ WIDTH /4) * 10)

                            clickable_area = pg.Rect((x_cube, y_cube), (OPTION_RECT_VOL_HEIGHT, OPTION_RECT_VOL_WIDTH))
                            rect_screen = pg.Surface(clickable_area.size)
                            rect_screen.fill(WHITE)

            screen.fill(BLACK)

            #afficher les gouttes
            for i in range(int(len(drops))):
                drops[i].draw(screen)
                drops[i].y += drops[i].speed
                drops[i].impact_sol()

            pg.draw.rect(screen, BLACK, POS_VOLUME)

            pg.draw.rect(screen, WHITE, POS_CADRE_1)
            pg.draw.rect(screen, WHITE, POS_CADRE_2)
            pg.draw.rect(screen, WHITE, POS_CADRE_3)
            pg.draw.rect(screen, WHITE, POS_CADRE_4)

            screen.blit(rect_screen, clickable_area)

            pg.draw.rect(screen, BLACK, (0,0, WIDTH, HEIGHT /32))
            pg.draw.rect(screen, WHITE, POS_RECT_1)
            screen.blit(TXT_1, POS_TXT_1)

            pg.draw.rect(screen, WHITE, POS_RECT_3)
            screen.blit(TXT_5, POS_TXT_3)

            pg.display.flip()
            pg.display.update()

################### CORE

#creer les gouttes
for i in range(NBGOUTTES):
            drop = Drops()
            drops.append(drop)

MUSIC.play(loops=-1, fade_ms=5000)
MUSIC.set_volume(0.5)
Menu().loop(screen)
pg.quit()
