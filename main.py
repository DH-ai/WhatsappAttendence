import pywhatkit
import time
import csv

import pywhatkit.sc
# pywhatkit.sendwhatmsg('+917219201845',"Good Morning",7,14)



def parser():
    with open("database.csv","r") as file:
        reader = csv.reader(file)
        iter_reader = iter(reader)
        for( iter_reader) in iter_reader:
            
            print("Message sent to "+iter_reader[1])
            
            pywhatkit.sendwhatmsg_instantly("+91"+str(iter_reader[1]),msg,tab_close=True,wait_time=20
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                            )




msg = """Hello,
Get ready as Mood Indigo is coming to delhi on 13th - 14th October with its Mini Mood Indigo 🔥
Some of The unique incentives are: 
1) Mood Indigo Delhi multicity certificates to all the participants and the winners of multicity 
2) Direct Entry into the higher rounds of mood indigo in main fest in IIT Bombay. 
3) Championship trophy - Take your college to the top of the leaderboard by winning and participating in the competitions, the college with highest points will be awarded with Delhi Multicity Champions
Register now at my.moodi.org/multicities 
Rule Book is attached here - https://drive.google.com/file/d/1Qsm-c9juHlEoXXmi66yweaoG7bpoi2zc/view?usp=drive_link"""
parser()

# print(time.localtime())
