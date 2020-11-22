import pygame
from pygame.locals import *
import random
RESOLUTION_IMAGE=20
CELLSX=3
CELLSY=3
BOMBCOUNT=4
DISPLAYWIDTH=600
DISPLAYHEIGHT=400
img=("close.png","O.png")
im0 = pygame.image.load("images//"+img[0])


class cellsmine(object):
	"""dx,y,currentstate tring for cellsmine"""
	def __init__(self,dis, x,y):
		self.x = x
		self.y = y
		self.currentstate=21 # close image 21 open umage  22 marked flag
		self.disp=dis
		self.cells_show()
		
	def onclick(self,x,y):
		if (x>self.x and x<(self.x+RESOLUTION_IMAGE) ) and\
		(y>self.y and y<(self.y+RESOLUTION_IMAGE) ):
			if self.currentstate==22:
				return False
			if self.currentstate==21:
				if self.choosenmark<9:
					self.currentstate=self.choosenmark
					self.currentstate=22
					return False
				if self.choosenmark==9:
					return True # return flag bomb activated
	def cells_show(self):
		self.disp.blit(im0,(self.x,self.y))




def game():
	pygame.init()

 	dis = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
 	pygame.display.set_caption('Find bomb')
	
	mass_array=[] #cellsmine[CELLSX][CELLSY]
	mass_mine=set([])
	# forming set with unical random number for bombs
	while len(mass_mine)<BOMBCOUNT:
		d=random.randint(0, (CELLSX+1)*(CELLSY+1))
	######################################################### don undestand
		if (d>CELLSX) and ((d+1)%(CELLSX+2)!=0) and (d%(CELLSX+1)!=CELLSX):
			mass_mine.add(d)
	#create freee mass for each cells, add firast+last row and add fist and last column with zero bombs for wase calculate numbers
	for i in range(0, (CELLSX+1)*(CELLSY+1)):
		mass_array.insert(i,0)
		if (i in mass_mine):
			mass_array[i]=23 #bomb

	print (mass_mine)
	print (mass_array)


 	firstcell=cellsmine(dis,40,40)
 	firstcell=cellsmine(dis,80,80)
 	pygame.display.flip()
 	game_over=False
	while not game_over:
		for event in pygame.event.get():
		#	print(event)   #prints out all the actions that take place on the screen
 			pygame.display.update()
 			#print(event)
 			if pygame.mouse.get_pressed()[0]:
 				clickpos= pygame.mouse.get_pos()
 				print (clickpos)
 				firstcell.onclick(clickpos[0],clickpos[1])
 			if event.type==pygame.QUIT:
 				game_over=True

 	pygame.quit()
 	quit()




if __name__ == '__main__':
	game()

