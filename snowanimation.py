"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (750, 500)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("mount.jpg")


pygame.display.set_caption("Snow")


# Your SnowFlake class
class Snowflake:
	def __init__(self, x, y, speed, rad):
		self.x = x
		self.y = y
		self.speed = speed
		self.rad = rad
	
	def fall(self, screen, color, width, height):
		
		color = WHITE
		self.speed = random.randint(1,2)
		self.y += self.speed
		pygame.draw.circle(screen, WHITE, [self.x, self.y], self.rad)
		
		if self.y > 500:
			self.y = random.randint(-40,-10)
			self.x = random.randint(0, 750)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

# Snow List
snow_list = []

for i in range(random.randint(400,700)):
	x = random.randint(0,750)
	y = random.randint(0, 500)
	rad = random.randint(2,6)
	snow1 = Snowflake(x, y, speed, rad)
	snow_list.append(snow1)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(bg, (0, 0))


    # --- Drawing code should go here
    # Begin Snow
    for j in snow_list:
    	j.fall(screen, WHITE, 750, 500)
    
    	
    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
