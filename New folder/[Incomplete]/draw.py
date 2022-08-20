import pygame as py

plyr_x = 0
plyr_y = 0
x = 0
y = 0

window = py.display.set_mode((1000,400))

window.fill((200,50,255))    

clrr = (200, 50, 100)

py.init()

run = True
while run:
    plyr_x = py.mouse.get_pos()[0] - 25
    plyr_y = py.mouse.get_pos()[1] - 25
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        
        if event.type == py.KEYDOWN:
            if event.key == py.K_u:
                clrr = (200,50,255)

            if event.key == py.K_LEFT:
                x = -0.4

            if event.key == py.K_RIGHT:
                x = 0.4

            if event.key == py.K_UP:
                y = -0.4

            if event.key == py.K_DOWN:
                y = 0.4

            if event.key == py.K_r:
                window.fill((200,50,255))                    

        if event.type == py.KEYUP:
            if event.key == py.K_u:
                pass

            if event.key == py.K_LEFT:
                x = 0

            if event.key == py.K_RIGHT:
                x = 0

            if event.key == py.K_UP:
                y = 0

            if event.key == py.K_DOWN:
                y = 0

    #window.fill((200,50,255))
    py.draw.rect(window, clrr, (plyr_x, plyr_y, 50, 50))
    py.display.update()
    plyr_x = abs(plyr_x + x)
    plyr_y = abs(plyr_y + y)

    if plyr_x >= 960:
        plyr_x = 960

    if plyr_y >= 360:
        plyr_y = 360