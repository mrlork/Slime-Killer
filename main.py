import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Idle Game For Epic People')
clock = pygame.time.Clock()

font = pygame.font.Font('font.ttf',40)	
x = 50
y = 50
value = 0
value1 = 0
click = False
score = 0
button = pygame.image.load("slug_anim_f0.png")
button_rect = pygame.Rect(50, 50, 150, 150)
button = pygame.transform.scale_by(button,7)
run = True
mouse_was_down = False
counter = 0
slime_image = [pygame.image.load("slug_anim_f0.png"),pygame.image.load("slug_anim_f1.png"),pygame.image.load("slug_anim_f2.png"),pygame.image.load("slug_anim_f3.png")]
blood_splatter = [pygame.image.load("Blood Splatter/B001.png"),pygame.image.load("Blood Splatter/B002.png"),pygame.image.load("Blood Splatter/B003.png"),pygame.image.load("Blood Splatter/B004.png"),pygame.image.load("Blood Splatter/B005.png"),pygame.image.load("Blood Splatter/B006.png"),pygame.image.load("Blood Splatter/B007.png"),pygame.image.load("Blood Splatter/B008.png"),pygame.image.load("Blood Splatter/B009.png"),pygame.image.load("Blood Splatter/B010.png")]
hit = False

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


	mousepoint = pygame.mouse.get_pos()
	if event.type == pygame.MOUSEBUTTONUP:
		mouse_was_down = False

	mouse_down = pygame.mouse.get_pressed()[0]

	if mouse_down and not mouse_was_down:
		if button_rect.collidepoint(mousepoint):
			score += 1
			print("Button clicked! Counter:", score)
			hit = True
		mouse_was_down = True

	if value >= len(slime_image):
		value = 0
	image = slime_image[value]
	image_rect = image.get_rect(midbottom=(y, x))
	image = pygame.transform.scale_by(image, 6)

	if hit:
		if value1 < len(blood_splatter):
			blood = blood_splatter[value1]
			screen.blit(blood, (mousepoint[0] - 25, mousepoint[1]))
			value1 += 1
		else:
			value1 = 0
			hit = False

	screen.fill((0, 0, 0))
	screen.blit(image, (x, y))

	if hit and value1 < len(blood_splatter):
		screen.blit(blood, (mousepoint[0] - 25, mousepoint[1]))
	
	score_message = font.render(f'Slime: {score}',False,(255,255,255))
	screen.blit(score_message,(25,25))

	pygame.display.update()
	clock.tick(60)

	if counter == 10:
		value += 1
		counter = 0
	else:
		counter += 1