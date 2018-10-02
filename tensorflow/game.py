# youtube thenewboston python game development
# https://youtu.be/OGDJdeiuB5M?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
import pygame

print(pygame.init())

white = (255,255,255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('jumper')

pygame.display.update()

gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
	gameDisplay.fill(white)
	pygame.draw.rect(gameDisplay, black, [400,300, 10, 30])
	pygame.display.update()

pygame.quit()
quit()
