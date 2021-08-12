from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import *
from numpy import *
from socket import *
import threading
from random import randint

s = None
# shost = socket.gethostname()
# ip = socket.gethostbyname(shost)
host = '127.0.0.1'
client_started = False
server_started = False
port = randint(1024,65535)
port = 1024
stop = None
s = None
reciever_thread  = None
ipport = None
name = "Client"
addr = None
# ip = socket.gethostbyname(socket.gethostname())
conn = None

def toggleClient():
    global s,client_started,stop,reciever_thread,ipport,conn
    if client_started == False:
        stop = False
        # s = socket(AF_INET , SOCK_DGRAM )
        s = socket()
        s.connect((host, port))
        client_started = True
        reciever_thread = threading.Thread( target = recieve)
        reciever_thread.start()
        print("started")

    elif client_started == True:
        stop = True
        s.close()
        reciever_thread.join()
        client_started = False
    return

# s.send(name.encode())
# s_name = s.recv(1024)
# s_name = s_name.decode()
# print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

# while True:
#     message = s.recv(1024)
#     message = message.decode()
#     print("Server :", message)
    # message = input(str("Me : "))
    # s.send(message.encode())
def send():
    global name , conn
    message = "{}  : {}".format(name,inputbox.get())
    inputbox.delete(0,END)
    chat.insert(INSERT,message + "\n")
    # s.sendto(message.encode() , (serveripentry.get(),int(serverportentry.get())))
    s.send(message.encode())

def recieve():
    global stop , conn ,s , addr
    while stop == False:
        message = s.recv(1024)
        chat.insert(INSERT,message.decode() + "\n")

root = Tk()
root.title("TCP Chat App")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(2,weight=1)
button1 = Button(root, text="Connect Client",command = toggleClient)
# clientstatus = Label(root, text = "Connected")
serverip = Label(root, text = "IP:")
serveripentry = Entry(root)
serveripentry.insert(INSERT,"127.0.0.1")
serverport = Label(root, text = "Port:")
serverportentry = Entry(root)
serverportentry.insert(INSERT,"1024")
# serverstatus = Label(root, text = "Connected")
chat = Text(root)
inputbox = Entry(root)
send = Button(root, text="Send",command = send)
button1.grid(row = 0, column = 0 , columnspan= 2, sticky = N+S+W+E, pady = 2)
# clientstatus.grid(row = 0, column = 2 ,columnspan= 2, sticky = N+S+W+E, pady = 2)
serverip.grid(row = 1, column = 0 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serveripentry.grid(row = 1, column = 1 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverport.grid(row = 1, column = 2 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverportentry.grid(row = 1, column = 3 , columnspan= 1, sticky = N+S+W+E, pady = 2)
# serverstatus.grid(row = 1, column = 4 , columnspan= 1, sticky = N+S+W+E, pady = 2)
chat.grid(row = 2, column = 0, columnspan = 4 , sticky = N+S+E+W, pady = 2)
inputbox.grid(row = 3, column = 0, columnspan = 3 ,sticky = W+E, pady = 2)
send.grid(row = 3, column = 3, sticky = W+E, pady = 2)
root.mainloop()
