import pygame as pg
from pygame.locals import *
pg.init()
pg.mixer.init()

WIDTH = 1280
HEIGHT = 720

GameRunning = True

TITRE = "Go aHead"
screen = pg.display.set_mode((1280, 720))
FPS = 60
MUSIC = pg.mixer.Sound("8bit_Music.wav")

image_background = pg.image.load("background.png").convert()
image_porte = pg.image.load("porte.png").convert_alpha()
image_Tchomp = pg.image.load("FallingTrap.png").convert_alpha()
image_head = pg.image.load("head.png").convert_alpha()
image_corps = pg.image.load("corps.png").convert_alpha()
image_porte = pg.image.load("porte.png").convert_alpha()
image_Tchomp = pg.image.load("FallingTrap.png").convert_alpha()
image_Spikes = pg.image.load("spikes.png").convert_alpha()
image_Buttons = pg.image.load("button.png").convert_alpha()
image_Buttons_2 = pg.image.load("button_2.png").convert_alpha()

image_LVL1 = pg.image.load("LVL1.jpg").convert_alpha()
image_LVL2 = pg.image.load("LVL2.jpg").convert_alpha()
image_LVL3 = pg.image.load("LVL3.jpg").convert_alpha()
image_LVL4 = pg.image.load("LVL4.jpg").convert_alpha()
image_LVL5 = pg.image.load("LVL5.jpg").convert_alpha()
image_LVL6 = pg.image.load("LVL6.jpg").convert_alpha()

FALLSPEEDTRAP = 15
NBGOUTTES = 100
LASER_SPEED = 8

whitedrops = []
reddrops = []
niv_atteints = []

#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK =  (255, 64, 236)
ORCHID = (218, 112, 214)
GREYART = (35, 55, 35)

#Physic
PLAYER_FRICTION = -0.25
PLAYER_ACC = 0.9
PLAYER_GRAV = 0.6
PLAYER_JUMP = 13
SHOOT_FORCE = 60

#Parametre de la tete
COOLDOWN_HEAD = 80 # en frames
TELEPORT_TIMER = 18

#PLAYER
JUMP_TIMER = 50

#Rect_Menu
POS_RECT_0 = (490,300,300,80)
ZONE_REVIVE = pg.Rect(POS_RECT_0)

POS_RECT_1 = (0, 20, 1280, 110)

POS_RECT_2 = (390, 300, 500, 80)
ZONE_JOUER = pg.Rect(POS_RECT_2)

POS_RECT_3 = (390, 400, 500, 80)
ZONE_NIVEAU = pg.Rect(POS_RECT_3)

POS_RECT_4 = (390, 500, 500, 80)
ZONE_OPTION = pg.Rect(POS_RECT_4)

POS_RECT_5 = (390, 600, 500, 80)
ZONE_QUITTER = pg.Rect(POS_RECT_5)

#Rect Lvl
POS_RECT_10 = (47, 150, 360, 195)
ZONE_LVL1 = pg.Rect(POS_RECT_10)

POS_RECT_11 = (449, 150, 360, 195)
ZONE_LVL2 = pg.Rect(POS_RECT_11)

POS_RECT_12 = (851, 150, 360, 195)
ZONE_LVL3 = pg.Rect(POS_RECT_12)

POS_RECT_13 = (851, 385, 360, 195)
ZONE_LVL4 = pg.Rect(POS_RECT_13)

POS_RECT_14 = (449, 385, 360, 195)
ZONE_LVL5 = pg.Rect(POS_RECT_14)

POS_RECT_15 = (47, 385, 360, 195)
ZONE_LVL6 = pg.Rect(POS_RECT_15)

POS_SCREEN = (0, 0, 1280, 720)
ZONE_SCREEN = pg.Rect(POS_SCREEN)



#polices  d'ÃƒÆ’Ã‚Â©criture
POLICE_TXT_1 = pg.font.SysFont('arial',60, False)
POLICE_TXT_2 = pg.font.SysFont('arial',50, True)
POLICE_TXT_3 = pg.font.SysFont('arial',180, True)
POLICE_TXT_4 = pg.font.SysFont('arial',30, True)
POLICE_TXT_5 = pg.font.SysFont('arial',25, True, True)

#Txt_Menu
TXT_1 = POLICE_TXT_1.render("GO  A HEAD",True, BLACK)
POS_TXT_1 = TXT_1.get_rect()
POS_TXT_1.centerx = 640
POS_TXT_1.centery = 75

#
TXT_2 = POLICE_TXT_2.render("NOUVELLE PARTIE",True, BLACK)
POS_TXT_2 = TXT_2.get_rect()
POS_TXT_2.centerx = 640
POS_TXT_2.centery = 340

#
TXT_3 = POLICE_TXT_2.render("CONTINUER",True, BLACK)
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
POS_TXT_6 = TXT_6.get_rect()
POS_TXT_6.centerx = 640
POS_TXT_6.centery = 640

TXT_18 = POLICE_TXT_2.render("Commandes",True, WHITE)
POS_TXT_18 = TXT_18.get_rect()
POS_TXT_18.centerx = 640
POS_TXT_18.centery = 200

TXT_19 = POLICE_TXT_4.render("*Q* pour aller a gauche et *D* pour aller a droite",True, WHITE)
POS_TXT_19 = TXT_19.get_rect()
POS_TXT_19.centerx = 640
POS_TXT_19.centery = 250

