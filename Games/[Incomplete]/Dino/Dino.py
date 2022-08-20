import pygame as py
from random import randint

py.init()
neg = 0
y = 0

yes = 0
ye = 0

obs_x = 450
obs_y = 336
obs_y2 = 330

obx = randint(1000,1200)
obx2 = randint(1400,1600)
obx3 = randint(1800,2000)

speed = 0
count = 0
counter = 0

time = py.time.Clock()

bg_x = 0
bg2_x = 999

jump = True
jumpcount = 0
plyr_y = 310
plyr_x = 40

window = py.display.set_mode((999,500))
bg = py.image.load("img/back.png")
bg = py.transform.scale(bg,(999,500))
bg2 = py.image.load("img/back.png")
bg2 = py.transform.scale(bg2,(999,500))
move = py.image.load('img/dino1.png')
move = py.transform.scale(move,(200,190))
obs1 = py.image.load('img/obs.png')
obs1 = py.transform.scale(obs1,(200,180))
obs2 = py.image.load('img/obs.png')
obs2 = py.transform.scale(obs2,(150,250))
obs3 = py.image.load('img/obs.png')
obs3 = py.transform.scale(obs2,(250,180))



run = True
while run:
	if count == 10:
		move = py.image.load('img/dino1.png')
		move = py.transform.scale(move,(200,190))
		count = 10

	time.tick(40)
	#py.time.delay(50)
	for event in py.event.get():
		if event.type == py.QUIT:
			run = False

		if event.type == py.KEYDOWN and event.key == py.K_RETURN:
			speed = 8
			jumpcount = 10
			ye = 1
			jump = False
			neg = 1
			counter = 2

	keys = py.key.get_pressed()

	if jump == False:
		if keys[py.K_SPACE]:
			jump = True
			count = 1
			yes = ye

	if yes == 1:
		if jumpcount > -11:
			y = abs(jumpcount**2)*neg*0.7
			jumpcount -= 1
			plyr_x += 5
			if count == 9:
				move = py.image.load('img/jump.png')
				move = py.transform.scale(move,(200,190))
			
			if count == 13:
				move = py.image.load('img/jump2.png')
				move = py.transform.scale(move,(200,190))
				count = 1

			
			if jumpcount == 0:
				neg = -1
		else:
			jump = False
			jumpcount = 10
			neg = 1
			y = 0
			yes = 0
			move = py.image.load('img/dino2.png')
			move = py.transform.scale(move,(200,190))
			count = 0


	plyr_y -= y

	bg_x -= speed
	bg2_x -= speed
	obx -= speed
	obx2 -= speed
	obx3 -= speed
	count += counter
	window.fill((220,220,220))
	window.blit(bg,(bg_x,0))
	window.blit(bg2,(bg2_x,0))
	window.blit(obs1,(obx,obs_y))
	window.blit(move,(plyr_x,plyr_y))
	window.blit(obs2,(obx2,obs_y2))
	window.blit(obs3,(obx3,obs_y))
	line = py.draw.rect(window,(100,70,80),(0,440,1000,100))

	if bg_x <= -999:
		bg_x = 999 - speed -1

	if bg2_x <= -999:
		bg2_x = 999 - speed -2

	if jumpcount == 10:
		plyr_x -= 5 

	if plyr_x <= 39:
		plyr_x = 39

	if plyr_x >= 143:
		plyr_x = 143

	if obx <= -200:
		obx = randint(1000,1200)
	if obx2 <= -200:
		obx2 = randint(1500,1700)
	if obx3 <= -200:
		obx3 = randint(2000,2200)

	if count == 20:
		move = py.image.load('img/dino2.png')
		move = py.transform.scale(move,(200,190))
		count = 0

	if abs(plyr_x-obx) <= 80 and abs(plyr_y-obs_y) <= 100:
		if obx+40 < plyr_x:
			run = True
		else:
			run = False

	if abs(plyr_x-obx2) <= 80 and abs(plyr_y-obs_y2) <= 100:
		if obx2+20 < plyr_x:
			run = True
		else:
			run = False

	if abs(plyr_x-obx3) <= 60 and abs(plyr_y-obs_y) <= 100:
		if obx3+40 < plyr_x:
			run = True
		else:
			run = False

	py.display.update()