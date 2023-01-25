from colorama import Back as B
from colorama import Fore as F
from colorama import Style as S

import random as rndm
DEBUG = False
SIZE = 5
BOMB = int(SIZE*1.7)  
CLIS = {6:"",7:"",8:"",0:B.LIGHTWHITE_EX,1:B.CYAN,2:B.MAGENTA,3:B.LIGHTRED_EX,4:B.YELLOW,5:B.GREEN,"r":S.RESET_ALL, "@":F.RED}

lis = [[" " for _ in range(SIZE)] for _ in range(SIZE)]
if DEBUG:
    print(*lis, sep="\n\n")

def check(x,y,hlis,nclis):
    Left,Right,Up,Down = True,True,True,True
    
    if x>0 and nclis[y][x-1] != "@" and hlis[y+1][x] == "#":
        hlis[y+1][x] = lis[y][x-1]
        # check(x-1,y,hlis,nclis)
    else:Left = False
    if x<SIZE-1 and nclis[y][x+1] != "@" and hlis[y+1][x+2] == "#":
        hlis[y+1][x+2] = lis[y][x+1]
        # check(x+1,y,hlis,nclis)
    else: Right = True
    if y>0:
        
        if nclis[y-1][x] != "@" and hlis[y][x+1] == "#":
            hlis[y][x+1] = lis[y-1][x]
            # check(y-1,x,hlis,nclis)
        else: Up=False
        if Up:
            if x>0 and nclis[y-1][x-1] != "@" and Left and hlis[y][x] == "#":
                hlis[y][x] = lis[y-1][x-1]
                check(y-1,x-1,hlis,nclis)
            if  x<SIZE-1 and nclis[y-1][x+1] != "@"and Right and hlis[y][x+2] == "#":
                hlis[y][x+2] = lis[y-1][x+1]
                check(y-1,x+1,hlis,nclis)

    if y<SIZE-1:
        
        if nclis[y+1][x] != "@" and hlis[y+2][x+1] == "#":
            hlis[y+2][x+1] = lis[y+1][x]
            # check(y+1,x,hlis,nclis)
        else: Down = False
        if Down:
            if x>0 and nclis[y+1][x-1] != "@"  and Left and hlis[y+2][x] == "#":
                hlis[y+2][x] = lis[y+1][x-1]
                check(y+1,x-1,hlis,nclis)
            if x<SIZE-1 and nclis[y+1][x+1] != "@"  and Right and hlis[y+2][x+2] == "#":
                hlis[y+2][x+2] = lis[y+1][x+1]
                check(y+1,x+1,hlis,nclis)
    return hlis
def fvalue(x,y,c,lis):
    ret = 0
    if y>0:
        
        if x>0 and lis[y-1][x-1] == "@":
            ret+=1
        if lis[y-1][x] == "@":
            ret+=1
        if  x<SIZE-1 and lis[y-1][x+1] == "@":
            ret+=1

    if x>0 and lis[y][x-1] == "@":
        ret+=1
    if x<SIZE-1 and lis[y][x+1] == "@":
        ret+=1

    if y<SIZE-1:
        if x>0 and lis[y+1][x-1] == "@":
            ret+=1
        if lis[y+1][x] == "@":
            ret+=1
        if x<SIZE-1 and lis[y+1][x+1] == "@":
            ret+=1
    if lis[y][x] == "@":
        ret = "@"
    
    if c:
        return (CLIS[ret]+str(ret)+CLIS["r"])
    else: return (str(ret))

choosex,choosey = [i for i in range(SIZE)], [i for i in range(SIZE)]
coord = []

for i in range(BOMB):
    while True:
        x,y = rndm.choice(choosex), rndm.choice(choosey)
        if [x,y] not in coord:
            break
    coord.append([x,y])
    lis[y][x] = "@"

mynewlis = [[i for i in range(SIZE)] for x in range(SIZE)]


# print(*mynewlis, sep="\n\n")

if DEBUG:
    print(*lis, sep="\n\n")

for y in range(SIZE):
    for x in range(SIZE):
        if lis[y][x] != "@":
            lis[y][x] = fvalue(x,y,True,lis)

for y in range(SIZE):
    for x in range(SIZE):
        if mynewlis[y][x] != "@":
            mynewlis[y][x] = fvalue(x,y,False,lis)

for y in range(SIZE):
    for x in range(SIZE):
        if lis[y][x] == "@":
            lis[y][x] = fvalue(x,y,True,lis)


if DEBUG:
    print(*lis, sep="\n\n")
    print("dasdasd",*mynewlis, sep="\n\n")

hlis = [[f" {i}" if x == 0 else "#" for x in range(SIZE+1)] if i!=0 else ["  " if z == 0 else z for z in range(SIZE+1)] for i in range(SIZE+1)]

def show(hlis = hlis):
    for row in hlis:
        print(*row, sep=" | ")
        print("---+"*SIZE+"---")

print("Welocme To Minesweeper \n\nit Took me so much time to write its logic \n\nGive input like X-Y or X,Y for eg.'5-6' or '5,6' \n")
print("write 'F' or f at end to mark as flag for eg. 'X-Yf' or 'X-YF' \n\n\n")

while True:
    f = 0
    show()
    print("")
    xy = input("XY:")
    
    if "f" in xy or "F" in xy:
        f = 1
        xy = xy[0:-1]
        print(f"\n{xy} is marked as [F]lag\n")

    if "-" in xy:
        X,Y = xy.split("-")
    elif ' ' in xy:
        X,Y = xy.split(" ")
    elif ',' in xy:
        X,Y = xy.split(",")
    X,Y = int(X),int(Y)
    
    if X<1 or Y<1:
        print("\n[!]Input error, index must be greater than 0\n")
        continue
    
    elif X>SIZE or Y>SIZE:
        print(f"\n[!]Input error, index must be less than {SIZE}\n")
        continue
    
    if mynewlis[Y-1][X-1] == "@" and f == 0:
        hlis[Y][X] = lis[Y-1][X-1]
        show(lis)
        print("YOU LOST")
        break
    
    elif f == 0 and hlis[Y][X] != "F":
        hlis[Y][X] = lis[Y-1][X-1]
        hlis = check(X-1,Y-1,hlis,mynewlis)
        # print(*mynewlis, sep="\n")
    
    elif hlis[Y][X] != "F" and hlis[Y][X] == "#":
        hlis[Y][X] = "F"
    elif hlis[Y][X] != "#":
        hlis[Y][X] = "#"

    # if "#" not in hlis:
    #     for y in range(SIZE):
    #         for x in range(SIZE):
    #             if hlis[y][x] == "F":
    #                 hlis[y][x] = CLIS["@"]+str("@")+CLIS["r"]
    count = sum(row.count("#") for row in hlis) + sum(row.count("F") for row in hlis)
    if count == BOMB:
        print("You Won")
        show(lis)
        break