TXT_20 = POLICE_TXT_4.render("*A* pour lancer sa tête et *E* se téléporter dessus",True, WHITE)
POS_TXT_20 = TXT_20.get_rect()
POS_TXT_20.centerx = 640
POS_TXT_20.centery = 300

TXT_21 = POLICE_TXT_4.render("*ESPACE* pour sauter et *ECHAP* pour recommencer le niveau",True, WHITE)
POS_TXT_21 = TXT_21.get_rect()
POS_TXT_21.centerx = 640
POS_TXT_21.centery = 350

TXT_22 = POLICE_TXT_2.render("Volume",True, WHITE)
POS_TXT_22 = TXT_22.get_rect()
POS_TXT_22.centerx = 640
POS_TXT_22.centery = 450
#######
#Outro
TXT_23 = POLICE_TXT_3.render("FIN",True, WHITE)
POS_TXT_23 = TXT_23.get_rect()
POS_TXT_23.centerx = 640
POS_TXT_23.centery = 420
########

#
#Niveau
TXT_24 = POLICE_TXT_2.render("1",True, RED)
POS_TXT_24 = TXT_24.get_rect()
POS_TXT_24.centerx = 227
POS_TXT_24.centery = 247

TXT_25 = POLICE_TXT_2.render("2",True, RED)
POS_TXT_25 = TXT_25.get_rect()
POS_TXT_25.centerx = 629
POS_TXT_25.centery = 247

TXT_26 = POLICE_TXT_2.render("3",True, RED)
POS_TXT_26 = TXT_26.get_rect()
POS_TXT_26.centerx = 1031
POS_TXT_26.centery = 247

TXT_27 = POLICE_TXT_2.render("4",True, RED)
POS_TXT_27 = TXT_27.get_rect()
POS_TXT_27.centerx = 227
POS_TXT_27.centery = 482

TXT_28 = POLICE_TXT_2.render("5",True, RED)
POS_TXT_28 = TXT_28.get_rect()
POS_TXT_28.centerx = 629
POS_TXT_28.centery = 482

TXT_29 = POLICE_TXT_2.render("6",True, RED)
POS_TXT_29 = TXT_29.get_rect()
POS_TXT_29.centerx = 1031
POS_TXT_29.centery = 482

#Txt_Mort
TXT_7 = POLICE_TXT_2.render("REVIVRE",True, BLACK)
POS_TXT_7 = TXT_7.get_rect()
POS_TXT_7.centerx = 640
POS_TXT_7.centery = 340

TXT_8 = POLICE_TXT_2.render("MENU",True, BLACK)
POS_TXT_8 = TXT_8.get_rect()
POS_TXT_8.centerx = 640
POS_TXT_8.centery = 640

TXT_9 = POLICE_TXT_3.render("MORT",True, RED)
POS_TXT_9 = TXT_9.get_rect()
POS_TXT_9.centerx = 640
POS_TXT_9.centery = 520

TXT_10 = POLICE_TXT_2.render("COMMENCER", True, BLACK)
POS_TXT_10 = TXT_10.get_rect()
POS_TXT_10.centerx = 640
POS_TXT_10.centery = 640

TXT_11 = POLICE_TXT_4.render("Vous vous réveillez dans une salle qui vous est inconnue...", False, WHITE)
POS_TXT_11 = TXT_11.get_rect()
POS_TXT_11.centerx = 640
POS_TXT_11.centery = 200

TXT_12 = POLICE_TXT_4.render("Vous remarquez avec effroi de grosses marques sur votre cou !", False, WHITE)
POS_TXT_12 = TXT_12.get_rect()
POS_TXT_12.centerx = 640
POS_TXT_12.centery = 250

TXT_13 = POLICE_TXT_4.render("Que vous ont ils fait ?", False, WHITE)
POS_TXT_13 = TXT_13.get_rect()
POS_TXT_13.centerx = 640
POS_TXT_13.centery = 300

TXT_14 = POLICE_TXT_4.render("Vous remarquez un rapport d'expérience sur le sol. Vous lisez :", False, WHITE)
POS_TXT_14 = TXT_14.get_rect()
POS_TXT_14.centerx = 640
POS_TXT_14.centery = 350

TXT_15 = POLICE_TXT_5.render("* Le sujet 22.MK56.X a résisté à l'expérience et est parti dans le secteur SUD.", False, WHITE)
POS_TXT_15 = TXT_15.get_rect()
POS_TXT_15.centerx = 640
POS_TXT_15.centery = 425

TXT_16 = POLICE_TXT_5.render("  Il se serait évanoui. Evacuez le bâtiment il sera détruit par sécurité * ", False, WHITE)
POS_TXT_16 = TXT_16.get_rect()
POS_TXT_16.centerx = 640
POS_TXT_16.centery = 475

TXT_17 = POLICE_TXT_4.render("- Utilisez votre nouvelle capacité pour vous échapper du laboratoire. -", False, WHITE)
POS_TXT_17 = TXT_17.get_rect()
POS_TXT_17.centerx = 640
POS_TXT_17.centery = 550

#Volume option
POS_CADRE_1 = (320 , 500, 640, 25)
POS_CADRE_3 = (320 , 525, 25, 30)
POS_CADRE_2 = (320 , 555, 640, 25)
POS_CADRE_4 = (935, 525, 25, 30)

POS_VOLUME = pg.Rect((390,  525), (500, 30))
VOLUME_RECT = pg.Surface(POS_VOLUME.size)
