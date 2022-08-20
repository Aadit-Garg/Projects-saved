import pygame as py
from pygame import mixer
from random import randint
import math as maths
py.init()
py.mixer.init()

obs_x = randint(130,140)
obs_y = randint(-100,100)

obs_x1 = randint(145,155)
obs_y1 = randint(170,200)

obs_x2 = randint(160,170)
obs_y2 = randint(270,300)

play = 0

FPS = 120

music = mixer.music.load("sounds//back.wav")
car_crash = mixer.Sound("sounds//crash.wav")
appre = mixer.Sound("sounds//appre.wav")

frame_x = 500
frame_y = 700
game_x = 70
info_x = 18
info1_x = 86
name_x = 73
over_x = frame_x+10

ss = 0
speed2 = 0
speed = 0
direction = 0
direction_X = 0
po = py.surface

font = py.font.SysFont('Arial MS', 30)
font1 = py.font.SysFont('Comic Sans MS', 50)
font2 = py.font.SysFont('Comic Sans MS', 30)
font3 = py.font.SysFont('Arial MS', 50,"bold")

red = (255,0,0)
blue = (25,25,255)
green = (50,255,50)
white = (255,255,255)

icon = py.image.load('images//car_mania.ico')

frame = py.display.set_mode((frame_x,frame_y))
py.display.set_caption('CAR Mania 1.0')
py.display.set_icon(icon)

plyr_x = 280
plyr_y = frame_y-175
x = 0
y = 0
yy = -700
backx = 0
sc_x = 0
sc_y = 0
var = 0
crash = 0

over = font1.render('GAME OVER', True, red)
info = font.render('(Press Enter to Start or Esc to exit)' , True, green)
info1 = font.render('(Press ← or → to control)' , True, green)
name = font2.render('Developed by Aadit Garg' , True, blue)
game =  font3.render(' CAR MANIA ' , True, blue, red)

img = py.image.load("images//car.png").convert_alpha()
img = py.transform.scale(img,(50,100))

back_img = py.image.load("images//back.png")
back_img = py.transform.scale(back_img,(500,800))

obs = py.image.load('images//crate.png')
obs = py.transform.scale(obs,(50,50))
obs2 = py.image.load('images//crate.png')
obs2 = py.transform.scale(obs2,(50,50))
obs3 = py.image.load('images//car2.png')
obs3 = py.transform.scale(obs3,(50,73))

clock = py.time.Clock()

restart = True

run = True

while run:

	clock.tick(FPS)
	
	for event in py.event.get():

		if event.type == py.QUIT:
			run = False

		if event.type == py.KEYDOWN and event.key == py.K_LEFT:
			x = -direction
			direction += 0.5

		if event.type == py.KEYUP and event.key == py.K_LEFT:
			x = 0
			direction = direction_X

		if event.type == py.KEYDOWN and event.key == py.K_RIGHT:
			x = direction
			direction += 0.5

		if event.type == py.KEYUP and event.key == py.K_RIGHT:
			x = 0
			direction = direction_X


		if event.type == py.KEYDOWN:
			if event.key == py.K_ESCAPE:
				if crash == 1 or var == 0:
					run = False
				if crash == 0:
					crash = 1		

		if restart == True:
			if event.type == py.KEYDOWN and event.key == py.K_RETURN:
				y = -100
				yy = -900
				backx = 0
				ss = 1
				speed = 3
				speed2 = 4
				direction = 4
				direction_X = 4
				sc_x = 0 
				sc_y = 0
				var = 0
				crash = 0
				info_x = frame_x+10
				info1_x = frame_x+10
				name_x = frame_x+10
				over_x = frame_x+10
				game_x = frame_x+10 
				obs_x = randint(50,400)
				obs_y = randint(-200,-50)

				obs_x1 = randint(50,400)
				obs_y1 = randint(-300,-150)		

				obs_x2 = randint(50,400)
				obs_y2 = randint(-400,-250)

				mixer.music.play(-1)
				play = 0
				restart = False

	textsurface = font.render('Score :'+ str(var), True,(55,155,255),(0,0,0))	
	frame.fill((0,0,0))
	frame.blit(back_img,(backx,y))
	frame.blit(back_img,(backx,yy))
	frame.blit(img,(plyr_x,plyr_y))
	frame.blit(obs,(obs_x,obs_y))
	frame.blit(obs2,(obs_x1,obs_y1))
	frame.blit(obs3,(obs_x2,obs_y2))
	frame.blit(textsurface,(sc_x,sc_y))
	frame.blit(info,(info_x ,370))
	frame.blit(info1,(info1_x,410))
	frame.blit(name,(name_x,460))
	frame.blit(over,(over_x,150))
	frame.blit(game,(game_x,100))

	py.display.update()

	plyr_x = plyr_x + x
	y += speed
	yy += speed


	if y >= 700:
		y = yy-800

	if yy >= 700:
		yy = y-800
	
	if plyr_x <= 50:
		plyr_x = 50

	if plyr_x >= 400:
		plyr_x = 400

	if plyr_x == obs_y:
		plyr_y -= 1

	if abs(plyr_x-obs_x) <= 50 and abs(plyr_y-obs_y) <= 50:
		crash = 1

	if abs(plyr_x-obs_x1) <= 50 and abs(plyr_y-obs_y1) <= 50:
		crash = 1

	if abs(plyr_x-obs_x2) <= 50 and abs(plyr_y-obs_y2) <= 70:
		crash = 1

	if obs_y >= 700:
		obs_x = randint(50,400)
		obs_y = randint(-150,-50)
		

	if obs_y1 >= 700:
		obs_x1 = randint(50,400)
		obs_y1 = randint(-300,-200)		

	if obs_y2 >= 700:
		obs_x2 = randint(50,400)
		obs_y2 = randint(-450,-350)		

	if crash == 1:
		play += 1
		ss = 0
		speed = 0
		speed2 = 0
		over_x = 100
		direction = 0
		info_x = 18
		info1_x = 86
		name_x = 73
		sc_x = 180
		sc_y = 250
		mixer.music.pause()
		restart = True
		if play == 1:
			mixer.Sound.play(car_crash)

	obs_y += speed
	obs_y1 += speed
	obs_y2 += speed2
	var += ss

	if var == 500:
		speed = 4
		speed2 = 5
		direction = 5
		direction_X = direction

	if var == 1000:
		speed = 4.5
		speed2 = 5.5
		mixer.Sound.play(appre)
		

	if var == 2000:
		speed = 5
		speed2 = 6
		direction = 6.5
		direction_X = direction
		mixer.Sound.play(appre)

	if var == 5000:
		speed = 6
		speed2 = 7
		direction = 7
		direction_X = direction
		mixer.Sound.play(appre)

	if var == 10000:
		speed = 7
		speed2 = 8
		mixer.Sound.play(appre)

	if var == 15000:
		speed = 7.5
		speed2 = 8.5
		mixer.Sound.play(appre)

	if var == 20000:
		speed = 8
		speed2 = 9
		mixer.Sound.play(appre)
