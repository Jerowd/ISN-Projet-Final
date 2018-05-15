import pygame as pg
from pygame.locals import *
pg.init()
pg.mixer.init()

TITRE = "Go aHead"
screen = pg.display.set_mode((1280, 720))
FPS = 60
MUSIC = pg.mixer.Sound("8bit_Music.wav")

FALLSPEEDTRAP = 15
NBGOUTTES = 250

whitedrops = []
reddrops = []

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
POS_RECT_1 = (0, 20, 1280, 110)

POS_RECT_2 = (490, 300 , 300, 80)
ZONE_JOUER = pg.Rect(POS_RECT_2)

POS_RECT_3 = (490, 400, 300, 80)
ZONE_NIVEAU = pg.Rect(POS_RECT_3)

POS_RECT_4 = (490, 500, 300, 80)
ZONE_OPTION = pg.Rect(POS_RECT_4)

POS_RECT_5 = (490, 600, 300, 80)
ZONE_QUITTER = pg.Rect(POS_RECT_5)

#polices  d'écriture
POLICE_TXT_1 = pg.font.SysFont('arial',60, False)
POLICE_TXT_2 = pg.font.SysFont('arial',50, True)
POLICE_TXT_3 = pg.font.SysFont('arial',180, True)

#Txt_Menu
TXT_1 = POLICE_TXT_1.render("GO  A HEAD",True, BLACK)

POS_TXT_1 = TXT_1.get_rect()
POS_TXT_1.centerx = 640
POS_TXT_1.centery = 75

#
TXT_2 = POLICE_TXT_2.render("JOUER",True, BLACK)

POS_TXT_2 = TXT_2.get_rect()
POS_TXT_2.centerx = 640
POS_TXT_2.centery = 340

#
TXT_3 = POLICE_TXT_2.render("NIVEAU",True, BLACK)

POS_TXT_3 = TXT_3.get_rect()
POS_TXT_3.centerx = 640
POS_TXT_3.centery = 440

#
TXT_4 = POLICE_TXT_2.render("OPTION",True, BLACK)

POS_TXT_4 = TXT_4.get_rect()
POS_TXT_4.centerx = 640
POS_TXT_4.centery = 540

TXT_5 = POLICE_TXT_2.render("QUITTER",True, BLACK)

POS_TXT_5 = TXT_5.get_rect()
POS_TXT_5.centerx = 640
POS_TXT_5.centery = 640

#Txt_Option
TXT_6 = POLICE_TXT_2.render("RETOUR",True, BLACK)

POS_TXT_6 = TXT_2.get_rect()
POS_TXT_6.centerx = 625
POS_TXT_6.centery = 440

#Txt_Mort
TXT_7 = POLICE_TXT_2.render("REVIVRE",True, BLACK)

POS_TXT_7 = TXT_2.get_rect()
POS_TXT_7.centerx = 620
POS_TXT_7.centery = 340

TXT_8 = POLICE_TXT_2.render("MENU",True, BLACK)

POS_TXT_8 = TXT_2.get_rect()
POS_TXT_8.centerx = 650
POS_TXT_8.centery = 640

TXT_9 = POLICE_TXT_3.render("MORT",True, RED)

POS_TXT_9 = TXT_2.get_rect()
POS_TXT_9.centerx = 500
POS_TXT_9.centery = 420

#Volume option
POS_CADRE_1 = (320 , 500, 640, 25)
POS_CADRE_3 = (320 , 525, 25, 30)

POS_CADRE_2 = (320 , 555, 640, 25)
POS_CADRE_4 = (935, 525, 25, 30)

POS_VOLUME = pg.Rect((390,  525), (500, 30))
VOLUME_RECT = pg.Surface(POS_VOLUME.size)

#lASER
LASER_SPEED = 10
