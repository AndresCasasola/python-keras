
import sys, pygame, random
from neuralNet import neural_net

############### Definitions
white = 255, 255, 255
font = 200, 200, 200
background = 60, 60, 60
black = 0, 0, 0

class SmartSnake():

############### Attributes
	width, height = 600, 450
	score = 0
	speed = (0, 0)	# (X, Y)
	snake = pygame.image.load("images/snake.png")
	snakerect = snake.get_rect()
	food = pygame.image.load("images/diamond2_res.png")
	foodrect = food.get_rect()
	screen = pygame.display.set_mode([width, height])

############### Init class attributes
	def __init__(self, epochs=10, batch_size=10, epsilon=1, gamma=.8):
		self.epochs = epochs
		self.batch_size = batch_size
		self.epsilon = epsilon
		self.gamma = gamma
		#self.model = neural_net([15, 16])
		self.experience = []

############### End screen
	def end_screen(self):
		self.screen.fill(background)
		endTextSurface = self.gameFont.render('- YOU DIED -', 1, font)
		endScoreSurface = self.gameFont.render('Score: ' + str(self.score), 1, font)
		exitButton = pygame.image.load("images/exit_button_black.png")
		exitButtonRect = exitButton.get_rect()
		self.screen.blit(endTextSurface, (self.width/2-(endTextSurface.get_width()/2), self.height/3-(endTextSurface.get_height()/2)))
		self.screen.blit(endScoreSurface, (self.width/2-(endScoreSurface.get_width()/2), self.height/2-(endScoreSurface.get_height()/2)))
		exitButtonRect.move_ip(self.width/2-(exitButtonRect.width/2), self.height/1.2-(exitButtonRect.height/2))
		self.screen.blit(exitButton, exitButtonRect)
		pygame.display.flip()
		# Wait for exit button pressed
		exit = False
		while exit == False:
			pygame.event.wait()
			m1, m2, m3 = pygame.mouse.get_pressed()
			if m1 == True:
				mpos = pygame.mouse.get_pos()
				if exitButtonRect.collidepoint(mpos):
					exit = True

############### Test colission
	def collide(self, snakerect, foodrect):
		if snakerect.colliderect(foodrect):
			return True
		else:
			return False

############### Draw background, snake, food, score and refresh screen
	def draw_screen(self, screen):
		self.screen.fill(background)
		self.screen.blit(self.food, self.foodrect)
		self.screen.blit(self.snake, self.snakerect)
		scoreSurface = self.gameFont.render(str(self.score), 1, font)
		screen.blit(scoreSurface, (30, 30))
		pygame.display.flip()

	def start_game(self):

		# Init pygame
		pygame.init()

		# Change window name and create gameFont
		pygame.display.set_caption("Smart snake")
		self.gameFont = pygame.font.Font("fonts/comic.ttf", 40)

		## Start position and speed
		snake_start_position = [self.width/5, self.height/2]
		food_start_position = [random.randint(25,self.width-25),random.randint(25,self.height-25)]
		start_speed = (1, 0) # X, Y
		self.snakerect.move_ip(snake_start_position)
		self.foodrect.move_ip(food_start_position)
		speed = start_speed		
		
		## Start loop
		run = True
		while run:
			pygame.time.delay(5) # ms
			# Capture events
			for event in pygame.event.get():
				# If QUIT event then exit
				if event.type == pygame.QUIT: run = False
			# Key events
			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
				speed = [0, 0]
			if keys[pygame.K_UP]:
				speed[1] = -1
			if keys[pygame.K_DOWN]:
				speed[1] = 1
			if keys[pygame.K_LEFT]:
				speed[0] = -1
			if keys[pygame.K_RIGHT]:
				speed[0] = 1
		
			if self.collide(self.snakerect, self.foodrect) == True:
				self.score = self.score + 1			
				self.foodrect.move_ip(random.randint(25,self.width-25)-self.foodrect.x,random.randint(25,self.height-25)-self.foodrect.y)

			# Move snake
			self.snakerect = self.snakerect.move(speed)
			# Test frame collisions
			if self.snakerect.left < 0 or self.snakerect.right > self.width:
				run = False
			if self.snakerect.top < 0 or self.snakerect.bottom > self.height:
				run = False
			
			self.draw_screen(self.screen)
			## End loop

		
		## Show end screen when game finish
		self.end_screen()


# Main
snake = SmartSnake()
snake.start_game()
pygame.quit()


