import threading #for both loops to run together
import time
import random 
import sys #red text
def eprint(*args, **kwargs):

    print(*args, file=sys.stderr, **kwargs)

fingpos = 15 #0 = outside door, -1 = inside office
clock = 300 #time system from fnaf
doors = ("OPEN")
power = 100
powercap = 100
night = 1
mini = 0
maxi = 0
fingdetect = 0

def infiniteloop1(): #finger AI
    global mini
    global maxi
    global doors
    global fingpos
    global clock
    global power
    counter = 0
    goal = random.randint(10-mini,35-maxi) 

    while True:
        counter += 1
        if(night == 100):
            clock += 1
        else:
            clock -= 1
        if(doors == ("CLOSED")):
           power -= 1
        if(counter == goal):
            counter = 0
            goal = random.randint(10-mini,35-maxi)
            
            if(fingpos == 14):               
                move = random.randint(1,3)
                if(move == 1):
                    fingpos = 13 
                else:
                    fingpos = 11 
                    
            elif(fingpos == 13):
                move = random.randint(1,3)
                if(move == 1):
                    fingpos = 14
                else:
                    fingpos = 12
                    
            elif(fingpos == 12):
                move = random.randint(1,3)
                if(move == 1):
                    fingpos = 11
                else:
                    fingpos = 10
                    
            elif(fingpos == 11):
                move = random.randint(1,3)
                if(move == 1):
                    fingpos = 12
                else:
                    fingpos = 9
                    
            elif(fingpos == 7):
                move = random.randint(1,2)
                if(move == 1):
                    fingpos = 5
                else:
                    fingpos = 6
                    
            elif(fingpos == 6):
                move == random.randint(1,3)
                if(move == 1):
                    fingpos = 7
                else:
                    fingpos = 4
            elif(fingpos == 5):
                fingpos = 2
                
            elif(fingpos == 4):
                fingpos = 3
                    
            elif(fingpos == 3):
                fingpos -=2
                
            elif(fingpos == 0):
                if(doors == ("OPEN")):
                    fingpos = -1
                    eprint("\nSOMETHING IS INSIDE THE OFFICE\n")
                    time.sleep(2)
                    eprint("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢠\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⣿⣿⣟⣿⣿⣿⣷⠀⠀⠀\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣽⣾⣻⣾⣿⣿⣿⣿⡿⣿⣿⠀⠀⠀\n⠀⠀⠀⢰⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡿⠿⠟⠛⣟⣿⣽⠀⠀⠀\n⠀⠀⠀⠸⣿⣿⣿⣷⣿⣿⣿⣿⡿⠍⠈⠀⠁⣴⡆⠀⠀⠠⢭⣮⣿⡶⠀⠀\n⠀⡴⠲⣦⢽⣿⣿⣿⣿⣿⣟⣩⣨⣀⡄⣐⣾⣿⣿⣇⠠⣷⣶⣿⣿⡠⠁⠀\n⠀⠃⢀⡄⠀⢻⣿⣿⣿⣿⣽⢿⣿⣯⣾⣿⣿⣿⣿⣿⢿⣿⣿⡟⣿⠀⠀⠀\n⠀⠀⠀⠁⠼⣒⡿⣿⣿⣿⣿⣿⣿⣿⣠⣬⠀⠀⠀⠀⣾⣷⡈⣿⡇⠀⠀⠀\n⠀⠀⠀⠀⠀⠉⢳⣿⣿⣿⣿⣿⣿⣿⢟⠗⠼⠖⠒⠔⠉⠉⠻⣿⠇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠈⣻⡿⣿⣿⣿⣿⡿⡀⣤⡄⠸⣰⣾⡒⣷⣴⣿⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠂⢸⡗⡄⠘⠭⣭⣷⣿⣮⣠⣌⣫⣿⣷⣿⣿⠃⠀⠈⠀⠀\n⠀⠀⠀⠀⠀⠈⠀⢸⣿⣾⣷⣦⡿⣿⣿⣿⡿⢻⠞⣹⣿⣿⠏⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⢘⠀⠘⢻⡿⢿⣋⣤⣤⠌⠉⠛⠛⠀⠈⠉⠁⠀⠀⠀⠀⠀⡀\n")

                    eprint("\nFINGER: I'VE GOT YOU NOW WALTUH!!!\n\nYour screams fall on deaf ears until 6AM.\nNobody believes that a senile man could ever do these things...\nYou will never be found.")
                    print("\n\nTime survived: "+str(clock)+" seconds.\nSo close, you only had an infinity more to go!")
                    break
            else:
                fingpos -= 1
                   
        elif(fingpos == 0):
            if(doors == ("CLOSED")):
                time.sleep(2)
                if(clock < 100):
                    fingpos = random.randint(10,12)
                    print(fingpos)
                else:
                    fingpos = random.randint(13,15)
                    print(fingpos)
                eprint("\nFINGER: ...Next time, Waltuh. There's always a next time.\n")                           
        time.sleep(1)

