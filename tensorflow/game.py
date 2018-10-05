# youtube thenewboston python game development
# https://youtu.be/OGDJdeiuB5M?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
import pygame

print(pygame.init())

white = (255,255,255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('jumper')
windowSurface = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.update()

gameExit = False

player_x_pos = 300
player_y_pos = 300
player_y_pos_change = 0

clock = pygame.time.Clock()

count = 0
while not gameExit:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
			
				# make the player start going up only if already not doing so
				if player_y_pos_change == 0:
					player_y_pos_change = -5

	# when you have jumped high enough come back
	if player_y_pos == 200:
		player_y_pos_change = 5
	
	# player_y_pos_change > 0 means that the player is coming down
	if player_y_pos_change > 0 and player_y_pos == 300:
		player_y_pos_change = 0
	
	# screen shot
	if player_y_pos_change == 0:
	
		pygame.image.save(windowSurface, "screenshots/screenshot_"+str(count)+".jpeg")
		count += 1

	player_y_pos += player_y_pos_change

	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [player_x_pos,player_y_pos, 10, 30])
	pygame.display.update()

	clock.tick(30)

pygame.quit()
quit()
