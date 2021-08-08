import os
#To hide version info and welcome message from Pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
import schedule
import time
"""
9am-6pm
water- water.mp3 - Drank- 25min - log
eyes- eyes.mp3 - Done - 30min - log
exercise- physical.mp3 - Done - 45min - log
"""
no_glass = 0
current_time=time.strftime("%H:%M:%S")
work_start="16:00:00"
work_end="17:01:00"
water_song="water.mp3"
exercise_song="physical.mp3"
eyes_song="eyes.mp3"
# tot_no_glass=18
waterSec=10
eyesSec=20
exerciseSec=30

def PlayMusic(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)

def water_reminder():
    drank_w=''
    while drank_w != 'drank':
        PlayMusic(water_song)
        drank_w=input("Drink Water, Enter 'drank' as drink it. ").lower()
        if drank_w == 'drank':
            mixer.music.stop()
            f=open("Water_Report.txt","a")
            now=time.ctime()
            f.write("You Drank Water on: "+now+"\n")
            f.close()
            print("Thank You")
            time.sleep(waterSec)
            break

def eyes_reminder():
    edone_e=''
    while edone_e != 'done':
        PlayMusic(eyes_song)
        edone_e=input("Do eyes exercise, Enter 'done' as you have finish doing. ").lower()
        if edone_e == 'done':
            mixer.music.stop()
            f=open("Eyes_Report.txt","a")
            now=time.ctime()
            f.write("You did Eyes Exercise on: "+now+"\n")
            f.close()
            print("Thank You")
            time.sleep(eyesSec)
            break
def exercise_reminder():
    exdone_e=''
    while exdone_e != 'done':
        PlayMusic(exercise_song)
        exdone_e=input("Do small exercise, Enter 'done' as you finish doing. ").lower()
        if exdone_e == 'done':
            mixer.music.stop()
            f=open("Exercise_Report.txt","a")
            now=time.ctime()
            f.write("You did Exercise on: "+now+"\n")
            f.close()
            print("Thank You")
            time.sleep(exerciseSec)
            break

print("Welcome To Healthy Programmer \n")

try:

    while (current_time is not work_end):


        if current_time >= work_start and current_time <= work_end:
            tot_no_glass = 18

            if no_glass == tot_no_glass:
                pass
            else:
                water_reminder()
                no_glass += 1
            eyes_reminder()
            exercise_reminder()
            current_time=time.strftime("%H:%M:%S")
except Exception as e:
    print(e)