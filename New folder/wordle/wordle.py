import random_word
import enchant
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(convert=True)
RES,RED,GREEN,YELLOW=Style.RESET_ALL,Fore.RED ,Fore.GREEN, Fore.YELLOW

print(f"{GREEN}Welcome to WORDLE{RES}")
time.sleep(1)
print(f"{YELLOW}it may take some time to load...{RES}")
time.sleep(1)

# ........funct........
def hin_giver(wrd,rig):
    a = True
    for i in range(0,len(wrd)):
        if wrd[i] == rig[i]:
            print(GREEN,wrd[i],end="")
            print(RES,end="")
        elif wrd[i] in rig:
            a = False
            print(YELLOW,wrd[i],end="")
            print(RES,end="",)
        else:
            a = False
            print(RED,wrd[i],end="")
            print(RES,end="")
    print("")
    return a

def input_(i):
    return (input(f"{i}. WORD: ")).lower()
    
def gen_():
    return (genrator.get_random_word(minLength=5,maxLength=5)).lower()

def gen_giv(wrd):
    a = False
    word = wrd
    a = checker.check(word)
    if "-" in word:
        a = False
    if len(wrd) != 5:
        a = False
    debug_lis.append(word)
    if a == True:
        return (word,word)
    else:
        return (False,word)
def get_m_wrd():
    global debug
    global debug_lis
    global genrator
    global checker

    genrator = random_word.RandomWords()
    checker = enchant.Dict("en_US")

    debug_lis = []
    debug = False

    try:
        a = True
        while a:
            word, word_= gen_giv(gen_())
            if word == False:
                debug_lis.append(word_)
            else:
                a = False
    except:
        print("[ERROR] retrying in 1s....")
        time.sleep(1)
        word, debug_lis=gen_giv()
    return word

def game():
    wd=get_m_wrd()
#..........debug............
    if debug:print(f"[DEBUG]INVALID_LIST: {debug_lis} \n[DEBUG]WORD: {wd}")

    i = 1
    while i < 7:
        inp = input_(i)
        _,inp = gen_giv(inp)
        if (_):
            i+=1
            win = hin_giver(inp,wd)
        else:
            print("invalid input")
        
        if win:
            print(f"{GREEN}YOU WON{RES}")
            print(f"{YELLOW}The word is: {inp}{RES}")
            i = 8
    if not(win):
        print(f"{RED}You Lost") 
        print(f"{YELLOW}The word is: {wd}{RES}")
#........STARTING........
play = True
while play:
    con = (input("Do you want to play([Y]/N)")).lower()
    if con == "n":
        play = False
        
        print("Exiting.....")
    else:
        game()