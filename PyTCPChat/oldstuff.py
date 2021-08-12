


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
   