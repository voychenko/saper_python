import pygame
from pygame.locals import *
import random

img=("close.png","O.png")

def game():
	pygame.init()
	dis_width = 600
	dis_height = 400
 	dis = pygame.display.set_mode((dis_width, dis_height))
 	pygame.display.set_caption('Find bomb')
 	im0 = pygame.image.load(img[0])
 	print(im0)
 	pygame.display.flip()
 	dis.blit(im0,(40,40))
 	game_over=False
	while not game_over:
		for event in pygame.event.get():
		#	print(event)   #prints out all the actions that take place on the screen
 			pygame.display.update()
 			if event.type==pygame.QUIT:
 				game_over=True

 	pygame.quit()
 	quit()




if __name__ == '__main__':
	game()