def infiniteloop2():
    global fingpos
    global clock
    global doors
    global power
    global night
    global fingdetect
    global powercap
    global mini
    global maxi
    while True:
        if (clock > 0):  
            if(fingpos < 16 or fingpos > -1):
                if(power > 0):
                    clock = clock + 1
                    if(night == 100):
                        hud = input("\nCAMS: 1\nLIGHTS: 2\nDOORS: 3 ("+doors+")\nPower: "+str(power)+"%\nEons remaining: ∞\n-----------------\nYour input:   ")
                    elif(fingdetect == 0):
                        hud = input("\nCAMS: 1\nLIGHTS: 2\nDOORS: 3 ("+doors+")\nPower: "+str(power)+"%\nTime left (s): "+str(clock)+"\n-----------------\nYour input:   ")
                    else:
                        hud = input("\nFINGER DETECTOR: 1\nLIGHTS: 2\nDOORS: 3 ("+doors+")\nPower: "+str(power)+"%\nTime left (s): "+str(clock)+"\n-----------------\nYour input:   ")
                    if(hud.isnumeric()):
                        hudint = int(hud)
                        if(hudint == 1): #cameras/finger detector
                            easteregg = random.randint(1,23)
                            if(fingdetect == 0):
                                power = power - 2
                                print("\nLOADING... PLEASE WAIT (2% power subtracted)")
                            else:
                                power = power - 3
                                print("\nDETECTING FINGER... PLEASE WAIT (3% power subtracted)")
                            time.sleep(1.7)
                            while True:
                                if(fingdetect == 0):
                                    camnum = input("\ncam6 -- cam7 -- cam8 -- cam9 -- cam10\n |       |               |         |\n |       |               |         |\ncam5    cam4           cam11 -- cam12\n |       |               |         |\n |       |               |         |\ncam3    cam2           cam14 -- cam13\n  \      /               /\n    cam1              cam15\n     |\n    YOU\n\n SELECT A VALID NUMBER (Or an invalid number to exit): ")
                                    while True:
                                        if(camnum.isnumeric()):
                                            camint = int(camnum)
                                            if(0 < camint < 16):    #cameras
                                                if(camint == fingpos):
                                                    power = power - 1  #power value
                                                    eprint("\nYou see someone on the cameras.\n...Suddenly, they twist their head directly towards the camera, as they say:")
                                                    miketalk = random.randint(1,5)
                    
                                                    if(miketalk == 1):
                                                        eprint("\nFINGER: I tend to get a little quirky at night, Waltuh...\n")
                                                    elif(miketalk == 2):
                                                        eprint("\nFINGER: No more half measures...\n")
                                                    elif(miketalk == 3):
                                                        eprint("\nFINGER: Waltuh... keep your camera down, Waltuh...\n")    
                                                    elif(miketalk == 4):
                                                        eprint("\nFINGER: Here's whats gonna happen-- I'm gonna turn your asshole into pimento cheese.\n")
                                                    elif(miketalk == 5):
                                                        eprint("\nFINGER: Hey, uh... Vince? Why are we shootin' all my scenes first?\n")
                                                    else:
                                                        eprint("\nSHADOW GUSTAVO: This error message is not up to Pollos Standards.\n")
                                                else:
                                                    easteregg = random.randint(1,15)
                                                    power = power - 1
                                                    if(easteregg == 2):
                                                        print("...It's just an empty room.\nYou swore you saw a fresh set of meth lab equipment with a bloody handprint staining one of the tools...")
                                                        time.sleep(0.4)
                                                        print("...But when you blink again, it's gone.")
                                                    elif(easteregg == 10):
                                                        print("...It's just an empty room.\nSuddenly, a shadowy figure wearing what seems to be a tie crosses CAM "+str(camint)+"...")
                                                        time.sleep(0.4)
                                                        print("...Nevermind. You're just seeing things. Keep it together, Walt...!")
                                                    elif(easteregg == 15):
                                                        print("...You see a strange stuffed animal spinning in front of CAM "+str(camint)+"...")
                                                        time.sleep(0.4)
                                                        print("...But it's gone in a flash. Nobody's in the room, either.")
                                                    else:
                                                        print("...It's just an empty room.")
                                                time.sleep(2)
                                                camnum = input("\nNEW CAMERA INPUT (Or select an invalid number to exit): ")
                                            else:
                                                eprint("\nEXITING...")
                                                time.sleep(1)
                                                break
                                        else:
                                            eprint("\nEXITING...")
                                            time.sleep(1)
                                            break
                                    break
                                else:
                                    if(fingpos == 0):
                                        eprint("\nFINGER DETECTOR: RUN\n")
                                    else:
                                        eprint("\nFINGER DETECTOR: Finger is at CAM "+str(fingpos)+".\n")
                                    time.sleep(1)
                                    break
                                
                        elif(hudint == 2):  #lights
                            if(fingpos == 0):
                                eprint("\nSHUT THE DOOR NOW\nFINGER: Why won't you let me inside, Waltuh...?")
                            elif(fingpos == 4 or fingpos == 3):
                                print("\nYou swore you just saw a silhouette peek in from the corner of the left hallway...")
                            elif(fingpos == 5 or fingpos == 2):
                                print("\nYou swore you just saw a silhouette peek in from the corner of the right hallway...")
                            elif(fingpos == 1):
                                print("\nSomeone makes their way to the end of the hall, but they're too far away to close the door.")
                            else:
                                logue = random.randint(1,15)
                                if(logue == 1):
                                    desc = (" the cobweb in the corner of the hall.")
                                elif(logue == 2):
                                    desc = (" some weird yellow-ish rabbit costume near the door.\n...Huh. It smells like something died in there.")
                                elif(logue == 3):
                                    desc = (" an elderly man in a wheelchair... ringing a bell.\nYou feel like strapping a pipe bomb to their wheelchair for some reason...")
                                else:
                                    desc = (" the hallway in front of you.")

                                    
                                print("\nFlickering lights pierce the darkness, yet the only thing in sight is"+desc+"\n")
                            power = power - 3
                            time.sleep(1)
                        elif(hudint == 3):  #doors
                        
                            if(doors == ("OPEN")):
                                print("\nThe door slams shut.\nYour power slowly drains...") 
                                doors = ("CLOSED")
                                power = power - 4
                                time.sleep(1)
                           
                            elif(doors == ("CLOSED")):
                                if(fingpos == 0):
                                    eprint("\nBAD IDEA\nFinger stands at your door.")
                                else:
                                    print("\nYou opened the door... nobody's there.")
                                doors = ("OPEN")
                                time.sleep(1)
                        else:
                            eprint("\nNOT A VALID ENTRY\n")
                    else:
                        eprint("\nINVALID CHARACTER\n")
                    time.sleep(1)
                else:
                    eprint("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢠\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⣿⣿⣟⣿⣿⣿⣷⠀⠀⠀\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣽⣾⣻⣾⣿⣿⣿⣿⡿⣿⣿⠀⠀⠀\n⠀⠀⠀⢰⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡿⠿⠟⠛⣟⣿⣽⠀⠀⠀\n⠀⠀⠀⠸⣿⣿⣿⣷⣿⣿⣿⣿⡿⠍⠈⠀⠁⣴⡆⠀⠀⠠⢭⣮⣿⡶⠀⠀\n⠀⡴⠲⣦⢽⣿⣿⣿⣿⣿⣟⣩⣨⣀⡄⣐⣾⣿⣿⣇⠠⣷⣶⣿⣿⡠⠁⠀\n⠀⠃⢀⡄⠀⢻⣿⣿⣿⣿⣽⢿⣿⣯⣾⣿⣿⣿⣿⣿⢿⣿⣿⡟⣿⠀⠀⠀\n⠀⠀⠀⠁⠼⣒⡿⣿⣿⣿⣿⣿⣿⣿⣠⣬⠀⠀⠀⠀⣾⣷⡈⣿⡇⠀⠀⠀\n⠀⠀⠀⠀⠀⠉⢳⣿⣿⣿⣿⣿⣿⣿⢟⠗⠼⠖⠒⠔⠉⠉⠻⣿⠇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠈⣻⡿⣿⣿⣿⣿⡿⡀⣤⡄⠸⣰⣾⡒⣷⣴⣿⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠂⢸⡗⡄⠘⠭⣭⣷⣿⣮⣠⣌⣫⣿⣷⣿⣿⠃⠀⠈⠀⠀\n⠀⠀⠀⠀⠀⠈⠀⢸⣿⣾⣷⣦⡿⣿⣿⣿⡿⢻⠞⣹⣿⣿⠏⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⢘⠀⠘⢻⡿⢿⣋⣤⣤⠌⠉⠛⠛⠀⠈⠉⠁⠀⠀⠀⠀⠀⡀\n")
                    eprint("\nFINGER: Power's out, Waltuh... I like the dark. You're gonna like the dark too.")
                    if(night == 100):
                        print("\n\nTime survived: "+str(clock)+" seconds.\nSo close, you only had an infinity more to go!")
                    break
            
        else:
            if(night == ("666 (FULL MEASURE)")):
                eprint("\n\n6AM\n\nFINGER: how the fuck") #if you beat night 666
                time.sleep(1)
                quit()
                
            fingpos == -2
            eprint("\n\n6AM (Yeah, bitch!!)\n\nFINGER: Here's what's gonna happen. You're gonna get your pay, walk outta those doors, and come back tomorrow night.\nI'll be waitin'.")
            time.sleep(1)
            cont = input("\nContinue? (Y \ N):   ")     #resets power, door status, time, and fingpos and makes ai harder
            if(cont == ("y") or cont == ("Y")):
                doors = ("OPEN")
                clock = 99999
                currency = power
                time.sleep(0.5)
                shop = input("\n\nUsing your leftover "+str(currency)+"% power, you cook meth and sell it to any buyers available.\nAt the end of the day, you and Jesse net a total of $"+str(currency)+",000.\n...Wanna spend some of that money? (Y / N):   ")
                if(shop == ("y") or shop == ("Y")):
                    time.sleep(0.5)
                    while True:
                        print("\n\nYour Money: $"+str(currency)+",000\n")
                        items = input("BUYABLE ITEMS (One Per Night Usage):\n1) 10% Power Increase ($20,000)\n2) Finger Detector ($40,000)\n(Press any other key to exit.)\n--------------------------------\nYour input:   ")
                        if(items.isnumeric()):
                            itemsint = int(items)
                            if(itemsint == 1):
                                if(currency >= 20):
                                    powercap += 10
                                    currency -= 20
                                    print("\nCha-ching! Enjoy your limited 110% power!\n")
                                    time.sleep(1)
                                    break
                                else:
                                    print("\nOops... maybe next night, save up some more power... to get more power?\n") #oOPS! you have to put the CD in your computer
                            elif(itemsint == 2):
                                if(currency >= 40):
                                    fingdetect += 1
                                    print("\nCha-ching! Enjoy your, uh... Finger Detector!\n")
                                    time.sleep(1)
                                    break
                                else:
                                    print("\nOops... you'll need a liiiittle more than $"+str(currency)+" to get the FINGER DETECTOR.\n")
                            else:
                                break
                        else:
                            print("\n...Well, that's all for today.\n")
                            time.sleep(1)
                            break
                        time.sleep(1)
                else:
                    print("\n\n...Suddenly, your money dissapears into thin air!\nUhhh... what the fuck?! Whatever. As if you aren't a millionare...")
                    time.sleep(1)
                    print("\n...Wait, no. Skyler gave it all to Ted.\nFuck.\n\n")
                    time.sleep(1)
                clock = 300
                power = powercap
                fingpos = 15

                if(night < 6):  #new night changing system
                    night += 1
                    mini += 1
                    maxi += 5
                else:
                    eprint("\n\nPure Cook Mode (ENDLESS)\n-----------------")
                    mini += 1
                    maxi += 1
                    clock = 1
                    time.sleep(1)
                eprint("\n\nNight "+str(night)+"\n-----------------")
                time.sleep(1)
                if(power == 110):
                    eprint("\nYou hear the power generator whirring to life.\n...That extra 10% is gonna make a difference.")
                elif(fingdetect == 1):
                    eprint("\nYou equip the FINGER DETECTOR USB into the camera monitor.\n...Your camera system is replaced with a singular button.")
            elif(cont == ("n") or cont == ("N")):
                eprint("\nFINGER: ...Alright. You get your pay, and your rear end walks outta here unscathed.\nNot what I'd reccomend, but a deal's a deal.\nThanks for playing, Waltuh...")
                time.sleep(3)
                quit()
            else:
                eprint("\nTry again")
                time.sleep(3)
                quit()


