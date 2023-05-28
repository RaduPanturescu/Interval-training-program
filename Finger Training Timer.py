#---- Finger Training Timer -----#

import winsound
import time
import os
from tkinter import *
from tkinter import ttk


frequency = 500  # Set Frequency To 2500 Hertz
frequency2 = 800
duration = 1500  # Set Duration To 1000 ms == 1 second
duration2 = 500
clear = lambda: os.system('cls')

# Storing round function for button
def store_rounds():
    global rounds
    rounds = entry.get() 

# Set rounds button with command
top = Tk()
button2 = Button(top, text="Set Rounds", command=store_rounds)

# Main Program
def roundStart():
  top.destroy()
  clear()
  timeout = 87

  for i in range(int(rounds)):
    clear()
    time.sleep(0.5)
    print("\n3!\n".center(15,"-"))
    winsound.Beep(frequency, duration2)
    time.sleep(0.5)

    clear()
    print("\n2!\n".center(15,"-"))
    winsound.Beep(frequency, duration2)
    time.sleep(0.5)

    clear()
    print("\n1!\n".center(15,"-"))
    winsound.Beep(frequency, duration2)
    time.sleep(0.5)

    clear()
    print("\nGo\n".center(15,"-"))
    winsound.Beep(frequency2, duration2)
    time.sleep(0.5)

    worktime = 11   # exercise time
    set = 1

    for i in range(worktime,0,-1):
      clear()
      
      print(f"--Round {set}---")

      print("  " + str(i))
      print("-----")
      time.sleep(1)
      set =+ 1

    clear()
    print("\nBreak\n".center(15,"-"))
    winsound.Beep(frequency, duration)

    for i in range(timeout,0,-1):
      
      clear()
      print(f"--Break {set}---")

      print("  " + str(i))
      print("-----")
      time.sleep(1)
      
      
# Button Area #
top.geometry("300x150")
top.title("Finger Training")

style = ttk.Style()
style.configure("TFrame", background="grey")
style.configure("TButton", foreground="black", background="gray")

label1 = Label(text= "How many rounds?",)
label1.pack(side = "top")

entry = Entry(top)
entry.pack(side = "top")

button2.pack(side="top")

button = Button(top, text = "Start Training", command = roundStart)
button.pack(side = "bottom")


# END #
if __name__ == "__main__":
  top.mainloop()