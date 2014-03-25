# Keyboard input and player movement in pygame
# -Ole Herman Schumacher Elgesem
#  www.github.com/olehermanse
# Simple template to get started with pygame

#Pygame is not yet updated for python 3+
#See Makefile

#Setup
import pygame, sys
from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()

#Window management
windowSurfaceObj = pygame.display.set_mode((800,600))
pygame.display.set_caption('Player Movement in pygame')

#Global variables for visuals and "game logic"
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)
playerx, playery = 0,0
unit = 20

#Fill BG with black and draw player on top
def drawScene():
	windowSurfaceObj.fill(blackColor)
	pygame.draw.rect(windowSurfaceObj, whiteColor, (playerx, playery, unit, unit))

#Moves player by (x*unit, y*unit)
def playerMove(x,y):
	global playerx
	global playery
	playerx += x*unit
	playery += y*unit

while True:
	#Handle events:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_w:
				playerMove(0, -1)
			if event.key == K_a:
				playerMove(-1, 0)
			if event.key == K_s:
				playerMove(0, 1)
			if event.key == K_d:
				playerMove(1, 0)
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
	#Drawing scene and updating window:
	drawScene()
	pygame.display.update()
	fpsClock.tick(30)
