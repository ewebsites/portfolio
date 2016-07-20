import pygame
import random
from cityscrollertemp import Scroller

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 127)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
BACKGROUND_COLOR = (0, 24, 72)
FRONT = (48, 24, 96)
MIDDLE = (72, 48, 120)
BACK = (96, 72, 120)
colors = [BLACK, BLUE, GREY]
bg = pygame.image.load("nightstar.jpg")


pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Runner Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Runner
class RunnerSprite(pygame.sprite.Sprite):
	def __init__(self, file):
		super().__init__()
		self.image = pygame.image.load(file)
		self.rect = self.image.get_rect()
	
	def update(self, gspeed):
		self.rect.x -= gspeed
		if self.rect.left < 0:
			self.rect.center = (random.randint(700, 800), random.randint(50, 450))
	
	def update2(self, bspeed):
		self.rect.x += bspeed
		if self.rect.left > SCREEN_WIDTH:
			self.rect.center = (random.randint(-100, 0), random.randint(50, 450))
		

		
#Initialize
score = 0
gspeed = 3
bspeed = 3
level = 1
lives = 5
moreruns = 0
total_score = 0

all_sprites_list = pygame.sprite.Group()

good_sprites = pygame.sprite.Group()

bad_sprites = pygame.sprite.Group()

for i in range(8):
	good1 = RunnerSprite("coin.png")
	good1.rect.x = random.randint(700, 800)
	good1.rect.y = random.randint(50,450)
	good_sprites.add(good1)
	all_sprites_list.add(good1)
	
for i in range(8):
	bad1 = RunnerSprite("skull2.png")
	bad1.rect.x = random.randint(-100, 0)
	bad1.rect.y = random.randint(50,450)
	bad_sprites.add(bad1)
	all_sprites_list.add(bad1)
	
player1 = RunnerSprite("colorwheel.png")
all_sprites_list.add(player1)

front_scroller = Scroller(SCREEN_WIDTH, 650, FRONT, 3, 300, 50)
middle_scroller = Scroller(SCREEN_WIDTH, 650, MIDDLE, 2, 500, 100)
back_scroller = Scroller(SCREEN_WIDTH, 650, BACK, 1, 650, 300)

# -------- MAIN PROGRAM LOOP -----------
while not done:
	# --- MAIN EVENT LOOP --------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# SCREEN CODE: 
	screen.blit(bg, (0,0))
	
	# --- Screen-clearing code goes here

	
	
	# Meat of the Code:
	back_scroller.draw_buildings(screen)
	back_scroller.move_buildings()
	middle_scroller.draw_buildings(screen)
	middle_scroller.move_buildings()
	front_scroller.draw_buildings(screen)
	front_scroller.move_buildings()
	
	mpos = pygame.mouse.get_pos()
	player1.rect.center = mpos
	
	for item in good_sprites:
		item.update(gspeed)
		
	for item in bad_sprites:
		item.update2(bspeed)
		
	good_hit_list = pygame.sprite.spritecollide(player1, good_sprites, True)
	bad_hit_list = pygame.sprite.spritecollide(player1, bad_sprites, True)
	
	for good in good_hit_list:
		score += 1
		good2 = RunnerSprite("coin.png")
		good2.rect.x = random.randint(700, 800)
		good2.rect.y = random.randint(50,450)
		good_sprites.add(good2)
		all_sprites_list.add(good2)
	
	for bad in bad_hit_list:
		score -= 1
		lives -= 1
		bad2 = RunnerSprite("skull2.png")
		bad2.rect.x = random.randint(-100, 0)
		bad2.rect.y = random.randint(50,450)
		bad_sprites.add(bad2)
		all_sprites_list.add(bad2)
	
	all_sprites_list.draw(screen)
	
	font = pygame.font.SysFont('Calibri', 30, True, False)
	text = font.render("Score: " + str(score), True, WHITE)
	screen.blit(text, [575, 25])

	
	font = pygame.font.SysFont('Calibri', 30, True, False)
	text = font.render("Level: " + str(level), True, WHITE)
	screen.blit(text, [10, 25])
	
	font = pygame.font.SysFont('Calibri', 30, True, False)
	text = font.render("Lives left: " + str(lives), True, WHITE)
	screen.blit(text, [250, 25])
	
	if score >= 50:
		font = pygame.font.SysFont('Calibri', 50, True, False)
		text = font.render("Next level!", True, WHITE)
		screen.blit(text, [400, 300])
		
		level += 1
		score = 0
		
		gspeed += 2
		bspeed += 3
	
	if lives <= 0:
	
		total_score = (50*level) + score
		
		font = pygame.font.SysFont('Calibri', 75, True, False)
		text = font.render("YOU LOSE, score = " + str(total_score), True, WHITE)
		screen.blit(text, [10, 250])
		
		moreruns += 1
	
	if moreruns >= 100:
		done = True
		
		
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE