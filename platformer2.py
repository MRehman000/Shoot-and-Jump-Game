#Muhammad Rehman

import pygame
import time
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("Space to Shoot, Arrows to Move")
done = False
score = 0
bullet_list = pygame.sprite.Group()
myfont = pygame.font.Font("arial.ttf",80)
label = myfont.render("GAME OVER",1,(255,255,0))
myfont2 = pygame.font.Font("arial.ttf",30)
label2 = myfont2.render("CONGRATULATIONS, YOU FOUND THE KEY TO SUCCESS",1,(255,255,0))
label3 = myfont2.render("Restart the game for ANOTHER ONE",1,(255,255,0))
start_frame = time.time()

class Background(pygame.sprite.Sprite):
	def __init__(self,x,y,x_pos,y_pos,a,b,c):
		pygame.sprite.Sprite.__init__(self)
		self.surface = pygame.Surface((x,y))
		self.rect = self.surface.get_rect()
		self.rect.x = x_pos
		self.rect.y = y_pos
		self.a = a
		self.b = b
		self.c = c
	def draw(self):
		pygame.draw.rect(screen,(self.a,self.b,self.c),self)
		
bg1 = Background(2048,600,0,0,173,216,230)
bg2 = Background(2048,600,2048,0,170,170,170)
bg3 = Background(2048,600,4096,0,132,132,132)
bg4 = Background(2500,600,6144,0,176,196,222)

def get_animation(x,y,w,h):
	sprites = pygame.image.load("images/soldier.png")
	img = pygame.Surface([w,h])
	img.blit(sprites,(0,0),(x,y,w,h))
	img.set_colorkey((0,0,0))
	return img
	
def get_reverse_img(x,y,w,h):
	image = get_animation(x,y,w,h)
	image = pygame.transform.flip(image, True,False)
	return image
	
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.right_anim = []
		self.right_anim.append(get_animation(0,11,43,55))
		self.right_anim.append(get_animation(118,9,41,58))
		self.right_anim.append(get_animation(168,8,43,59))
		self.right_anim.append(get_animation(214,9,43,58))
		self.right_anim.append(get_animation(263,11,43,55))
		self.right_anim.append(get_animation(316,10,46,57))
		self.right_anim.append(get_animation(372,9,40,58))
		self.right_anim.append(get_animation(422,8,37,59))
		self.right_anim.append(get_animation(466,8,40,59))
		self.right_anim.append(get_animation(510,9,45,58))
		self.right_anim.append(get_animation(569,10,45,57))
		
		self.left_anim = []
		self.left_anim.append(get_reverse_img(0,11,43,55))
		self.left_anim.append(get_reverse_img(118,9,41,58))
		self.left_anim.append(get_reverse_img(168,8,43,59))
		self.left_anim.append(get_reverse_img(214,9,43,58))
		self.left_anim.append(get_reverse_img(263,11,43,55))
		self.left_anim.append(get_reverse_img(316,10,46,57))
		self.left_anim.append(get_reverse_img(372,9,40,58))
		self.left_anim.append(get_reverse_img(422,8,37,59))
		self.left_anim.append(get_reverse_img(466,8,40,59))
		self.left_anim.append(get_reverse_img(510,9,45,58))
		self.left_anim.append(get_reverse_img(569,10,45,57))
		
		self.jump_anim =[]
		self.jump_anim.append(get_animation(10,84,37,56))
		
		self.rev_jump_anim = []
		self.rev_jump_anim.append(get_reverse_img(10,84,37,56))
		
		self.image = self.right_anim[0]
		self.rect = pygame.Rect(100,558,43,55)
		self.dx = 0
		self.dy = 0
		self.last_key_pressed = "RIGHT"
	def jump(self):
		self.rect.y += 2
		plats = pygame.sprite.spritecollide(self,platforms,False)
		self.rect.y -=2
		if len(plats) > 0:
			self.dy = -20
	def move(self):
		if self.dy == 0:
			self.dy = 1
		else:
			self.dy += .4
		self.rect.x += self.dx
		plats = pygame.sprite.spritecollide(self,platforms,False)
		for p in plats:
			if self.dx > 0:
				self.rect.right = p.rect.left
			elif self.dx < 0:
				self.rect.left = p.rect.right
		self.rect.y += self.dy
		plats = pygame.sprite.spritecollide(self,platforms,False)
		for p in plats:
			if self.dy > 0:
				self.rect.bottom = p.rect.top
			elif self.dy < 0:
				self.rect.top = p.rect.bottom
			self.dy = 0
	def update(self):
		pressed = pygame.key.get_pressed()
		self.dx = 0
		if self.dx == 0:
			if self.last_key_pressed == "RIGHT":
				self.image = self.right_anim[0]
			elif self.last_key_pressed == "LEFT":
				self.image = self.left_anim[0]
		current_image = int((time.time() - start_frame)* 15 % 11)
		self.rect.y += 2
		plats = pygame.sprite.spritecollide(self,platforms,False)
		self.rect.y -=2
		if len(plats) == 0:
			if self.last_key_pressed == "RIGHT":
				self.image = self.jump_anim[0]
			elif self.last_key_pressed == "LEFT":
				self.image = self.rev_jump_anim[0]
			if pressed[pygame.K_UP]:
				self.jump()
			if pressed[pygame.K_DOWN]:
				pass
			if pressed[pygame.K_LEFT]:
				self.dx += -3
				self.last_key_pressed = "LEFT"
			if pressed[pygame.K_RIGHT]:
				self.dx += 3
				self.last_key_pressed = "RIGHT"
		else:
			if pressed[pygame.K_UP]:
				self.jump()
			if pressed[pygame.K_DOWN]:
				pass
			if pressed[pygame.K_LEFT]:
				self.dx += -3
				self.image = self.left_anim[current_image]
				self.last_key_pressed = "LEFT"
			if pressed[pygame.K_RIGHT]:
				self.dx += 3
				self.image = self.right_anim[current_image]
				self.last_key_pressed = "RIGHT"
		self.move()
	def shoot(self):
		bullet = Bullet(self.rect.x,self.rect.y)
		bullet.rect.center = player.rect.center
	def draw(self):
		#pygame.draw.rect(screen,(25,25,112),self) #midnight blue	
		screen.blit(self.image,(self.rect.x,self.rect.y),(0,0,64,58))

