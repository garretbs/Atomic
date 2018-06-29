import pygame
from pygame.locals import *


def main():
	pygame.init()
	size = 640, 480
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Screensaver")
	bg = pygame.Surface(size)
	bg = bg = bg.convert()
	bg.fill((0, 0, 0))
	
	bsize = 16
	sx = sy = 4.0
	#sy = 0
	x = y = 48
	#r = pygame.Rect(0, 0, bsize, bsize)
	box = pygame.Surface((bsize, bsize))
	fcolor = (255, 255, 255)
	box.fill(fcolor)
	
	fps = 60.0
	frametime = int(1000.0/fps) #in milliseconds
	time_since_update = 0.0
	tick = fps/1000.0
	clock = pygame.time.Clock()
	
	sx *= fps
	sy *= fps
	
	#todo: more advanced. separate physics from frame rate. find better way to limit frame rate. interpolate between frames
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == MOUSEBUTTONDOWN:
					#print('called')
					x = 48
					y = 48
					#box.move(-box.x, -box.y)
					pygame.event.clear() #don't want queued clicks building up			
		
		time_since_update = (clock.tick(fps))/1000.0
		x += sx * time_since_update
		y += sy * time_since_update
		#box = box.move(sx, sy)		
		
		#print(time_since_update)
		
		if x + bsize >= size[0] or x <= 0:
			sx *= -1
		if y + bsize >= size[1] or y <= 0:
			sy *= -1
		
		screen.blit(bg, (0,0))
		screen.blit(box, (x, y))
		#pygame.draw.rect(screen, fcolor, box)
		pygame.display.flip()
		#pygame.time.delay(frametime)

if __name__ == '__main__': main()