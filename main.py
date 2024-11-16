import pywhatkit
import time
import csv

import pywhatkit.sc
# pywhatkit.sendwhatmsg('+917219201845',"Good Morning",7,14)


def check(num):
    if len(num) == 10:
        return num
    if num[0] == "0":
        return num[1:]
    else:
        return num
def parser():
    with open("./WhatsappAttendence/database.csv","r") as file:
        reader = csv.reader(file)
        iter_readerr = iter(reader)
        for( iter_reader) in iter_readerr:
            

            try:
                pywhatkit.sendwhatmsg_instantly("+91"+check(str(iter_reader)),msg,tab_close=True,wait_time=10)
            except:
                print("Error")
                pass


                                            
                                            
                                            
                                            
                                            

msg = """Greetings from Mood Indigo, 
Based on popular request, we've extended the submission deadline for your competition entries! 🎉

🗓 New Deadline: 24th November 2024, 11:59 PM

This extra time is all yours to make sure your entry is exactly how you want it. Don’t forget to go over the guidelines to ensure everything’s set.
Also note that, no further deadlines will be extended 
You Can Register now and submit the drive link till 24th Nov 2024
Register now at my.moodi.org/competitions 
rulebook: rulebook.moodi.org"""
parser()

# print(time.localtime())
