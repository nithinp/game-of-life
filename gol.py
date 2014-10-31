
########################################################################
#                                                                      #
#                      Nithin's Game of Life!!                         #
#                                                                      #
#                                                                      #
# CREATED BY    :    Nithin.P                                          #
#                    nithup123@gmail.com                               #
#                    http://facebook.com/nithin.nithinp                #
#                                                                      #
# Description   :    This is my version of world famous Conway's       #
#                    Game of Life I coded this in python using pygame  #
#                    module. I used my own logic to create this.       #
#                                                                      #
# License       :    This Source Code is free to use                   #
#                    for educational purpose only.                     #
#                                                                      #
# Instructions  :    Mouse click on the small cels to select an        #
#                    initial configuration                             #
#		     Press 'S' to start the simulation                 #
#		     Press 'S' again to stop the simulation            #
#		     Press 'r' to reset the screen.                    #
#		     Create nice patterns and watch  ho it simulates   #
#                                                                      #
########################################################################



import pygame
import sys

# Initial Conditions.

white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
gray=(128,128,128)
size=[1000,650]
new_initial_pattern=True
# Array to represent screen
game=[ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ]
start_simulation=False
time_limit=200
time1=pygame.time.get_ticks()
generations=0
alive=0
dead=0







# Function to reset screen.

def reset() :
	global new_initial_pattern
	global start_simulation
	global time1
	global generations
	global alive
	global dead
	new_initial_pattern=True
	start_simulation=False
	time1=pygame.time.get_ticks()
	generations=0
	alive=0
	dead=0
	for i in range(20) :
		for j in range(40) :
			game[i][j]=0









# Function for simulation.

def simulate() :
	global time1
	global generations
	global alive
	global dead
	if pygame.time.get_ticks() > (time1+200) :
		game1=[]
		for i in range(20) :
			tt=[]
			for j in range(40) :
				tt.append(0)
			game1.append(tt)
		for i in range(20) :
			for j in range(40) :
				live_neighbours=0
				if (i-1)>=0 and (j-1)>=0 and (i+1)<20 and (j+1)<40 :
					if game[i-1][j-1]==1 :
						live_neighbours+=1
					if game[i-1][j]==1 :
						live_neighbours+=1
					if game[i-1][j+1]==1 :
						live_neighbours+=1
					if game[i][j-1]==1 :
						live_neighbours+=1
					if game[i][j+1]==1 :
						live_neighbours+=1
					if game[i+1][j-1]==1 :
						live_neighbours+=1
					if game[i+1][j]==1 :
						live_neighbours+=1
					if game[i+1][j+1]==1 :
						live_neighbours+=1
				if game[i][j]==1 :
					if live_neighbours<2 :
						game1[i][j]=0
					if live_neighbours>3 :
						game1[i][j]=0
					if live_neighbours==2 or live_neighbours==3 :
						game1[i][j]=1
				if game[i][j]==0 :
					if live_neighbours==3 :
						game1[i][j]=1
					else :
						game1[i][j]=0
		alive=0
		for i in range(20) :
			for j in range(40) :
				game[i][j]=game1[i][j]
				if game[i][j] :
					alive+=1
		dead=800-alive
		generations+=1
		time1=pygame.time.get_ticks()






# Function to set pattern.

def set_pattern(cord) :
	if cord[1]>=(size[1]-100) or cord[1]<50 :
		return
	xx=0
	while xx<size[0] :
		if cord[0]>=xx and cord[0]<(xx+25) :
			j=xx/25
			break
		xx+=25
	yy=50
	while yy<(size[1]-100) :
		if cord[1]>=yy and cord[1]<(yy+25) :
			i=(yy/25)-2
			break
		yy+=25
	if game[i][j]==0 :
		game[i][j]=1
	else :
		game[i][j]=0





# Function to draw Screen.

def draw_screen() :
	screen.fill(white)
	i=0
	while i<(size[0]) :
		pygame.draw.line(screen,gray,(i,50),(i,size[1]-100))
		i+=25
	i=50
	while i<=(size[1]-100) :
		pygame.draw.line(screen,gray,(0,i),(size[0],i))
		i+=25
	font=pygame.font.Font(None,30)
	generations1='Generations : '+str(generations)
	generationsText=font.render(generations1,True,black)
	generationsRect=generationsText.get_rect()
	generationsRect.centerx=100
	generationsRect.centery=size[1]-25
	screen.blit(generationsText,generationsRect)

	alive1='Alive : '+str(alive)
	aliveText=font.render(alive1,True,black)
	aliveRect=aliveText.get_rect()
	aliveRect.centerx=int(size[0]/2)
	aliveRect.centery=size[1]-25
	screen.blit(aliveText,aliveRect)

	dead1='Dead : '+str(dead)
	deadText=font.render(dead1,True,black)
	deadRect=deadText.get_rect()
	deadRect.centerx=size[0]-100
	deadRect.centery=size[1]-25
	screen.blit(deadText,deadRect)

	instr="Mouse click to select initial configuration.Press 's' to start/stop simulation or 'r' to reset the screen."
	instrText=font.render(instr,True,black)
	instrRect=instrText.get_rect()
	instrRect.centerx=int(size[0]/2)
	instrRect.centery=size[1]-75
	screen.blit(instrText,instrRect)

	name="Nithin's Game Of Life"
	nameText=font.render(name,True,black)
	nameRect=nameText.get_rect()
	nameRect.centerx=int(size[0]/2)
	nameRect.centery=25
	screen.blit(nameText,nameRect)



# Function to draw pattern.

def draw_pattern() :
	for i in range(20) :
		for j in range(40) :
			if game[i][j]==1 :
				left=(j*25)+1
				up=(i*25)+50+1
				pygame.draw.rect(screen,green,(left,up,24,24))

pygame.init()
screen=pygame.display.set_mode(size,0,32)
pygame.display.set_caption("Nithin's Game Of Life!!!")
# Main game loop
while True :
	for event in pygame.event.get() :
		if event.type==pygame.QUIT :
			sys.exit()
			pygame.quit()
		elif event.type==pygame.MOUSEBUTTONDOWN :
			if new_initial_pattern :
				set_pattern(pygame.mouse.get_pos())
		if event.type == pygame.KEYDOWN :
			if event.key == ord('s') :
				if start_simulation :
					start_simulation=False
				else :
					start_simulation=True
					new_initial_pattern=False
			if event.key == ord('r') :
				reset()

	if start_simulation :
		simulate()
	draw_screen()
	draw_pattern()
	pygame.display.update()
