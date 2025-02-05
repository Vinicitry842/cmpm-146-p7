import pygame
import random

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (150, 150, 150)

WIDTH = 1200
HEIGHT = 600
FPS = 60
TITLE = "DUNGEON FROM AI"
BGCOLOR = LIGHTGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

## DEFAULT SETTINGS
# PLAYER_SPEED = 160
# PLAYER_HEALTH = 1000
# DAMAGE_RATE = 800
# SWAP_RATE = 100

## DEVELOPER MODE SETTINGS
PLAYER_SPEED = 500
PLAYER_HEALTH = 10000
DAMAGE_RATE = 800
SWAP_RATE = 100

#Sword settings
SWORD_SPEED = 200
SWORD_LIFETIME = 100
SWORD_RATE = 400
SWORD_DAMAGE = 3

#Wand settings
ORB_SPEED = 200
ORB_LIFETIME = 1000
ORB_RATE = 600
ORB_DAMAGE = 10

#Enemy
ENEMY_HEALTH = 30
ENEMY_SPEED = 130
ENEMY_DAMAGE = 10
ENEMY_KNOCKBACK = TILESIZE
RANGED_DAMAGE = 5
RANGED_SPEED = 160
WALK_R = 3000
WALK_L = 1500

BOSS_HEALTH = 150
BOSS_SPEED = 110
BOSS_DAMAGE = 10
BOSS_WEB_DAMAGE = 15
BOSS_WEB_SPEED = 200
BOSS_WEB_LIFETIME = 1300
BOSS_WEB_RATE_MIN = 10
BOSS_WEB_RATE_MAX = 30
BOSS_TRACK_MIN = 70
BOSS_TRACK_MAX = 100
BOSS_TRACK_LIFETIME = 1500
TRACK_DAMAGE = 5
TRACK_SPEED = 120

