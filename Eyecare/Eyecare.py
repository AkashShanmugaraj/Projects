import time
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import os
main = Tk()
main.geometry("200x200")
main.title("Eyecare")


sub = Tk() 
sub.geometry("250x250")
def care(): 
    
    count = 0
    while 1 + 1 == 2:
        count += 1
        b2 = Button(text = "End Session", command =lambda: quit()).pack()
        Label(sub, text = "Session " + str(count)).pack()
        Label(sub, text = "\nEye Care session " + str(count) + " Started at " + str(datetime.now().time())).pack()
        messagebox.showinfo("EyeCare", "Eyecare Session Started sucessfully")
        time.sleep(1200)
        messagebox.showinfo("EyeCare", "20 minutes over.. Kindly take rest by clicking \"OK\"")
        time.sleep(20)
        messagebox.showinfo("Eyecare", "Rest duration completed. You can proceed with your work. Thankyou ☺")
        Label(sub, text = "\nEyecare Session " + str(count) + " Ended at " + str(datetime.now().time())).pack()
        
def sessionquit():
    sub.destroy()
def quit():
    quit()
Label(main, text = "Eyecare, \ncare your eyes during the online classes").pack()
b1 = Button(main, text = "Start Session", command = care).pack()
b2 = Button(main, text = "End Session" , command = sessionquit).pack()
b3 = Button(main, text = "Quit Program", command = quit)

main.mainloop()
