# import pyautogui
import os
import pathlib
from urllib.parse import quote
import requests
import time
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