from tkinter import *
import subprocess
import sys
import os
from tkinter import messagebox
import webbrowser

def exit1():
    root.quit()
    root.destroy()

def help1():
    lines = ('POEC Mining suite', '', 'http://www.poeight.net/', '', '© Piece of Eight 2018 all rights reserved')
    msg = messagebox.showinfo('About', "\n".join(lines))

def help2():
    lines = ('Getting started', '', '1) Type in your mining pool address. Leave out the "-o stratum+tcp://" part.' , '')
    lines1 = ('2) Type in the receiving wallet address.','')
    lines2 = ('3) Type in the password used, this can be anything. Don''t leave it blank.', '')
    #lines3 = ('4) Add in any other optional parameters.', '')
    msg = messagebox.showinfo('Help', "\n".join(lines + lines1 + lines2))

def hyperlink():
     webbrowser.open_new(r"http://www.poeight.net/")

def hyperlink2():
    webbrowser.open_new(r"http:209.97.185.191:3001/")
    
    

if __name__ == "__main__":

    root = Tk()
    root.title('POEC Mining suite v1.0')
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    helpmenu = Menu(menubar, tearoff=0)

    def reload():
        python = sys.executable
        os.execl(python, python, * sys.argv)
              
        
    filemenu.add_command(label="Reload", command=reload)
    filemenu.add_command(label="Exit", command=exit1)
    helpmenu.add_command(label="About", command=help1)
    helpmenu.add_command(label="Help", command=help2)
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="About", menu=helpmenu)

    setup = LabelFrame(root, text = "Setup")
    setup.pack(fill = "both", expand = "yes")


 
    stratum = Label(setup, text="Stratum:").place(x = 30, y = 10)
    stratum1 = Entry()
    stratum1.insert(0, "Enter the stratum address + port (E.g. 1.domain.com:port)")
    stratum1.place(x = 90, y = 29, width = 350)

    wallet = Label(setup, text="Wallet:").place(x = 30, y = 40)
    wallet1 = Entry()
    wallet1.place(x = 90, y = 59, width = 350)

    password = Label(setup, text="Pass:").place(x = 30, y = 70)
    password1 = Entry()
    password1.place(x = 90, y = 89, width = 350)

    #extra = Label(setup, text="Params:").place(x = 30, y = 100)
    #extra = Entry()
    #extra.place(x = 90, y = 120, width = 350)

 
    def edit():
        with open('poec.bat', 'wt') as f:
            if not stratum1.get():
                msg = messagebox.showerror("Error", "Please fill out the stratum box, including the port number.")
            else:
                f.write("ccminer-x64 -a scrypt -o stratum+tcp:/")
                f.write("/" + stratum1.get())
            if not wallet1.get():
                msg = messagebox.showerror("Error", "Please fill out the wallet box.")
            else:
                f.write(" -")
                f.write("u " + wallet1.get())
            if not password1.get():
                msg = messagebox.showerror("Error", "Please fill out the password box, type in x if not required.")
            else:
                    
                f.write(" -")
                f.write("p " + password1.get())
                f.close()

    def start():
        if not stratum1.get():
            msg = messagebox.showerror("Error", "Please fill out the stratum box, including the port number.")
        if not wallet1.get():
            msg = messagebox.showerror("Error", "Please fill out the wallet box.")
        if not password1.get():
            msg = messagebox.showerror("Error", "Please fill out the password box, type in x if not required.")
        else:
            subprocess.call([r'poec.bat'])
        

    save = Button(text = "Save batch file", command = edit).place(x=120, y = 200)
    save = Button(text = "Start Miner", command = start).place(x=220, y = 200)
    help = Button(text = "Need help?", command = help2).place(x=460, y = 25)
    Poeight = Button(text = "Poeight.net", command = hyperlink).place(x=460, y = 70)
    blockexplorer = Button(text = "Block Explorer", command = hyperlink2).place(x=460, y = 120)



    def on_closing():
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            root.quit()
            root.destroy()
            sys.exit()
            exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.geometry('580x380')
    root.iconbitmap('coin.ico')
    root.resizable(False, False)
    root.config(menu=menubar)
    root.mainloop()
