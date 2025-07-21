import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Idle Game For Epic People')
clock = pygame.time.Clock()
	
x = 50
y = 50
value = 0
click = False
score = 0
button = pygame.image.load("slug_anim_f0.png")
button_rect = pygame.Rect(50, 50, 150, 150)
button = pygame.transform.scale_by(button,7)
run = True
mouse_was_down = False
counter = 0
slime_image = [pygame.image.load("slug_anim_f0.png"),pygame.image.load("slug_anim_f1.png"),pygame.image.load("slug_anim_f2.png"),pygame.image.load("slug_anim_f3.png")]

def load_image(filepath: str):
	return pygame.image.load(filepath)

def load_images(filpaths: list[str]):
	ret = []
	for filepath in filpaths:
		ret.append(load_image(filepath))
	return ret

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
	if event.type == pygame.MOUSEBUTTONUP:
		mouse_was_down = False
	
	mouse_down = pygame.mouse.get_pressed()[0]

	if mouse_down and mouse_was_down == False:
		if button_rect.collidepoint(event.pos):
			score += 1
			print("Button clicked! Counter:", score)
		mouse_was_down = True
	
	if value >= len(slime_image):
		value = 0
	image = slime_image[value]
	
	image_rect = image.get_rect(midbottom = (y,x))
	image = pygame.transform.scale_by(image,6)
	
	if counter == 10:
		value += 1
		counter = 0
	else:
		counter += 1
	screen.blit(image,(x,y))

	pygame.display.update()
		#updates the display surface
	screen.fill((0, 0, 0))
	clock.tick(60)