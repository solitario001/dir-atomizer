from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
from subprocess import Popen, PIPE
from tkinter import messagebox
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def origem ():
       arquivo = open ('src.txt','w+')
       path = filedialog.askdirectory()
       arquivo.writelines(path)
       arquivo.close()
       if os.stat('src.txt').st_size > 0:
        messagebox.showinfo(message='New origin path saved in src.txt')
    
def destino ():
     arquivo = open ('dst.txt','w+')
     path = filedialog.askdirectory()
     arquivo.writelines(path)
     arquivo.close()
     if os.stat('dst.txt').st_size > 0:
      messagebox.showinfo(message='New destiny path saved in dst.txt')

def memoria():
    with open ('memory.txt','w+') as arquivo2:
     name = name_var.get()
     arquivo2.writelines(name)
     if os.path.exists('memory.txt'): 
         messagebox.showinfo(message='New value saved in memory.txt')

def site():
 webbrowser.open("https://github.com/solitario001/dir-atomizer")  
 

root = Tk()
root.title('dir-atomizer')
name_var=StringVar()
name_var2=StringVar()
ttk.Button(root, text='Source folder',padding="50 0 30 5", command=origem).grid()
ttk.Button(root, text='Target folder',padding="50 0 30 5", command=destino).grid()
myimg = ImageTk.PhotoImage(Image.open(resource_path("fran.png")))
ttk.Button(root,image=myimg,command=site).grid()
ttk.Label(root, text='Choose the source folder you want to move').grid(column=1, row=0,sticky=W)  
ttk.Label(root, text='Choose destination folder').grid(column=1, row=1,sticky=W)
ttk.Label(root, text='Current value :').grid(column=0, row=3,sticky=E)
sub_btn=ttk.Button(root,text = 'New value', command = memoria).grid(column=1, row=2,sticky=W)
name_entry = ttk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')).grid(column=1, row=2,sticky=E)

root.geometry('650x320-1500+800')


if os.path.exists('memory.txt'):
    if os.stat('memory.txt').st_size > 0:  
     with open ('memory.txt') as memory:
      data = memory.read()
      atual = ttk.Label(root, text=data).grid(column=1,row=3,sticky=W)


root.mainloop()
