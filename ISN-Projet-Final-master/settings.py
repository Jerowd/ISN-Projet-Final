import pygame as pg
from pygame.locals import *
pg.init()
pg.mixer.init()


TITRE = "Go aHead"
screen = pg.display.set_mode((1280, 720))
FPS = 60
MUSIC = pg.mixer.Sound("8bit_Music.wav")

FALLSPEEDTRAP = 15
NBGOUTTES = 320
drops = []

#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK =  (255, 64, 236)
ORCHID = (218, 112, 214)

#Physic
PLAYER_FRICTION = -0.12
PLAYER_ACC = 0.8
PLAYER_GRAV = 0.4
PLAYER_JUMP = 12
SHOOT_FORCE = 30

#Rect_Menu
POS_RECT_1 = (0, 23, 1280, 90)

POS_RECT_2 = (500, 240 , 300, 90)
ZONE_JOUER = pg.Rect(POS_RECT_2)

POS_RECT_3 = (500, 350, 300, 90)
ZONE_OPTION = pg.Rect(POS_RECT_3)

POS_RECT_4 = (500, 460, 300, 90)
ZONE_QUIT = pg.Rect(POS_RECT_4)

#Txt_Menu
POLICE_TXT_1 = pg.font.SysFont('arial', int(60 ), False)
TXT_1 = POLICE_TXT_1.render("GO  A HEAD",True, BLACK)

POS_TXT_1 = TXT_1.get_rect()
POS_TXT_1.centerx = 640
POS_TXT_1.centery = 68

#
POLICE_TXT_2 = pg.font.SysFont('arial', int(45 ), True)
TXT_2 = POLICE_TXT_1.render("JOUER",True, BLACK)

POS_TXT_2 = TXT_2.get_rect()
POS_TXT_2.centerx = 650
POS_TXT_2.centery = 285

#
POLICE_TXT_3 = pg.font.SysFont('arial', int(45 ), True)
TXT_3 = POLICE_TXT_1.render("OPTION",True, BLACK)

POS_TXT_3 = TXT_2.get_rect()
POS_TXT_3.centerx = 640
POS_TXT_3.centery = 395

#
POLICE_TXT_4 = pg.font.SysFont('arial', int(45 ), True)
TXT_4 = POLICE_TXT_1.render("QUITTER",True, BLACK)

POS_TXT_4 = TXT_2.get_rect()
POS_TXT_4.centerx = 630
POS_TXT_4.centery = 505

#Txt_Option
POLICE_TXT_5 = pg.font.SysFont('arial', int(45 ), True)
TXT_5 = POLICE_TXT_1.render("RETOUR",True, BLACK)

POS_TXT_5 = TXT_2.get_rect()
POS_TXT_5.centerx = 640
POS_TXT_5.centery = 395

#Volume option
POS_CADRE_1 = (320 , 480, 640, 25)
POS_CADRE_3 = (320 , 570, 640, 25)

POS_CADRE_2 = (320 , 505, 25, 90)
POS_CADRE_4 = (935, 505, 25, 90)

POS_VOLUME = pg.Rect((360,  480), (550, 115))
VOLUME_RECT = pg.Surface(POS_VOLUME.size)

#lASER
LASER_SPEED = 10