class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y,dx):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(x,y,11,9)
		self.image = pygame.image.load("images/bullett1.png")
		bullet_list.add(self)
		self.x = dx
	def move(self):
		self.rect.x += self.x
		screen.blit(self.image,(self.rect.x,self.rect.y),(11,10,11,11))
		
class Enemy(pygame.sprite.Sprite):
	def __init__(self,x,y,left,right):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/jellyfish8.png")
		self.rect = pygame.Rect(x,y,31,31)
		self.left_bound = left
		self.right_bound = right
		self.dx = 1
	def move(self):
		self.rect.x += self.dx
		if (self.rect.x - cam_shift) < self.left_bound:
			self.dx = 1
		if (self.rect.x - cam_shift) > self.right_bound:
			self.dx = -1
		screen.blit(self.image,(self.rect.x,self.rect.y),(0,0,32,32))
	def draw(self):
		pass
class Platform(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height,filename,x_pos,y_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = pygame.Rect(x,y,width,height)
		self.x = x_pos
		self.y = y_pos
		self.w = width
		self.h = height
	def draw(self):
		screen.blit(self.image,(self.rect.x,self.rect.y),(self.x,self.y,self.w,self.h))	
class Small_Platform(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/platforms.png")
		self.rect = pygame.Rect(x,y,64,64)
	def draw(self):
		screen.blit(self.image,(self.rect.x,self.rect.y),(256,0,64,64))

class Grassy_Platform(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/platforms.png")
		self.rect = pygame.Rect(x,y,128,64)
	def draw(self):
		screen.blit(self.image,(self.rect.x,self.rect.y),(0,0,128,64))
class Vertical_Moving_Platform(pygame.sprite.Sprite):
	def __init__(self,x,y,dy,top,bottom):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/platforms.png")
		self.rect = pygame.Rect(x,y,64,64)
		self.top_bound = top
		self.bottom_bound = bottom
		self.dy = dy
	def move(self):
		self.rect.y += self.dy
		player_hit = pygame.sprite.collide_rect(self,player)
		if player_hit:
			if self.dy < 0:
				player.rect.bottom = self.rect.top
			else:
				player.rect.top = self.rect.bottom		
		if self.rect.y < self.top_bound:
			self.dy *= -1 
		if self.rect.y > self.bottom_bound:
			self.dy *= -1
	def draw(self):
		screen.blit(self.image,(self.rect.x,self.rect.y),(384,0,64,64))
class Horizontal_Moving_Platform(pygame.sprite.Sprite):
	def __init__(self,x,y,dx,left,right):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/platforms.png")
		self.rect = pygame.Rect(x,y,64,64)
		self.left_bound = left
		self.right_bound = right
		self.dx = dx
	def move(self):
		self.rect.x += self.dx
		player_hit = pygame.sprite.collide_rect(self,player)
		if player_hit:
			if self.dx < 0:
				player.rect.right = self.rect.left
			else:
				player.rect.left = self.rect.right
		if self.rect.x - cam_shift < self.left_bound:
			self.dx *= -1 
		if self.rect.x - cam_shift > self.right_bound:
			self.dx *= -1		
	def draw(self):
		screen.blit(self.image,(self.rect.x,self.rect.y),(384,0,64,64))
class Coin(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/Retro_Coin.png")
		self.rect = pygame.Rect(x,y,32,32)
	def draw(self):
		screen.blit(self.image,(self.rect.x,self.rect.y))

cam_shift = 0
def camera_shift(shift):
	global cam_shift 
	cam_shift += shift
	for p in platforms:
		p.rect.x += shift
	for e in enemies:
		e.rect.x += shift
	for c in coins:
		c.rect.x += shift
	for b in backgrounds:
		b.rect.x += shift
def game_over():
	myfont = pygame.font.Font(None,30)
	label = myfont.render("GAME OVER",1,(255,255,0)) 
	screen.blit(label,(512,300))
player_list = pygame.sprite.Group()
coins = pygame.sprite.Group()
moving_plats = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
backgrounds = []
backgrounds.append(bg1)
backgrounds.append(bg2)
backgrounds.append(bg3)
backgrounds.append(bg4)

#Left Vertical Wall
y = 578
for i in range(12):
	platforms.add(Small_Platform(0,y))
	y-=64
#Bottom Wall
x = 0
for i in range(12):
	platforms.add(Grassy_Platform(x,578))
	x+=64
#Continue Bottom wall	
x = 1000
for i in range(7):
	platforms.add(Grassy_Platform(x,578))
	x+=64
#Mid game vertical wall
y = 578
for i in range(5):
	platforms.add(Platform(784,y,64,64,"images/platforms.png",192,0))
	y-=64

#Beginning Platforms	
#Two Grassy Platform and bottom roots
platforms.add(Grassy_Platform(300,450))		
platforms.add(Grassy_Platform(540,350))		
platforms.add(Platform(363,514,62,64,"images/platforms.png",0,64))
platforms.add(Platform(301,514,62,64,"images/platforms.png",384,384))
platforms.add(Platform(603,414,62,64,"images/platforms.png",0,64))
platforms.add(Platform(541,414,62,64,"images/platforms.png",384,384))
#vertical platform after mid game vert wall
p5 = Vertical_Moving_Platform(900,300,1,200,500)
#platform with monster on top
p6 = Horizontal_Moving_Platform(100,375,1,90,150)
platforms.add(p5)
platforms.add(p6)
moving_plats.add(p5)
moving_plats.add(p6)


#Stair1
x = 1508
for i in range(41):
	platforms.add(Small_Platform(x,546))
	x+=64
#Stair2
x = 1640
for i in range(38):
	platforms.add(Small_Platform(x,482))
	x+=64
#Stair3
x = 1768
for i in range(35):
	platforms.add(Small_Platform(x,418))
	x+=64
#Stair4
x = 1888
for i in range(30):
	platforms.add(Small_Platform(x,354))
	x+=64
#Cave Entrance
x = 2048
for i in range(33):
	platforms.add(Platform(x,0,64,64,"images/platforms.png", 384,64))
	x+= 64
#Cave Entrance Platforms
platforms.add(Platform(2112,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(2176,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(2432,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(2944,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(2240,64,128,64,"images/platforms.png",384,384))
platforms.add(Platform(2560,64,128,64,"images/platforms.png",384,384))
platforms.add(Platform(2250,290,192,64,"images/platforms.png",128,256))
platforms.add(Platform(2800,290,64,128,"images/platforms.png",128,64))
platforms.add(Platform(2700,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(3100,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(3300,64,128,64,"images/platforms.png",384,384))
platforms.add(Platform(3600,64,128,64,"images/platforms.png",384,384))
platforms.add(Platform(3500,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(3900,64,64,64,"images/platforms.png",448,128))
platforms.add(Platform(3980,64,128,64,"images/platforms.png",384,384))




x = 190
for i in range(4):
	coins.add(Coin(x,543))
	x += 32
y = 200
for i in range(6):
	coins.add(Coin(900,y))
	y-=32
x = 1900
for i in range(8):
	coins.add(Coin(x,322))
	x += 40
enemies.add(Enemy(500,533,490,600))              
enemies.add(Enemy(1200,533,1110,1400))
enemies.add(Enemy(100,343,90,150))
enemies.add(Enemy(540,310,540,600))
enemies.add(Enemy(1800,370,1768,1850))
x = 2550
for i in range(3):
	enemies.add(Enemy(x,305,x-100,x+100))
	x+= 50
y = 305
for i in range(6):
	enemies.add(Enemy(3200,y,3100,3300))
	coins.add(Coin(3250,y))
	coins.add(Coin(3400,y))
	y-=32
#Cave Platforms
p7 = Vertical_Moving_Platform(4100,450,1,200,451)
platforms.add(Grassy_Platform(4500,300))
platforms.add(Grassy_Platform(4700,300))
p9 = Vertical_Moving_Platform(4900,400,1,200,550)
platforms.add(Grassy_Platform(4300,300))
platforms.add(Platform(4363,364,62,64,"images/platforms.png",0,64))
platforms.add(Platform(4301,364,62,64,"images/platforms.png",384,384))
platforms.add(Grassy_Platform(5050,500))
platforms.add(Grassy_Platform(5250,400))
platforms.add(Grassy_Platform(5450,300))
platforms.add(Grassy_Platform(5650,200))
platforms.add(Grassy_Platform(5850,300))
platforms.add(Grassy_Platform(6050,400))
enemies.add(Enemy(4550,257,4500,4600))
platforms.add(p7)
moving_plats.add(p7)

#Outisde Cave
x=6250
for i in range(30):
	platforms.add(Grassy_Platform(x,500))
	platforms.add(Small_Platform(x,564))
	platforms.add(Small_Platform(x+6250,564))
	x+=64
y = 450
for i in range(6):
	enemies.add(Enemy(6500,y,6450,6800))
	enemies.add(Enemy(6550,y,6500,6850))
	enemies.add(Enemy(6600,y,6550,6900))
	enemies.add(Enemy(6650,y,6600,6950))
	enemies.add(Enemy(6700,y,6650,7000))
	enemies.add(Enemy(6750,y,6700,7050))
	y-=32
y=578
for i in range(12):
	platforms.add(Small_Platform(8200,y))
	y-=64
platforms.add(p9)
moving_plats.add(p9)
key = pygame.image.load("images/key.png")
dj = pygame.image.load("images/imgg.jpg")
player = Player() 
player_list.add(player)
while not done:
	for b in backgrounds:
		b.draw()
	game_is_over = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if player.last_key_pressed == "RIGHT":
					bullet = Bullet((player.rect.x+39),(player.rect.y+4), 6)
				if player.last_key_pressed == "LEFT":
					bullet = Bullet(player.rect.x+12,player.rect.y+4, -6)
	#Bullet draw
	for x in bullet_list:
		x.move()
	#Bullet interacts with Enemies
	for x in bullet_list:
		block_hit = pygame.sprite.spritecollide(x,enemies,True)
		for block in block_hit:
			bullet_list.remove(x)
	#Bullet interacts with platforms		
	for x in bullet_list:
		block_hit = pygame.sprite.spritecollide(x,platforms,False)
		for block in block_hit:
			bullet_list.remove(x)
	#Camera Shift
	if player.rect.right >= 800:
		x_shift = player.rect.right - 800
		player.rect.right = 800
		camera_shift(-x_shift)
	if player.rect.left <= 200:
		x_shift = 200 - player.rect.left
		player.rect.left = 200
		camera_shift(x_shift)
	# Game Over Situations
	coin_hit = pygame.sprite.spritecollide(player,coins,True)
	if len(coin_hit) > 0:
		score += 1
		print (score)
	player_hit = pygame.sprite.spritecollide(player,enemies,True)
	if len(player_hit) > 0:
		game_is_over = True
	if player.rect.y >= 568:
		game_is_over = True
	while game_is_over:
		screen.blit(label,(400,300))
		pygame.display.flip()
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_is_over = False
				done = True
	#Movement
	player.update()
	#Drawing everything
	player.draw()
	for p in platforms:
		p.draw()
	for m in moving_plats:
		m.move()
	for e in enemies:
		e.move()
		e.draw()
	for c in coins:
		c.draw()
	screen.blit(key,(7200+cam_shift,300))
	screen.blit(label2,(7200+cam_shift,350))
	screen.blit(dj,(7700+cam_shift,0))
	screen.blit(label3,(7200+cam_shift,250))
	#Window Settings
	pygame.display.flip()
	clock.tick(60)