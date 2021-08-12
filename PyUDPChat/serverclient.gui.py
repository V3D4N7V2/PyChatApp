from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import *
from numpy import *
from socket import *
import threading
from random import randint
import os
# s = None
port = randint(1024,65535)
server_started = False
name = "test"
stop = False
x2 = None
ipport = ""
def server():
    global s,server_started,stop,x2,ipport
    if server_started == False:
        stop = True
        s = socket(AF_INET , SOCK_DGRAM )
        # s.bind(('',int(serverportentry.get())))
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
    

def send():
    message = "{}  : {}".format(name,inputbox.get())
    inputbox.delete(0,END)
    s.sendto(message.encode() , (serveripentry.get(),int(serverportentry.get())))

def rec():
    global stop
    while stop == False:
        msg = s.recvfrom(1024)
        chat.insert(INSERT,msg[0].decode() + "\n")

root = Tk()
root.title("Chat App " + ipport)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.rowconfigure(2,weight=1)
button1 = Button(root, text="Toggle Server",command = server)
# button2 = Button(root, text="Client",command = client)
serverip = Label(root, text = "IP:")
serveripentry = Entry(root)
serveripentry.insert(INSERT,"127.0.0.1")
serverport = Label(root, text = "Port:")
serverportentry = Entry(root)
# serverportentry.insert(INSERT,"1337")
# serverstatus = Label(root, text = "Connected ?")
chat = Text(root)
# chat.insert(INSERT,"client : Hi\nserver : ok\nclient : ok\n")
# chat.insert(INSERT,"client : Hi\nserver : ok\nclient : ok")
inputbox = Entry(root)
send = Button(root, text="Send",command = send)
button1.grid(row = 0, column = 0 , columnspan= 2, sticky = N+S+W+E, pady = 2)
# button2.grid(row = 0, column = 2 ,columnspan= 2, sticky = N+S+W+E, pady = 2)
serverip.grid(row = 1, column = 0 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serveripentry.grid(row = 1, column = 1 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverport.grid(row = 1, column = 2 , columnspan= 1, sticky = N+S+W+E, pady = 2)
serverportentry.grid(row = 1, column = 3 , columnspan= 1, sticky = N+S+W+E, pady = 2)
# serverstatus.grid(row = 1, column = 4 , columnspan= 1, sticky = N+S+W+E, pady = 2)
chat.grid(row = 2, column = 0, columnspan = 4 , sticky = N+S+E+W, pady = 2)
inputbox.grid(row = 3, column = 0, columnspan = 3 ,sticky = W+E, pady = 2)
send.grid(row = 3, column = 3, sticky = W+E, pady = 2)
root.mainloop()












def issue():
    file = read_excel('database.xlsx')
    serial_no=int(sne.get())
    roll=rne.get()
    name=ne.get()
    # print(len(file.index[file['Sr No.'] == serial_no].values)==0)
    if(len(file.index[file['Sr No.'] == serial_no].values)==0):
        print("\nSerial Number Not Exists\n")
        messagebox.showinfo("Error","Serial Number Not Exists")
        return
    if (file.loc[file['Sr No.']==serial_no,'issued'].to_string(index=False) ==" Yes"):
        print("\nAlready Issued\n")
        messagebox.showinfo("Error","Already Issued")
        return
    file.loc[file['Sr No.']==serial_no,'issued_by'] = roll
    file.loc[file['Sr No.']==serial_no,'issue_date'] = (datetime.now().date())
    file.loc[file['Sr No.']==serial_no,'return_date'] = (datetime.now().date()+ timedelta(days=14))
    file.loc[file['Sr No.']==serial_no,'issuer_name'] = name
    file.loc[file['Sr No.']==serial_no,'issued'] = "Yes"
    file.to_excel('database.xlsx', index=False)
    messagebox.showinfo("Done","Done Issueing")

def rturn():
    file = read_excel('database.xlsx')
    serial_no=int(sne.get())
    if(len(file.index[file['Sr No.'] == serial_no].values)==0):
        print("\nSerial Number Not Exists\n")
        messagebox.showinfo("Error","Serial Number Not Exists")
        return
    if (file.loc[file['Sr No.']==serial_no,'issued'].to_string(index=False) ==" No"):
        print("\nAlready In Library\n")
        messagebox.showinfo("Error","Already In Library")
        return
    delta = datetime.strptime(file.loc[file['Sr No.']==serial_no,'return_date'].to_string(index=False), '%Y-%m-%d') - datetime.now()
    delta = int(delta.days)
    fine = abs(delta*10)
    if (delta>0):
        messagebox.showinfo("Late Fine","Late Return Fine : " + str(fine) + " Rs")
    file.loc[file['Sr No.']==serial_no,'issued_by'] = nan
    file.loc[file['Sr No.']==serial_no,'issue_date'] = nan
    file.loc[file['Sr No.']==serial_no,'return_date'] = nan
    file.loc[file['Sr No.']==serial_no,'issuer_name'] = nan
    file.loc[file['Sr No.']==serial_no,'issued'] = "No"
    file.to_excel('database.xlsx', index=False)
    messagebox.showinfo("Done","Done Returning")
    
def adnew():
    file = read_excel('database.xlsx')
    serial_no=int(sne.get())
    book=bne.get()
    if(len(file.index[file['Sr No.'] == serial_no].values)!=0):
        print("\nSerial Number Already Exists\n")
        messagebox.showinfo("Error","Already Already Exists")
        return
    new_row = {'Sr No.':serial_no, 'book_name':book,'issued':"No"}
    file = file.append(new_row, ignore_index=True)
    file.to_excel('database.xlsx', index=False)
    messagebox.showinfo("Done","Done Adding")
    
def rmold():
    file = read_excel('database.xlsx')
    serial_no=int(sne.get())
    file = file.drop(index=file.index[file['Sr No.'] == serial_no].values)
    file.to_excel('database.xlsx', index=False)
    messagebox.showinfo("Done","Done Removing")
    
def renIssue(): 
    global sne,rne,ne,bne
    if len(root.winfo_children()) > 5:
        root.winfo_children()[5].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 5, sticky = W, pady = 2)
    
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)
    
    rnl = Label(frame, text = "Roll No.") 
    rne = Entry(frame) 
    rnl.grid(row = 1, column = 0, sticky = W, pady = 2)
    rne.grid(row = 1, column = 1, sticky = W, pady = 2)

    nl = Label(frame, text = "Name") 
    ne = Entry(frame) 
    nl.grid(row = 2, column = 0, sticky = W, pady = 2)
    ne.grid(row = 2, column = 1, sticky = W, pady = 2)

    ok = Button(frame, text="OK",command = issue)
    ok.grid(row = 3, column = 0, columnspan = 4 ,sticky = W, pady = 2)
    
