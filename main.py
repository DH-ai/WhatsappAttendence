import pywhatkit
import time

# pywhatkit.sendwhatmsg('+917219201845',"Good Morning",7,14)
index=0
numer_dict={
    "1":["Kamlesh Kurmi Sir","+919827736549"],
    "2":["Mahesh Kurmi Sir ",'+918839833628'],
    "3":["Jindal Sir","+919752611611"],
    "4":["Prakhar Gupta","+919235527628"],
    "5":["Aditya Gautam","+917771033480"]
}

for i in range(1,6):
    for j in range(1,6):
        msg=f"{numer_dict[str(i)][0]}, GoodAfter Noon {j} times"
        try:

            pywhatkit.sendwhatmsg_instantly(f"{numer_dict[str(i)][1]}",msg,tab_close=True)
            print(f"Message sent to {numer_dict[str(i)][0]}\n")
        except Exception:

            print(f"Unable to send the message on iteration {numer_dict[str(i)][0]}")
        time.sleep(1.5)
