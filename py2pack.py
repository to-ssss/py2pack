import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.filedialog
import os
import sys

'''
def mess1():
    messagebox.showinfo("","开发中")
'''

def path1():
    global path11
    patha=tkinter.filedialog.askopenfilename()
    path11.set(patha)

def path2():
    global path21
    pathb=tkinter.filedialog.askopenfilenames()
    path21.set(pathb)

def path3():
    global path31
    pathc=tkinter.filedialog.askopenfilename()
    path31.set(pathc)

def pack(): 
    global vc11,vc12,path11,path21,fn1,fn2,fn3,path31,fn4
    os.chdir(path11.get().rsplit("/",1)[0])
    ev=path21.get().split(" ")
    if (vc11.get()==True):fn1=" -F"
    else:fn1=""
    if (vc12.get()==True):fn2=" -w"
    else:fn2=""  
    if (path21.get()==""):fn3="" 
    else:   
        for i in range(len(ev)):
            ev[i]='--add-data="'+ev[i].split("'")[1]+';."'
            evy=",".join(ev)
        fn3=evy
    if (path31.get()==""):fn4=""
    else:fn4=' -i="'+path31.get()+'"'
    os.system("start pyinstaller"+" "+path11.get().rsplit("/",1)[1]+fn1+fn2+" "+fn3+fn4)

def show1():
    global l12,e12,b13
    if (vc11.get()==False):
        l12.grid_forget()
        e12.grid_forget()
        b13.grid_forget()
    else:      
        l12.grid(row=2,column=0,sticky="w")
        e12.grid(row=2,column=1,ipadx=100)
        b13.grid(row=2,column=2)

    

def center_window(w,width,height):
    screenwight=w.winfo_screenwidth()
    screenheight=w.winfo_screenheight()
    size="%dx%d+%d+%d"%(width,height,(screenwight-width)/2,(screenheight-height)/3)
    w.geometry(size)

def get_resource_path(relative_path):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__=='__main__':
    window=tk.Tk()
    window.title("python打包器")
    window.resizable(0,0)
    center_window(window,485,200)
    path11=tk.StringVar()
    path21=tk.StringVar()
    path31=tk.StringVar()
    vc11=tk.BooleanVar()
    vc12=tk.BooleanVar()
    fn1,fn2,fn3,fn4="","","",""

    l11=tk.Label(window,text="程序文件位置:")
    l11.grid(row=0,column=0,sticky="w")
    e11=tk.Entry(window,textvariable=path11)
    e11.grid(row=0,column=1,ipadx=100)
    b11=tk.Button(window,width=7,text="选择文件",command=path1)
    b11.grid(row=0,column=2)

    l12=tk.Label(window,text="其他文件位置:")
    e12=tk.Entry(window,textvariable=path21)        
    b13=tk.Button(window,width=7,text="选择文件",command=path2)  

    l13=tk.Label(window,text="图标位置:")
    l13.grid(row=1,column=0,sticky="w")
    e13=tk.Entry(window,textvariable=path31)
    e13.grid(row=1,column=1,ipadx=100)
    b14=tk.Button(window,width=7,text="选择文件",command=path3)
    b14.grid(row=1,column=2)

    b12=tk.Button(window,width=7,text="打包",command=pack)
    b12.grid(row=5,column=1)

    c11=tk.Checkbutton(window,text="打包成单个可执行文件",variable=vc11,command=show1)
    c11.grid(row=3,column=0,columnspan=2,sticky="w")
    c12=tk.Checkbutton(window,text="执行时不带命令窗口",variable=vc12)
    c12.grid(row=4,column=0,columnspan=2,sticky="w")
    window.mainloop()
