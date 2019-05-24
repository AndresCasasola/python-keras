
import sys, pygame, random

# Init pygame
pygame.init()

############### Init environment
# Show 800x600 window
width, height = 400, 300
screen = pygame.display.set_mode([width, height])
# Start mixer with 22050Hz, 2 channels, 16 bit sample size
pygame.mixer.init(frequency=22050, channels=1, size=16, buffer=4096)
s = pygame.mixer.Sound("./sounds/TP_Secret.wav")
# Change window name
pygame.display.set_caption("Snakegame")
gameFont = pygame.font.SysFont("Times New Roman", 30)

############### Variables
snake_start_position = [width/2, height/2]
food_start_position = [random.randint(25,width-25),random.randint(25,height-25)]
start_speed = [1, 0] # X, Y
score=0;
speed = start_speed
white = 255, 255, 255
background = 60, 60, 60
black = 0, 0, 0
snake = pygame.image.load("./images/snake.png")
snakerect = snake.get_rect()
food = pygame.image.load("./images/diamond1.png")
food = pygame.transform.scale(food, (25, 25))
foodrect = food.get_rect()

# Start position
snakerect.move_ip(snake_start_position)
last = foodrect.move_ip(food_start_position)

############### Loop conditions
run = True
stop = False
############### Start loop
while run:
	if stop == True:
		pygame.wait(1*1000) # ms
	pygame.time.delay(5) # ms
	# Capture events
	for event in pygame.event.get():
		# If QUIT event then exit
		if event.type == pygame.QUIT: run = False
############### Key events
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
		speed = [0, 0]
	if keys[pygame.K_UP]:
		speed[1] = -1;
	if keys[pygame.K_DOWN]:
		speed[1] = 1;
	if keys[pygame.K_LEFT]:
		speed[0] = -1;
	if keys[pygame.K_RIGHT]:
		speed[0] = 1;
	if keys[pygame.K_p]:
		if stop == True:
			stop = False
			
############### Test colission
	if snakerect.colliderect(foodrect):
		if colliding == False:
			score = score + 1;
			foodrect.move_ip(random.randint(25,width-25)-foodrect.x,random.randint(25,height-25)-foodrect.y)
			colliding = True
	else:
		colliding = False

	# Move snake
	snakerect = snakerect.move(speed)

	if snakerect.left < 0 or snakerect.right > width:
		run = False
	if snakerect.top < 0 or snakerect.bottom > height:
		run = False

############### Draw background, snake, food, score and refresh screen
	screen.fill(background)
	screen.blit(food, foodrect)
	screen.blit(snake, snakerect)
	scoreSurface = gameFont.render(str(score), 1, white)
	screen.blit(scoreSurface, (30, 30))
	pygame.display.flip()

pygame.quit()


