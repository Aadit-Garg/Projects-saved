import pygame as pyg
pyg.init()

screen = pyg.display.set_mode((800,600))

run = True

while run:
   for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

        print(event)