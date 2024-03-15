# Import Libraries
import pywhatkit
import pyautogui
from tkinter import *
import datetime

win = Tk()
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

# Function to schedule message
def schedule_message(phone_number, message, scheduled_time,screen_width,screen_height):
            pywhatkit.sendwhatmsg(phone_number, message, scheduled_time.hour, scheduled_time.minute)
            pyautogui.press('enter') # Sends the message

sched_time=datetime.datetime(2024, 3, 15, 21, 14,0)

mes="Your Message"
p_num='+91XXXXXXXXXX'

schedule_message(p_num,mes,sched_time,screen_width,screen_height)
