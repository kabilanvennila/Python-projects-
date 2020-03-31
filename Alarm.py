#Alarm basic app V1.0

#Importing modules that are needed 
import time
import datetime
import pygame
print('*****')
print(' *** ')
print('  *  ')
print(' *** ')
print('*****')

#This is just a basic Greetings 
print('Welcome to Alarm App')
print('SET OF RULES FOR USAGE:')

#User should enter the time in 24 Hours Time format
print('******USE ONLY 24 HOURS CLOCK FORMAT******')
current_time=time.asctime()
current_time=current_time[11:-8]

#prints the current Time 
print("The current time in Your Country is: "+current_time)

#Gets Input from the User To set the alarm timer
User_time=input("plese enter a time : ")
Set_time=User_time

#Execution Part
#NOTE: Change the music location if you want to use this code as it is 
Bool=True
while Bool:
    time=datetime.datetime.now()
    time=str(time.hour)+':'+str(time.minute)
    if(Set_time==time):
        Bool=False
        pygame.mixer.init()
        pygame.mixer.music.load(r"C:\Users\HP\Music\05+The+Conquest+Of+Time+(Instrumental)+-+Adhi.mp3")
        pygame.mixer.music.play()       

