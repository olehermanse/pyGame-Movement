'''============================================================================

File: main.py
From project: pyGameMovement
Date: 2015-03-29
Author: olehermanse ( http://www.github.com/olehermanse )
License: The MIT License (MIT)

The MIT License (MIT)

Copyright (c) 2015 olehermanse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

============================================================================'''


# Simple template to get started with pygame
# If you download the Makefile you can run by using make

# Loosely based on the pygame cheat sheet
#  www.inventwithpython.com/pygamecheatsheet.png
# See www.pygame.org for more info
# Pygame is not yet updated for python 3+

# Setup
import pygame, sys
from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()

# Window management
windowSurfaceObj = pygame.display.set_mode((800,600))
pygame.display.set_caption('Player Movement in pygame')

# Global variables for visuals and "game logic"
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(0,0,0)
playerx, playery = 0,0
unit = 40

# Fill BG with black and draw player on top
def drawScene():
	windowSurfaceObj.fill(blackColor)
	pygame.draw.rect(windowSurfaceObj, whiteColor, (playerx, playery, unit, unit))

# Moves player by (x*unit, y*unit)
def playerMove(x,y):
	global playerx
	global playery
	playerx += x*unit
	playery += y*unit

# Infinite loop can be broken by quit event
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
