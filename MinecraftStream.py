import socket
import threading
import time
import pyautogui
import ctypes
import win32con
import numpy
import Xlib
from pynput.keyboard import Key, Controller

keyboard = Controller()
from pynput.mouse import Button, Controller

mouse = Controller()

SERVER = "irc.twitch.tv"
PORT = 6667
PASS = ""
BOT = "MC_Bot"
CHANNEL = "tecnagamer"
OWNER = "tecnagamer"
message = ""
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send((  "PASS " + PASS + "\n" +
            "NICK " + BOT + "\n" +
            "JOIN #" + CHANNEL + "\n").encode())

def gamecontrol():
    global message
    while True:
        if "up" in message.lower():
            pyautogui.moveRel(None,-50,0.3)
            message = ""
        elif "down" in message.lower():
            pyautogui.moveRel(None,50,0.3)
            message = ""
        elif "left" in message.lower():
            pyautogui.moveRel(-50,None,0.3)
            message = ""
        elif "right" in message.lower():
            pyautogui.moveRel(50,None,0.3)
            message = ""
        elif "turnaround" in message.lower():
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)
            pyautogui.moveRel(50,None,0.3)


            message = ""
        elif "forward" in message.lower():
            pyautogui.mouseDown(button='middle')
            message = ""
            time.sleep(1)
            pyautogui.mouseUp(button='middle')
        elif "walk" in message.lower():
            pyautogui.mouseDown(button='middle')
            message = ""
        elif "stop" in message.lower():
            message = ""
            pyautogui.mouseUp(button='middle')
        elif "punch" in message.lower():
            pyautogui.click(button='left')
            message = ""
        elif "lclick" in message.lower():
            pyautogui.click(button='left')
            message = ""
        elif "rclick" in message.lower():
            pyautogui.click(button='right')
            message = ""
        elif "mine" in message.lower():
            pyautogui.mouseDown(button='left')
            message = ""
            time.sleep(5)
            pyautogui.mouseUp(button='left')
        elif "break" in message.lower():
            pyautogui.mouseDown(button='left')
            message = ""
            time.sleep(1)
            pyautogui.mouseUp(button='left')
        elif "destroy" in message.lower():
            pyautogui.mouseDown(button='left')
            message = ""
            time.sleep(10)
            pyautogui.mouseUp(button='left')
        elif "hold" in message.lower():
            pyautogui.mouseDown(button='left')
            message = ""
        elif "release" in message.lower():
            message = ""
            pyautogui.mouseUp(button='left')
        elif "hblft" in message.lower():
            pyautogui.scroll(20)
            message = ""
        elif "hbrit" in message.lower():
            pyautogui.scroll(-20)
            message = ""
        elif "eat" in message.lower():
            pyautogui.mouseDown(button='right')
            message = ""
            time.sleep(3)
            pyautogui.mouseUp(button='right')
        elif "use" in message.lower():
            pyautogui.click(button='right')
            message = ""
        elif "inv" in message.lower():
            keyboard.press('e')
            time.sleep(0.01)
            keyboard.release('e')
            message = ""
        elif "sprint" in message.lower():
            pyautogui.mouseUp(button='middle')
            time.sleep(0.01)
            pyautogui.mouseDown(button='middle')
            time.sleep(0.01)
            pyautogui.mouseUp(button='middle')
            time.sleep(0.01)
            pyautogui.mouseDown(button='middle')
            message = ""
        elif "respawn" in message.lower():
            pyautogui.moveTo(665,640)
            pyautogui.click(button='left')
            message = ""
        elif "rejoin" in message.lower():
            pyautogui.moveTo(655,650)
            pyautogui.click(button='left')
            pyautogui.moveTo(655,660)
            pyautogui.click(button='left')
            pyautogui.moveTo(655,670)
            pyautogui.click(button='left')
            pyautogui.moveTo(655,680)
            pyautogui.click(button='left')
            pyautogui.moveTo(655,690)
            pyautogui.click(button='left')
            pyautogui.moveTo(400,200)
            pyautogui.doubleClick(button='left')
            message = ""
        elif "jump" in message.lower():
            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
            message = ""
        elif "climb" in message.lower():
            pyautogui.mouseDown(button='middle')
            keyboard.press(Key.up)
            time.sleep(0.1)
            keyboard.release(Key.up)
            pyautogui.mouseUp(button='middle')
            message = ""
        elif "swim" in message.lower():
            keyboard.press(Key.up)
            message = ""
        elif "sink" in message.lower():
            keyboard.release(Key.up)
            message = ""
        elif "sneak" in message.lower():
            message = ""
            
        else:
            pass

def twitch():
    def joinchat():
        Loading = True
        while Loading:
            readbuffer_join = irc.recv(1024)
            readbuffer_join =  readbuffer_join.decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                Loading = loadingComplete(line)
    def loadingComplete(line):
        if ("End of /NAMES list" in line):
            print("Bot has joined " + CHANNEL + "'s Channel!")
            sendMessage(irc, "Bot Joined sucsessfully")
            return False
        else:
            return True
    def sendMessage(irc, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((messageTemp + "\n").encode())
    def getUser(line):
        seperate = line.split(":", 2)
        user = seperate[1].split("!", 1)[0]
        print(user)
        return user
    def getMessage(line):
        global message
        try: 
            message = (line.split(":",2))[2]
        except:
            message = ""
        return message
    def Console(line):
        if "PRIVMSG" in line:
            return False
        else:
            return True

    joinchat()
    while True:
        try: 
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            elif "PING" in line and Console(line):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(msgg)
                print(msgg)
                continue
            else:
                print(line)
                user = getUser(line)
                message = getMessage(line)
                print(user + " : " + message)

if __name__ =='__main__':
    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gamecontrol)
    t2.start()

