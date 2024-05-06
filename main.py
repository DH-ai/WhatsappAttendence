import pywhatkit


# pywhatkit.sendwhatmsg('+917219201845',"Good Morning",7,14)
index=0
while True:
    pywhatkit.sendwhatmsg_instantly('+919171981824',f"GoodMornign {index}")
    print(index)
    index+=1