print("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢠\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⣿⣿⣟⣿⣿⣿⣷⠀⠀⠀\n⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣽⣾⣻⣾⣿⣿⣿⣿⡿⣿⣿⠀⠀⠀\n⠀⠀⠀⢰⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡿⠿⠟⠛⣟⣿⣽⠀⠀⠀\n⠀⠀⠀⠸⣿⣿⣿⣷⣿⣿⣿⣿⡿⠍⠈⠀⠁⣴⡆⠀⠀⠠⢭⣮⣿⡶⠀⠀\n⠀⡴⠲⣦⢽⣿⣿⣿⣿⣿⣟⣩⣨⣀⡄⣐⣾⣿⣿⣇⠠⣷⣶⣿⣿⡠⠁⠀\n⠀⠃⢀⡄⠀⢻⣿⣿⣿⣿⣽⢿⣿⣯⣾⣿⣿⣿⣿⣿⢿⣿⣿⡟⣿⠀⠀⠀\n⠀⠀⠀⠁⠼⣒⡿⣿⣿⣿⣿⣿⣿⣿⣠⣬⠀⠀⠀⠀⣾⣷⡈⣿⡇⠀⠀⠀\n⠀⠀⠀⠀⠀⠉⢳⣿⣿⣿⣿⣿⣿⣿⢟⠗⠼⠖⠒⠔⠉⠉⠻⣿⠇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠈⣻⡿⣿⣿⣿⣿⡿⡀⣤⡄⠸⣰⣾⡒⣷⣴⣿⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠂⢸⡗⡄⠘⠭⣭⣷⣿⣮⣠⣌⣫⣿⣷⣿⣿⠃⠀⠈⠀⠀\n⠀⠀⠀⠀⠀⠈⠀⢸⣿⣾⣷⣦⡿⣿⣿⣿⡿⢻⠞⣹⣿⣿⠏⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⢘⠀⠘⢻⡿⢿⣋⣤⣤⠌⠉⠛⠛⠀⠈⠉⠁⠀⠀⠀⠀⠀⡀\n")
time.sleep(0.5)
print("\nFIVE NIGHTS AT FINGER'S\n------------------------")
while True:
    time.sleep(0.5)
    print("\nNew Game: 1")
    choice = input("Instructions: 2\nExit: 3\n\n")
    if(choice.isnumeric()):
        print("\n")
        time.sleep(0.2)
        choiceint = int(choice)
        if(choiceint == 1):
            break
        elif(choiceint == 2):
            print("JESSE: Uh... hello, like, hello hello, bitch?!")
            time.sleep(0.5)
            print("...Damn, I'll just send a message.")
            time.sleep(0.5)
            print("\nYo, uh... Mr. White, the doors are kinda, like... glued shut, bitch!\nGetting you outta there would take, like, 6 hours... or around 5 minutes. Yeah, whichever you prefer... yo.")
            time.sleep(0.7)
            print("\nAnyways, you're hooked up to a fancy camera system to like, spy on people, or some shit.\n...Oh yeah, and a door with lights. If someone tries to get in your room, uh... close them, I think.")
            time.sleep(0.7)
            print("\nOh, also... the place has, like... limited power, so you can't just keep the doors closed.\nYou need every percent of that power to cook crystal afterwards, bitch!! See ya at 6, Mr. White!\n")
        elif(choiceint == 3):
            eprint("FINGER: Well then... goodbye, Waltuh.")
            time.sleep(1)
            quit()
        else:
            eprint("NOT A VALID INPUT")
    else:
        if(choice == "finger" or choice == "POLLOS" or choice == "pollos" or choice == "Pollos"):
            print("\nSHADOW GUSTAVO: ...You said the magic word(s), have you not?\nPlease pick whatever night you find suitable for you.\n")
            time.sleep(1)
            nightnum = input("Select the night that you would want to play (2-5, or anything else for Pure Cook Mode):   ")
            if(nightnum == "1"):
                print("\nSHADOW GUSTAVO: You should've chose New Game, Mr. White.\nInstead, you decided to waste my time.")
                time.sleep(1.5)
                print("Goodbye, Walter.")
                time.sleep(0.5)
                quit()
            if(nightnum == "2"):
                mini = 3
                maxi = 5
                night = 2
                break
            elif(nightnum == "3"):
                mini = 4
                maxi = 10
                night = 3
                break
            elif(nightnum == "4"):
                mini = 5
                maxi = 15
                night = 4
                break
            elif(nightnum == "5"):
                mini = 6
                maxi = 12
                night = 5
                break
            elif(nightnum == "666" or nightnum == "69" or nightnum == "420"):
                mini = 6
                maxi = 20
                night = ("666 (FULL MEASURE)")
                eprint("You are DONE.\n")
                time.sleep(1)
                break
            else: #pure cook mode (ENDLESS)
                mini = random.randint(0,8)
                maxi = random.randint(0,20)
                night = 100
                clock = 1
                time.sleep(1)
                (infiniteloop2)
                break
            (infiniteloop2)
            print("\n\n")
            break
        elif(choice == "shadow gus" or choice == "shadow gustavo" or choice == "Shadow gus" or choice == "Shadow Gustavo" or choice == "Shadow gustavo" or choice == "SHADOW GUSTAVO" or choice == "SHADOW GUS" or choice == "4378"):
            quit()
        else:
            eprint("NOT A VALID INPUT")
if(night == 100):
    eprint("\n\n\nNight ∞ (Pure Cook Mode)\n--------------------------------------")
    time.sleep(1)
else:
    eprint("\nNight "+str(night)+"\n--------------------------------------")
    time.sleep(1)

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()
