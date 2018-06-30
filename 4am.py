trigger = -4
timezone = "EST"
#Ok so in my case, my time zone is est. est is 4 hours behind utc, whitch this program runs on. The amount of hours behind/ahead utc is wha you should put for trigger
#Timezone is just for the "The time is currently: " text
#Oh yeah, everything is in military time
import pygame, os, time
from time import gmtime, strftime
os.system("mode con: cols=40 lines=2")
os.system("title 4AM")
while 1 == 1:
    os.system("cls")
    cur_time = strftime("%H:%M", gmtime()).split(":")
    print("The time is currently: " + str(int(cur_time[0])+trigger) + ":" + cur_time[1] + " " + str(timezone))
    if int(strftime("%H", gmtime()))+trigger == 4: #Trigger time in your time zone
        print("Its 4")
        if strftime("%M", gmtime()) == "00": #Trigger hour
            os.system("cls")
            print("Its 4:00!")
            pygame.mixer.init()
            pygame.mixer.music.load("4am.mp3")
            pygame.mixer.music.play()
            time.sleep(6)
            exit()
    time.sleep(15)
