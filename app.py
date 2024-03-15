import streamlit as st
import time
import pyautogui as pg

st.title("WHatsapp Messages Automator")

import pywhatkit
from pynput.keyboard import Controller, Key

# Get the screen resolution
screen_width, screen_height = pg.size()

def schedule_messages():
    pywhatkit.sendwhatmsg_instantly("+44XXXXXXXXXX", "Hello")
    pg.moveTo(screen_width*0.694,screen_height*0.964)
    pg.click()
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    pywhatkit.sendwhatmsg_instantly("+91XXXXXXXXXX", "Hola")
    pg.moveTo(screen_width*0.694,screen_height*0.964)
    pg.click()
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    pywhatkit.sendwhatmsg_instantly("+1XXXXXXXXXX", "Oye luls")
    pg.moveTo(screen_width*0.694,screen_height*0.964)
    pg.click()
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

if st.button("Send Now"):
        schedule_messages()  # Call the function if the button is clicked
