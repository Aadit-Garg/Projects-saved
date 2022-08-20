import speech_recognition as sr
from random import randint 
import pyttsx3, names, time, wikipedia, webbrowser, colorama

uname = ""

def namer():
    print(colorama.Fore.BLACK, colorama.Back.WHITE)
    uname = input("Name: ")
    print("welcome:", uname)
    return uname

engine = pyttsx3.init()
lstnr = sr.Recognizer()

def tell(line):
    engine.say(line)
    engine.runAndWait()

def respond(line):
    engine.say(line)
    engine.runAndWait()

brek = False
loop = 1
u_name = namer()
while True:
    try:
        while not(brek):


            with sr.Microphone() as source:
                lstnr.adjust_for_ambient_noise(source,duration=5)
                print("Listening...")
                if loop==1:
                    tell(("Hello", u_name," I am Dave, what can I do for you"))
                    loop+=1
                voice = lstnr.listen(source)
                print(voice)
                conv = lstnr.recognize_google(voice)

                print(conv)
                conv = conv.lower()
                text = conv

                if 'dave' in conv or 'dev' in conv or "DAV" in conv:
                    conv = conv.replace("dev", "")                
                
                    if "number" in conv or "random number" in conv:
                        a = randint(0,100)
                        print(a)
                        tell(a)
                    elif 'search'  in conv:
                        conv = conv.replace("search", "")
                        webbrowser.open_new_tab(conv)
                        time.sleep(5)

                    elif "name" in conv or "random name" in conv:
                        tell(names.get_full_name(gender ="male"))
                        
                    elif "time" in conv:
                        tell(time.ctime())
                        print(time.ctime())

                    elif 'wikipedia' in conv:
                        respond('Searching Wikipedia')
                        conv = conv.replace("wikipedia", "")

                        results = wikipedia.summary(conv, sentences=3)
                        respond("According to Wikipedia")
                        print(results)
                        respond(results)

                    elif 'play' in conv:
                        conv = conv.replace("play", "")
                        conv = conv.split(" ")  

                        webbrowser.open_new_tab("https://www.youtube.com/ results?search_query=" + '+'.join(conv))
                        respond("youtube is opening")
                        time.sleep(5)

                if "exit" in conv or 'quit' in conv or 'q' in conv:
                    tell("exiting...")
                    brek = True
    except:
        print("error")