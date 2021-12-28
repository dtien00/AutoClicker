import pyautogui
import easygui
import time
#x coordinate goes left to right as it gets larger
#y coordinate goes up to down as it gets larger
def main(iterations): 
    time.sleep(3)  #Time to move cursor to what you want to click repeatedly
    cursorX = pyautogui.position().x
    cursorY = pyautogui.position().y
    pyautogui.click(cursorX,cursorY, clicks=iterations, interval=0.01)

def rerun():
    reply = easygui.buttonbox("Rerun?", choices=choices)
    print(reply)
    global onRepeat 
    if (reply=="Yes"): 
        onRepeat = True
    else:
        onRepeat = False
    print("END")

# easygui.msgbox("Hello World!", title="Autoclicker")
onRepeat= True #Variable used to determine whether or not to rerun
msg = "Enter a number of clicks (0-999)"
title = "Number of clicks"
choices = ["Yes","No"]
floor = 0
ceiling = 999
while(onRepeat==True):
    print("ITERATION")
    iterations = easygui.integerbox(msg, title, lowerbound=floor, upperbound=ceiling)
    if(iterations!=None):
        main(iterations)
        rerun()
    else:
        onRepeat = False
    
