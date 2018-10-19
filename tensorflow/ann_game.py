# youtube thenewboston python game development
# https://youtu.be/pNjSyBlbl_Q?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

import pygame

print(pygame.init())

WINDOW_HEIGHT = 200
WINDOW_WIDTH = 200

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 30
PLAYER_X_POS = 20
PLAYER_Y_POS = WINDOW_HEIGHT - PLAYER_HEIGHT
PLAYER_Y_ORIGINAL_POS = WINDOW_HEIGHT - PLAYER_HEIGHT
PLAYER_Y_POS_CHANGE = 0
JUMP_HEIGHT = 100

POS_CHANGE_GRANULARITY = 5

OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 40
OBSTACLE_Y_POS = WINDOW_WIDTH - OBSTACLE_HEIGHT
OBSTACLE_X_POS = WINDOW_WIDTH
OBSTACLE_X_POS_CHANGE = 2

obstaclePositions = []

screenshotCount = 0
iterationCOunt = 0
gameExit = False
FRAME_RATE = 60

white = (255,255,255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('jumper')
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

pygame.display.update()

clock = pygame.time.Clock()

def drawObstacles():
	for obstacleXPos in obstaclePositions:
		pygame.draw.rect(gameDisplay, black, [obstacleXPos,OBSTACLE_Y_POS, OBSTACLE_WIDTH, OBSTACLE_HEIGHT])

def addRandomObstacle():
	randomValBetween_0_and_50 = 50
	obstaclePositions.append(WINDOW_WIDTH-randomValBetween_0_and_50)

def putLabelInFile(value):	
	scoresFile.write(value+"\n")	

def isOkayToJump():
	# check for an obstacle nearing the player
	for obstacleXPos in obstaclePositions:
		if obstacleXPos <= PLAYER_X_POS+20:
			return True
	return False
	
def jump():
	PLAYER_Y_POS_CHANGE = -1*POS_CHANGE_GRANULARITY

scoresFile = open("labels.txt","a")
while not gameExit:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				gameExit = True
			if event.key == pygame.K_SPACE:			
				# make the player start going up only if it is stationary
				if PLAYER_Y_POS_CHANGE == 0:
					PLAYER_Y_POS_CHANGE = -1*POS_CHANGE_GRANULARITY

	# when you have jumped high enough come back
	if PLAYER_Y_POS == PLAYER_Y_ORIGINAL_POS - JUMP_HEIGHT:
		PLAYER_Y_POS_CHANGE = POS_CHANGE_GRANULARITY
	
	# PLAYER_Y_POS_CHANGE > 0 means that the player is coming down
	if PLAYER_Y_POS_CHANGE > 0 and PLAYER_Y_POS == PLAYER_Y_ORIGINAL_POS:
		PLAYER_Y_POS_CHANGE = 0

	# update the position of player
	PLAYER_Y_POS += PLAYER_Y_POS_CHANGE
	
	# update the position of the each obstacle
	for index, position in enumerate(obstaclePositions):
		obstaclePositions[index] -= OBSTACLE_X_POS_CHANGE
	
	# remove the passed obstacle from the obstacle list
	for index, obstacleXPos in enumerate(obstaclePositions):
		if obstacleXPos < 0:
			obstaclePositions.pop(index)
		
	# add an obstacle every 100th iteration
	if iterationCOunt % 100 == 0:
		addRandomObstacle()	

	# check if an obstacle collided with the player 
	for obstacleXPos in obstaclePositions:
		# check if obstacle has crossed into the player's territory
		if obstacleXPos < PLAYER_X_POS+PLAYER_WIDTH:
			# check if player is blocking
			if OBSTACLE_Y_POS <= PLAYER_Y_POS:
				gameExit = True

	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [PLAYER_X_POS,PLAYER_Y_POS, PLAYER_WIDTH, PLAYER_HEIGHT])	
	drawObstacles()
	pygame.display.update()
	iterationCOunt += 1

	clock.tick(FRAME_RATE)
	
scoresFile.close()
pygame.quit()
quit()