def renRet():
    global sne,rne,ne,bne
    if len(root.winfo_children()) > 5:
        root.winfo_children()[5].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 5, sticky = W, pady = 2)
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)
    
    ok = Button(frame, text="OK",command = rturn)
    ok.grid(row = 1, column = 0, columnspan = 4 ,sticky = W, pady = 2)
    
def renNew():
    global sne,rne,ne,bne
    if len(root.winfo_children()) > 5:
        root.winfo_children()[5].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 5, sticky = W, pady = 2)
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)
    
    bnl = Label(frame, text = "Book Name")
    bne = Entry(frame) 
    bnl.grid(row = 1, column = 0, sticky = W, pady = 2)
    bne.grid(row = 1, column = 1, sticky = W, pady = 2)

    ok = Button(frame, text="OK",command = adnew)
    ok.grid(row = 2, column = 0, columnspan = 4 ,sticky = W, pady = 2)
 
def renDel():
    global sne,rne,ne,bne
    if len(root.winfo_children()) > 5:
        root.winfo_children()[5].destroy()
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 5, sticky = W, pady = 2)
    snl = Label(frame, text = "Serial No.")
    sne = Entry(frame)
    snl.grid(row = 0, column = 0, sticky = W, pady = 2)
    sne.grid(row = 0, column = 1, sticky = W, pady = 2)

    ok = Button(frame, text="OK",command = rmold)
    ok.grid(row = 1, column = 0, columnspan = 4 ,sticky = W, pady = 2)

def show():
    global sne,rne,ne,bne
    if len(root.winfo_children()) > 5:
        root.winfo_children()[5].destroy()
    file = read_excel('database.xlsx')
    frame = Frame(root)
    frame.grid(row = 2, column = 0, columnspan = 5, sticky = W, pady = 2)
    snl = Label(frame, text = file.to_string(index=False))
    snl.grid(row = 0, column = 0, columnspan = 5, sticky = W, pady = 2)
   