import pygame
from random import randint

print(pygame.init())

WINDOW_HEIGHT = 200
WINDOW_WIDTH = 600

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 30
PLAYER_X_POS = 20
PLAYER_Y_POS = WINDOW_HEIGHT - PLAYER_HEIGHT
PLAYER_Y_ORIGINAL_POS = WINDOW_HEIGHT - PLAYER_HEIGHT
PLAYER_Y_POS_CHANGE = 0
JUMP_HEIGHT = 100

POS_CHANGE_GRANULARITY = 5

MIN_OBSTACLE_WIDTH = 20
MIN_OBSTACLE_HEIGHT = 40
OBSTACLE_Y_POS = 160
OBSTACLE_X_POS = WINDOW_WIDTH
OBSTACLE_X_POS_CHANGE = 2

obstacles = []

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

class Obstacle:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

def drawObstacles():
	for obstacle in obstacles:
		pygame.draw.rect(gameDisplay, black, [obstacle.x, WINDOW_HEIGHT-obstacle.height, obstacle.width, obstacle.height])

def addRandomObstacle():
	if len(obstacles) < 4:
		newObstaclePos = WINDOW_WIDTH
		if len(obstacles) > 0:
			print(obstacles[-1].height)
			lastObstaclePos = obstacles[-1].x
			newObstaclePos = lastObstaclePos + randint(100, 200)
		height = MIN_OBSTACLE_HEIGHT+randint(0, 20)
		width = MIN_OBSTACLE_WIDTH+randint(0, 20)		
		obstacles.append(Obstacle(newObstaclePos, WINDOW_HEIGHT-height, width, height))

def isOkayToJump():
	# check for an obstacle nearing the player
	for obstacle in obstacles:
		if obstacle.x <= PLAYER_X_POS+20:
			return True
	return False
	
def jump():
	PLAYER_Y_POS_CHANGE = -1*POS_CHANGE_GRANULARITY

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
	for index, obstacle in enumerate(obstacles):
		obstacles[index].x -= OBSTACLE_X_POS_CHANGE
	
	# remove the passed obstacle from the obstacle list
	for index, obstacle in enumerate(obstacles):
		if obstacle.x < 0:
			obstacles.pop(index)
		
	# add an obstacle every 100th iteration
	#if iterationCOunt % 100 == 0:
	addRandomObstacle()	

	# check if an obstacle collided with the player 
	for obstacle in obstacles:
		# check if obstacle has crossed into the player's territory
		if obstacle.x < PLAYER_X_POS+PLAYER_WIDTH:
			# check if player is blocking
			if obstacle.y <= PLAYER_Y_POS:
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