# import pyautogui
import os
import pathlib
from urllib.parse import quote
import requests
import time
import csv
from webbrowser import open






from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite

class InternetException(Exception):
    """
    Host machine is not connected to the Internet or the connection Speed is Slow
    """
    pass


WIDTH, HEIGHT = size()



def checkNum(num:str)->bool:
    return '+'in num or '_'in num


def findTextBox()->None:
    dir_path=os.path.dirname(os.path.realpath(__file__))
    locate = (f"{dir_path}\\data\\pywhatkit_smile.png")
    try:
        moveTo(locate[0]+150,locate[1]-10 )
        click()
    except Exception:
        locate = (f"{dir_path}\\data\\pywhatkit_smile1.png")
        moveTo(locate[0]+150,locate[1]-10 )
        click()

def connection()->None:
    try:
        requests.get("https://google.com",timeout=5)
    except requests.RequestException:
        raise InternetException(
            "Error while connecting to the Internet. Make sure you are connected to the Internet!"
        )
    

def _web(receiver: str, message: str)->None:
    """ Opens whatsapp Web based on the reciever """
    if checkNum(num=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)



def sendMesg(receiver: str, message: str, wait_time:int)->None:
    
    _web(receiver=receiver,message=message)
    time.sleep(5)
    click(WIDTH/2,HEIGHT/2 + 15)
    time.sleep(wait_time-5)
    if not checkNum(num=receiver):
        index = 0
        length = len(message)       
        while index < length:
            letter = message[index]
            if letter == ":":    
                typewrite(letter)
                index += 1
                while index < length:
                    letter = message[index]
                    if letter == ":":
                        press("enter")
                        break
                    typewrite(letter)
                    index += 1
            elif letter == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(letter)
            index += 1
        press("enter")
    findTextBox()
    press("enter")

def parser():
    with open("database.csv","r") as file:
        reader = csv.reader(file)
        iter_reader = iter(reader)
        for( iter_reader) in iter_reader:
            
            print("Message sent to "+iter_reader[1])
            sendMesg("+91"+str(iter_reader[1]),msg,wait_time=3)
            

msg = """Hello,
Get ready as Mood Indigo is coming to delhi on 13th - 14th October with its Mini Mood Indigo 🔥
Some of The unique incentives are: 
1) Mood Indigo Delhi multicity certificates to all the participants and the winners of multicity 
2) Direct Entry into the higher rounds of mood indigo in main fest in IIT Bombay. 
3) Championship trophy - Take your college to the top of the leaderboard by winning and participating in the competitions, the college with highest points will be awarded with Delhi Multicity Champions
Register now at my.moodi.org/multicities 
Rule Book is attached here - https://drive.google.com/file/d/1Qsm-c9juHlEoXXmi66yweaoG7bpoi2zc/view?usp=drive_link"""
parser()