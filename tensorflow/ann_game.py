import pygame
import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np
import cv2
from keras.models import model_from_yaml
# from keras.models import model_from_json

# ------------------------------------------------------------------------------------
# ---------------------------- LOAD THE MODEL ----------------------------------------
# ------------------------------------------------------------------------------------

'''
# load saved model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json, custom_objects={'GlorotUniform': tf.keras.initializers.glorot_uniform(seed=None)})
'''

# load YAML and create model
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml, custom_objects={'GlorotUniform': tf.keras.initializers.glorot_uniform(seed=None)})

loaded_model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track

# load weights into the new model
loaded_model.load_weights("model.h5")
print(" ----- loaded model from disk")

# ------------------------------------------------------------------------------------
# ---------------------------- LOAD THE MODEL ----------------------------------------
# ------------------------------------------------------------------------------------

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------- GAME PART ------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

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

def isOkayToJump():
	# check for an obstacle nearing the player
	for obstacleXPos in obstaclePositions:
		if obstacleXPos <= PLAYER_X_POS+20:
			return True
	return False
	
def jump():
	PLAYER_Y_POS_CHANGE = -1*POS_CHANGE_GRANULARITY

while not gameExit:
#while True:

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

	# only when the player is stationary
	if PLAYER_Y_POS_CHANGE == 0:
		# take a screen shot
		IMG_SIZE = 100
		
		imgdata = pygame.surfarray.array3d(windowSurface)
		imgdata.swapaxes(0,1)
		
		frame = cv2.cvtColor(imgdata, cv2.COLOR_BGR2GRAY)
		
		new_array = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))

		(h, w) = new_array.shape[:2] 
		center = (w / 2, h / 2)
		angle270 = 270
		scale = 1.0
		M = cv2.getRotationMatrix2D(center, angle270, scale)
		rotated270 = cv2.warpAffine(new_array, M, (h, w))	

		horizontal_mirror = cv2.flip(rotated270, 1)
		
		test_data_sample = []
		test_data_sample.append(horizontal_mirror)
		
		test_data_sample = tf.keras.utils.normalize(test_data_sample, axis=1)

		# check if it is okay to jump
		predictions = loaded_model.predict(test_data_sample)
		
		jump = False
		if np.argmax(predictions[0]) == 1:
			jump = True		
		else:
			jump = False
		
		# jump
		if jump:
			PLAYER_Y_POS_CHANGE = -1*POS_CHANGE_GRANULARITY
			#print('jump')
	
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [PLAYER_X_POS,PLAYER_Y_POS, PLAYER_WIDTH, PLAYER_HEIGHT])	
	drawObstacles()
	pygame.display.update()
	iterationCOunt += 1

	clock.tick(FRAME_RATE)
	
pygame.quit()
quit()