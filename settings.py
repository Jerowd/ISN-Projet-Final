import pygame as pg
from pygame.locals import *
pg.init()
pg.mixer.init()


TITRE = "Go aHead"
WIDTH = 1280	
HEIGHT = 720
screen = pg.display.set_mode((1500, 750))
FPS = 60
MUSIC = pg.mixer.Sound("8bit_Music.wav")

FALLSPEEDTRAP = 15
NBGOUTTES = int(WIDTH/4)
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
PLAYER_FRICTION = -0.18
PLAYER_ACC = 0.8
PLAYER_GRAV = 0.4
PLAYER_JUMP = 12
SHOOT_FORCE = 30

#Parametre de la tete
COOLDOWN_HEAD = 80 # en frames
TELEPORT_TIMER = 10

#Rect_Menu

POS_RECT_1 = (0, HEIGHT /32, WIDTH, HEIGHT /8)

POS_RECT_2 = (WIDTH /3 +75, HEIGHT /3, WIDTH /3 -125, HEIGHT /8)
ZONE_JOUER = pg.Rect(POS_RECT_2)

POS_RECT_3 = (WIDTH /3 +75, HEIGHT /3 + HEIGHT /8 + 20, WIDTH /3 -125, HEIGHT /8)
ZONE_OPTION = pg.Rect(POS_RECT_3)

POS_RECT_4 = (WIDTH /3 +75, HEIGHT /3 + HEIGHT /4 + 40, WIDTH /3 -125, HEIGHT /8)
ZONE_QUIT = pg.Rect(POS_RECT_4)

#Txt_Menu

POLICE_TXT_1 = pg.font.SysFont('arial', int(HEIGHT/12), False)
TXT_1 = POLICE_TXT_1.render("GO  A HEAD",True, BLACK)

POS_TXT_1 = TXT_1.get_rect()
POS_TXT_1.centerx = WIDTH /2
POS_TXT_1.centery = HEIGHT /32 +HEIGHT /16
#

POLICE_TXT_2 = pg.font.SysFont('arial', int(HEIGHT/16), True)
TXT_2 = POLICE_TXT_1.render("JOUER",True, BLACK)

POS_TXT_2 = TXT_2.get_rect()
POS_TXT_2.centerx = WIDTH /2 + 10
POS_TXT_2.centery = HEIGHT /3 + HEIGHT /16
#

POLICE_TXT_3 = pg.font.SysFont('arial', int(HEIGHT/16), True)
TXT_3 = POLICE_TXT_1.render("OPTION",True, BLACK)

POS_TXT_3 = TXT_2.get_rect()
POS_TXT_3.centerx = WIDTH /2
POS_TXT_3.centery = HEIGHT /3 + HEIGHT /8 + 20 + HEIGHT /16
#
POLICE_TXT_4 = pg.font.SysFont('arial', int(HEIGHT/16), True)
TXT_4 = POLICE_TXT_1.render("QUITTER",True, BLACK)

POS_TXT_4 = TXT_2.get_rect()
POS_TXT_4.centerx = WIDTH /2 - 10
POS_TXT_4.centery = HEIGHT /3 + HEIGHT /4 + 40 + HEIGHT /16

#Txt_Option

POLICE_TXT_5 = pg.font.SysFont('arial', int(HEIGHT/16), True)
TXT_5 = POLICE_TXT_1.render("RETOUR",True, BLACK)

POS_TXT_5 = TXT_2.get_rect()
POS_TXT_5.centerx = WIDTH /2
POS_TXT_5.centery = HEIGHT /3 + HEIGHT /8 + 20 + HEIGHT /16

#Volume option

OPTION_RECT_VOL_HEIGHT = HEIGHT /8 -50
OPTION_RECT_VOL_WIDTH = HEIGHT /8 -50

pg.key.set_repeat(1, 20)

POS_CADRE_1 = (WIDTH /4 , 2*HEIGHT /3, WIDTH /2, 25)
POS_CADRE_3 = (WIDTH /4 , 2*HEIGHT /3 + HEIGHT /8, WIDTH /2, 25)

POS_CADRE_2 = (WIDTH /4 , 2*HEIGHT /3 + 25, 25, HEIGHT /8)
POS_CADRE_4 = (WIDTH /4 + WIDTH /2 - 25, 2*HEIGHT /3 + 25, 25, HEIGHT /8)



POS_VOLUME = pg.Rect((WIDTH/4 + HEIGHT /8 -50,  2*HEIGHT/3), (WIDTH/2 -HEIGHT /8, HEIGHT/8 +25))
VOLUME_RECT = pg.Surface(POS_VOLUME.size)

#lASER
LASER_SPEED = 10
