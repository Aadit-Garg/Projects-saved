import pygame as py
from random import randint
from pygame import mixer

mixer.pre_init(44100, 16, 2, 4096)
py.init()

shot = mixer.Sound(file = 'sound/bulletsound1.ogg')
mixer.music.set_volume(0.7)
# mixer.Sound.set_volume(0.7)
tim = 60
ys = 1
overx = 1500
nouu = True
cou = 0

relod = 1000

bl1 = 0
bl2 = 30
bl3 = 60
bl4 = 90
bl5 = 120

moux = 1000
mouy = 1000

space = 0

num = 0
num2 = 0

obsx = randint(92,758)
obsy = randint(90,251)

lr_ys = 1050
cen_ys = 900

lr_y = -235
cen_y = -250

l_x = -149
r_x = 635
font = py.font.SysFont('Arial MS', 30)

over = font.render('Time Over', True, (250, 50, 50))
over2 = font.render('Press ENTER To Restart', True, (250, 50, 50))

time = py.time.Clock()

py.mouse.set_visible(False)

window = py.display.set_mode((1000,400))
bang = py.image.load("img/bang.png")
bang = py.transform.scale(bang, (80, 80))

bullet = py.image.load("img/bullet.png")
bullet = py.transform.scale(bullet,(40, 70))
relo = font.render('Press R To Relod', True, (250, 50, 50))
run = True
while run:
	time_left = font.render('Time Left: ' + str(tim), True, (250, 50, 50))
	score = font.render('Score: '+ str(num), True, (250, 50, 50))
	hscore = font.render('Highest Score: ' + str(num2), True, (250, 50, 50))
	
	for event in py.event.get():
		if event.type == py.QUIT:
			py.quit()

	if ys == 1:
		mousx = py.mouse.get_pos()[0] - 23
		mousy = py.mouse.get_pos()[1] - 23

		if nouu:
			if (mousx - obsx) <= 55 and (mousy - obsy) <= 121 and event.type == py.MOUSEBUTTONDOWN:
				if (mousx - obsx) >= -22 and (mousy - obsy) >= -18 and event.type == py.MOUSEBUTTONDOWN:
					obsx = randint(92, 758)
					obsy = randint(90, 251)
					abc = randint(1,3)
					num += (abc*10)
					moux = py.mouse.get_pos()[0] - 40
					mouy = py.mouse.get_pos()[1] - 40
					tim += 1
			if cou == 0:
				if event.type == py.MOUSEBUTTONDOWN:
					mixer.Sound.play(shot)
					cou = 1
					moux = py.mouse.get_pos()[0] - 40
					mouy = py.mouse.get_pos()[1] - 40
					if bl4 == 1000:
						bl5 = 1000
						moux = 1000
						mouy = 1000
					if bl3 == 1000:
						bl4 = 1000
					if bl2 == 1000:
						bl3 = 1000
					if bl1 == 1000:
						bl2 = 1000
					if True:
						bl1 = 1000
					obsx = randint(92, 758)
					obsy = randint(90, 251)

			if event.type == py.MOUSEBUTTONUP:
				moux = 1000
				mouy = 1000
				cou = 0
		else:
			if event.type == py.KEYDOWN and event.key == py.K_r:
				bl1 = 0
				bl2 = 30
				bl3 = 60
				bl4 = 90
				bl5 = 120
				nouu = True
	
	l = py.image.load("img/l.png")
	l = py.transform.scale(l,(500,lr_ys))

	r = py.image.load("img/r.png")
	r = py.transform.scale(r,(500,lr_ys))

	cen = py.image.load('img/cen.png')
	cen = py.transform.scale(cen,(8000,cen_ys))
	time.tick(60)

	mous = py.image.load("img/poin.png")

	knoc = py.image.load("img/knock.png")

	window.fill((25,55,25))
	window.blit(cen,(-4630,cen_y))
	window.blit(l,(l_x,lr_y))
	window.blit(r,(r_x,lr_y))
	window.blit(knoc, (obsx, obsy))
	window.blit(mous, (mousx, mousy))
	window.blit(score, (10,	10))
	window.blit(time_left, (800, 10))
	window.blit(over, (overx, 170))
	window.blit(over2, (overx - 100, 200))
	window.blit(bang, (moux, mouy))
	window.blit(bullet, (bl1, 320))
	window.blit(bullet, (bl2, 320))
	window.blit(bullet, (bl3, 320))
	window.blit(bullet, (bl4, 320))
	window.blit(bullet, (bl5, 320))
	window.blit(relo, (relod, 100))
	window.blit(hscore, (420, 10))
	space += 1

	if tim == 0:
		keys = py.key.get_pressed()
		if keys[py.K_RETURN]:
			tim = 60
			ys = 1
			space = 0
			num = 0
			overx = 1500
			py.mouse.set_visible(False)
			bl1 = 0
			bl2 = 30
			bl3 = 60
			bl4 = 90
			bl5 = 120

	#print(mousx, mousy)
	py.display.update()

	if tim != 0:
		if space == 20:
			tim -= 1
			space = 0


	else:
		mousx = 1000
		mousy = 200
		ys = 0
		overx = 400
		py.mouse.set_visible(True)
	if bl5 == 1000:
		nouu = False
	if nouu  == False:
		relod = 400
	else:
		relod = 1000
	if num2 <= num:
		num2 = str(num2)
		num3 = str(num)
		num2 = num3[:]
		num2 = int(num2)
	if tim < 0:
		tim = 0
