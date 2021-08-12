from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import *
from numpy import *
from socket import *
import threading
from random import randint
import os

server_started = False
port = randint(1024,65535)
port = 1024
stop = None
s = None
reciever_thread  = None
ipport = None
name = "Server"
addr = None
# ip = socket.gethostbyname(socket.gethostname())
conn = None

def toggleServer():
    global s,server_started,stop,reciever_thread,ipport,conn
    if server_started == False:
        stop = False
        # s = socket(AF_INET , SOCK_DGRAM )
        s = socket()
        s.bind(('',port))
        server_started = True
        # time.sleep(1)
        reciever_thread = threading.Thread( target = recieve)
        reciever_thread.start()
        print("started")

    elif server_started == True:
        stop = True
        # time.sleep(1)
        s.close()
        server_started = False
        reciever_thread.join()
    return

def send():
    global name , conn 
    message = "{}  : {}".format(name,inputbox.get())
    inputbox.delete(0,END)
    chat.insert(INSERT,message + "\n")
    # s.sendto(message.encode() , (serveripentry.get(),int(serverportentry.get())))
    conn.send(message.encode())

def recieve():
    global stop , conn ,s , addr ,serverstatus
    s.listen(1)
    conn, addr = s.accept()
    serverstatus = Label(root, text = "Connected")
    while stop == False:
        msg = conn.recv(1024)
        chat.insert(INSERT,msg.decode() + "\n")
toggleServer()
root = Tk()
root.title("TCP Chat App")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(2,weight=1)
button1 = Button(root, text="Toggle Server",command = toggleServer)
# serverstatus = Label(root, text = "Not connected")
serverip = Label(root, text = "IP:")
serveripentry = Entry(root)
serveripentry.insert(INSERT,"127.0.0.1")
serverport = Label(root, text = "Port:")
serverportentry = Entry(root)
serverportentry.insert(INSERT,str(port))
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

# def server():
#     global s,server_started,stop,reciever_thread,ipport
#     if server_started == False:
#         stop = True
#         s = socket(AF_INET , SOCK_DGRAM )
#         s.bind(('',port))
#         print("started")
#         reciever_thread = threading.Thread( target = rec)
#         reciever_thread.start()
#         server_started = True
#         ipport = "(127.0.0.1:" + str(port) + ")"
#     elif server_started == True:
#         reciever_thread.join()
#         s.shutdown(SHUT_RDWR)
#         s.close()
#         server_started = False
#         print("Stopped")
#         ipport = ""
#     global root
#     root.title("Chat App " + ipport)
#     return
    

