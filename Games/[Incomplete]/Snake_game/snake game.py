#snake game
import pygame as py
import random
py.init()
snake_count = 1
snake_size = []
score = 0
left,right,up,down = True, True, True, True

foodx,foody = (20*random.randint(0,500/20)), (20*random.randint(0,500/20))

red = (200, 50, 50)
black = (0, 0, 0)
snakex,x, snakey,y = 40,0,40,0

screen = py.display.set_mode((520,520))

def rect_draw(col, placex, placey):
    global screen
    py.draw.rect(screen, col, (placex, placey, 20, 20))

clock = py.time.Clock()

run = True

font = py.font.SysFont('Arial MS', 30)

def ran():
    return random.randint(0,100)

def load_snake(snake_list):
    for xy in snake_list:
        global screen
        py.draw.rect(screen, (ran(),ran(),ran()), (xy[0], xy[1], 20, 20),4)

while run:
    score_board = font.render("score: "+ str(score), True, red)
    clock.tick(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        if event.type == py.KEYDOWN:
            if left:
                if event.key == py.K_LEFT:
                    y = 0
                    x = -20
                    right, up, down = False, True, True
                
            if right:
                if event.key == py.K_RIGHT:
                    y = 0
                    x = 20
                    left, up, down = False, True, True

            if up:
                if event.key == py.K_UP:
                    y = -20
                    x = 0
                    right, left, down = True, True, False

            if down:    
                if event.key == py.K_DOWN:
                    y = 20
                    x = 0
                    right, left, up = True, True, False

    screen.fill((3, 232, 252))
    #rect_draw((255,255,255), snakex, snakey)
    rect_draw(red, foodx, foody)
    screen.blit(score_board,(380,470))
    
    snakex+=x
    snakey+=y

    snake_head = []
    snake_head.append(snakex)
    snake_head.append(snakey)

    snake_size.append(snake_head)
    
    if len(snake_size) > snake_count:
        del(snake_size[0])
    load_snake(snake_size)

    if snakex == foodx and snakey == foody:
        snake_count+=1
        foodx = (20*random.randint(0,500/20))
        foody = (20*random.randint(0,500/20))
        score += 10

    if snakex >= 520:
        run = False
        
    if snakex <= -20:
        run = False
        
    if snakey >= 520:
        run = False

    if snakey <= -20:
        run = False

    #print(snake_size)
    
    py.display.update()