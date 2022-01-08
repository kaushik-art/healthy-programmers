import pygame
import time
import datetime
def music(mp3):
    pygame.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play(-1)
def water():
    music("water.mp3")
    print("Drink water")
def eyes():
        music("eyes.mp3")
        print("DO eyes exercise")

def physical_activities():
    music("exercise.mp3")
    print("DO physical exercises")
def text(a):
    if a == "water".lower():
        with open("water.txt","a") as f:
            f.write(time.asctime(time.localtime()))
    elif a == "eyes".lower():
        with open("eyes.txt","a") as f:
            f.write(time.asctime(time.localtime()))
    elif a == "physical_active".lower():
        with open("physical_exercises.txt","a") as f:
            f.write(time.asctime(time.localtime()))
def stop():
    while True:
        user = input("enter\n")
        if user == "done":
            pygame.mixer.music.stop()
            break
        else:
            continue

if __name__ == '__main__':
    print("WELCOME TO HEALTH MANAGEMENT SYSTEM.....")
    now =time.strftime('%H:%M:%S')
    if now>='18:00:00' and now<='19:00:00':
        while now>='18:00:00' and now<='19:00:00':
            time.sleep(18)
            a = "water"
            water()
            stop()
            text(a)
            time.sleep(9)
            a= "eyes"
            eyes()
            stop()
            text(a)
            time.sleep(21)
            a = "physical_active"
            physical_activities()
            stop()
            text(a)
            time.sleep(5)
            now =time.strftime('%H:%M:%S')
            continue







