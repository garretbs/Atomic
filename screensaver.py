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
	sx = sy = 4
	sy = 0
	x = y = 48
	#box = pygame.Rect(48, 48, bsize, bsize)
	fcolor = (255, 255, 255)
	
	fps = 60.0
	frametime = int(1000.0/fps) #in milliseconds
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == MOUSEBUTTONDOWN:
					print('called')
					#box.move(-box.x, -box.y)
					pygame.event.clear() #don't want queued clicks building up			
		
		#box = box.move(sx, sy)
		#print(box.y)
		#print(box.y + bsize >= size[1])
		
		x += sx
		y += sy
		
		if x + bsize >= size[0] or x <= 0:
			sy *= -1
		elif y + bsize >= size[1] or y <= 0:
			sx *= -1
		screen.blit(bg, (0,0))
		#pygame.draw.rect(screen, fcolor, box)
		pygame.display.flip()
		pygame.time.delay(frametime)

if __name__ == '__main__': main()