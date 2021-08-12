from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import *
from numpy import *
import os
server_started = False
stop 
def toggleServer():
    global server_started
    if server_started == True:
        server_started = False
    elif server_started == False:
        server_started = True
    return

def send():
    message = "{}  : {}".format(name,inputbox.get())
    inputbox.delete(0,END)
    s.sendto(message.encode() , (serveripentry.get(),int(serverportentry.get())))

def recieve():
    global stop
    while stop == False:
        msg = s.recvfrom(1024)
        chat.insert(INSERT,msg[0].decode() + "\n")

def server():
    global s,server_started,stop,x2,ipport
    if server_started == False:
        stop = True
        s = socket(AF_INET , SOCK_DGRAM )
        s.bind(('',port))
        print("started")
        x2 = threading.Thread( target = rec)
        x2.start()
        server_started = True
        ipport = "(127.0.0.1:" + str(port) + ")"
    elif server_started == True:
        x2.join()
        s.shutdown(SHUT_RDWR)
        s.close()
        server_started = False
        print("Stopped")
        ipport = ""
    global root
    root.title("Chat App " + ipport)
    return
    




root = Tk()
root.title("TCP Chat App")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(2,weight=1)
button1 = Button(root, text="Toggle Server",command = toggleServer)
serverstatus = Label(root, text = "Connected")
serverip = Label(root, text = "IP:")
serveripentry = Entry(root)
serveripentry.insert(INSERT,"127.0.0.1")
serverport = Label(root, text = "Port:")
serverportentry = Entry(root)
serverportentry.insert(INSERT,"1337")
chat = Text(root)
inputbox = Entry(root)
send = Button(root, text="Send",command = send)
button1.grid(row = 0, column = 0 , columnspan= 2, sticky = N+S+W+E, pady = 2)
serverstatus.grid(row = 0, column = 2 ,columnspan= 2, sticky = N+S+W+E, pady = 2)
serverip.grid(row = 1, column = 0 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serveripentry.grid(row = 1, column = 1 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverport.grid(row = 1, column = 2 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverportentry.grid(row = 1, column = 3 , columnspan= 1, sticky = N+S+W+E, pady = 2)
# serverstatus.grid(row = 1, column = 4 , columnspan= 1, sticky = N+S+W+E, pady = 2)
chat.grid(row = 2, column = 0, columnspan = 4 , sticky = N+S+E+W, pady = 2)
inputbox.grid(row = 3, column = 0, columnspan = 3 ,sticky = W+E, pady = 2)
send.grid(row = 3, column = 3, sticky = W+E, pady = 2)
root.mainloop()
