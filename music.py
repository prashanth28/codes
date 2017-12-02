import pygame
import threading
import os
import sys
from mutagen.mp3 import MP3
from tkinter import *
from tkinter.filedialog import askdirectory
root = Tk()
root.configure(background="black")
root.iconbitmap("icon.ico")
root.title("PLAY")
root.geometry("640x360")
f=Frame(root,highlightthickness=0,bg="grey",bd=0)
f.pack(side=BOTTOM,fill=X)
label=Label(f,bg='grey',fg='black')
label1=Label(f,bg="grey",fg="black")
global index
listofsongs = []
index = 0
x = 0
h=0
global stopbutton
def nextsong(event):
    global index
    global x
    x=2
    index += 0
    if(index>=len(listofsongs)):
       index=0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    label.config(text=str(listofsongs[index]))
def prevsong(event):
    global index
    global x
    x=2
    index -= 2
    if(index<0):
       index=len(listofsongs)-1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    label.config(text=str(listofsongs[index]))
def stopsong(event):
    global x
    global index
    global h
    if x == 2:
        pygame.mixer.music.pause()
        x -= 1
    elif x == 0:
        h=1
        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        label.config(text=str(listofsongs[index]))
        x +=2
    elif x==1:
        pygame.mixer.music.unpause()
        x+=1
def directorychooser():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
    for i in range(len(listofsongs)):
        lisbox.insert(END,listofsongs[i])
#def autochange():
 #   while True:
  #      label1.config(text=('%.2f'%(pygame.mixer.music.get_pos()/60000)))
def peep():
    while True:
        try:
            pygame.mixer.init()
            if( pygame.mixer.music.get_busy()==True):                
                x=('%.2f'%((pygame.mixer.music.get_pos()/60000)*0.6))
                label1.config(text=str(x))
        except:
            pygame.quit()
            pass
def autoplay():
    global index
    global h
    while True:
        try:
            if(pygame.mixer.music.get_busy()==False):
                if(h==1):
                    audio = MP3(listofsongs[index])
                    z = audio.info.length*1000
                    pygame.mixer.music.load(listofsongs[index])
                    label.config(text=str(listofsongs[index]))
                    index+=1
                    pygame.mixer.music.play()
        except:
            pass
def playsong(event):
    global x
    global index
    global m
    m = 0 
    x = 0
    a=lisbox.curselection()
    index=a[0]
    stopsong(event)
def exitsys(event):
    pygame.quit()
    root.destroy()
lisbox = Listbox(root,bg="black",bd=0,selectbackground='grey',selectforeground='black'
                 ,relief='flat',fg="grey",highlightthickness=0)
lisbox.bind("<Double-1>",playsong)
lisbox.pack(expand=True,anchor=CENTER,fill=BOTH)
ma=PhotoImage(file="img\\images (5).png")
ma1=ma.subsample(2,2)
mb=PhotoImage(file="img\\images (4).png")
mb1=mb.subsample(2,2)
mc=PhotoImage(file="img\\images (11).png")
mc1=mc.subsample(2,2)
md=PhotoImage(file="img\\image (3).png")
md1=md.subsample(3,3)
nextbutton = Button(f,image=ma1,relief='flat',bg="grey",fg="black")
nextbutton.bind("<Button>",nextsong)
root.bind("<KeyPress - Right>", nextsong)
nextbutton.pack(side=RIGHT,fill= BOTH)
stopbutton = Button(f,image=mc1,bg="grey",fg="white",relief='flat')
stopbutton.bind("<Button>",stopsong)
root.bind("<KeyPress - space>" ,stopsong)
stopbutton.pack(side=RIGHT,fill= BOTH)
previousbutton = Button(f,image=mb1,relief='flat',bg="grey",fg="black")
previousbutton.bind("<Button>",prevsong)
root.bind("<KeyPress - Left>", prevsong)
previousbutton.pack(side=RIGHT,fill= BOTH)
importbutton = Button(f,image=md1,width=50,bg="grey",fg="black",relief='flat',command = directorychooser)
importbutton.pack(side=LEFT,fill= BOTH)
label.pack(side=LEFT,anchor=W,fill=BOTH)
label1.pack(side=RIGHT,anchor=E,fill=BOTH)
root.bind("<KeyPress - Escape>",exitsys)
m=0
if (m==0):
    thread1 = threading.Thread(target=peep,args=())
    thread1.start()
    thread2 = threading.Thread(target=autoplay,args=())
    thread2.start()
    m=1
root.mainloop()
