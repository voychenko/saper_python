import pygame
from pygame.locals import *
import random
RESOLUTION_IMAGE=20
CELLSX=3
CELLSY=3
BOMBCOUNT=4
DISPLAYWIDTH=600
DISPLAYHEIGHT=400
img={"close":"closed.png","0":"numbers0.png","1":"numbers1.png","2":"numbers2.png","3":"numbers3.png","4":"numbers4.png","9":"bomb.png","flag":"flag.png"}


#im0 = pygame.image.load("images//"+img[0])
#im1 = pygame.image.load("images//"+img[1])

class cellsmine(object):
	"""dx,y,currentstate tring for cellsmine"""
	def __init__(self,dis, x,y):
		self.x = x
		self.y = y
		self.currentstate=20 # close image 21 open umage  22 marked flag
		self.disp=dis
		self.choosenmark=0
		self.cells_show()
		
	def onclick(self,x,y):

		if (x>self.x and x<(self.x+RESOLUTION_IMAGE) ) and\
		(y>self.y and y<(self.y+RESOLUTION_IMAGE) ):
			print (self)
			print (self.currentstate)
			print (self.choosenmark)
			if self.currentstate==20: # cells close
				self.currentstate=21 # mark open cells
				if self.choosenmark<9:
					self.cells_show()
					return False
				if self.choosenmark==9:
					print ("Bomb")
					self.cells_show()
					return True
			if self.currentstate==21:
				return False

	def onrightclick(self,x,y):
		if (x>self.x and x<(self.x+RESOLUTION_IMAGE) ) and\
		(y>self.y and y<(self.y+RESOLUTION_IMAGE) ):
			if self.currentstate==20:
				self.currentstate=22
				self.cells_show()
			elif self.currentstate==22:
				self.currentstate=20
				self.cells_show()



	def cells_show(self):
		if self.currentstate==21:
			print("showbomb")
			self.disp.blit(pygame.image.load("images//"+img[str(self.choosenmark)]),(self.x,self.y))
		if self.currentstate==20:
			self.disp.blit(pygame.image.load("images//"+img["close"]),(self.x,self.y))
		if self.currentstate==22:
			print("flag")
			self.disp.blit(pygame.image.load("images//"+img["flag"]),(self.x,self.y))


	def setmark_choosen(self,mark):
		self.choosenmark=mark
	def setx_choosen(self,x):
		self.x=x
	def sety_choosen(self,y):
		self.y=y
	def __str__(self):
		return (str(self.x)+" "+str(self.y))




def game():
	pygame.init()

 	dis = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
 	pygame.display.set_caption('Find bomb')
	
	
	mass_array = [[cellsmine(dis,0,0) for i in range(0,CELLSX)] for i2 in range(0,CELLSY)]  

	#forming full cells field
	for i in range(0, CELLSX):
		for i2 in range(0, CELLSY):
			mass_array[i][i2].setx_choosen(i*RESOLUTION_IMAGE)
			mass_array[i][i2].sety_choosen(i2*RESOLUTION_IMAGE)   #=cellsmine(dis,i*RESOLUTION_IMAGE,i2*RESOLUTION_IMAGE)
			mass_array[i][i2].currentstate=20
			mass_array[i][i2].cells_show()
	print("__________________")
	# forming set with unical random number for bombs
	count_mine=0
	while count_mine<(BOMBCOUNT):
		i=random.randint(0,CELLSX-1)
		i2=random.randint(0,CELLSY-1)
		if (mass_array[i][i2].choosenmark!=9):
			mass_array[i][i2].choosenmark=9
			mass_array[i][i2].cells_show()
			count_mine+=1
 	pygame.display.flip()
 	game_over=False
	while not game_over:
		for event in pygame.event.get():
		#	print(event)   #prints out all the actions that take place on the screen
 			pygame.display.update()

 			if pygame.mouse.get_pressed()[0]:
 				clickpos= pygame.mouse.get_pos()
 				print (clickpos)
				for i in range(0, CELLSX):
					for i2 in range(0, CELLSY):
						mass_array[i][i2].onclick(clickpos[0],clickpos[1])
 			if pygame.mouse.get_pressed()[2]:
 				clickpos= pygame.mouse.get_pos()
 				print (clickpos)
				for i in range(0, CELLSX):
					for i2 in range(0, CELLSY):
						mass_array[i][i2].onrightclick(clickpos[0],clickpos[1])

 			if event.type==pygame.QUIT:
 				game_over=True

 	pygame.quit()
 	quit()




if __name__ == '__main__':
	game()

