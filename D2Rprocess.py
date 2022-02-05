import pywinhandle as py
import tkinter as tk
import psutil
import threading
from time import sleep
gamelist=[]
NameList={}
Mrun=0

Att=1

def M_DelProcess(name):
    global Mrun
    #sleep(1)
    try:
        D2RL=py.find_handles_key(None,name,'DiabloII Check For Other Instances')
    except:
        pass
    if D2RL != 'None':
        try:
            py.close_handle(D2RL['process_id'],D2RL['handle'])
            print('closed')
        except:
            pass
    else:
        print('no find')
    Mrun-=1
    if Mrun==0:
        Ltext.config(foreground='black')


def process_del(NameList):
    global Mrun
    if Mrun==0:
        for name in NameList:
            L=[name]
            PD=threading.Thread(target=M_DelProcess,args=(L),daemon=True)
            PD.start()
            Mrun+=1

def find_game():
    global gamelist,NameList
    Chgamelist=[]
    NameList={}
    ExEname=Var_entry.get().split(',')
    for p in psutil.process_iter(['pid','name']):
        a=p.info['name'].split('.')
        if a[0] in  ExEname:
            pid=p.info['pid']
            Chgamelist.append(pid)
            NameList[a[0]]=a[0]
    if len(Chgamelist) > len(gamelist):
        Ltext.config(foreground='Red')
        process_del(NameList)
    gamelist=Chgamelist
    Var_Ltext.set('Find DiabloII：{} Game'.format(str(len(gamelist))))
    win.after(100,find_game)

def Winclose():
    win.destroy()

def WinstartMove(event):
    global oldx,oldy
    oldx=event.x
    oldy=event.y

def WinMove(event):
    global Win_size,oldx,oldy
    win.geometry('{}+{}+{}'.format('552x30',event.x-oldx+win.winfo_x(),event.y-oldy+win.winfo_y()))

def Winattributes(event):
    global Att
    Att=abs(Att-1)
    if Att==0:
        win.attributes('-alpha', 0.5)
    else:
         win.attributes('-alpha', 1)

win=tk.Tk()
win.title('多窗小工具')
win.resizable(0,0)
win.attributes('-toolwindow',2)
win.attributes("-topmost", 1)


win.overrideredirect(1)

lab1=tk.Label(win,text="  Input D2rGameName：")
Var_entry=tk.StringVar()

Entry=tk.Entry(win,textvariable=Var_entry,width=20)
Entry.insert(0,'D2R,D2RB')

Var_Ltext=tk.StringVar()
Var_Ltext.set('Find DiabloII：0 Game',)


Ltext=tk.Label(win,textvariable=Var_Ltext,font=('Algerian',16))
Ltext.grid(
    row=0,
    column=1,
    )

B_Exit=tk.Button(win,text='X',relief='groove',bg='Linen',command=Winclose)
B_Exit.grid(
    row=0,
    column=0,
    sticky='w',padx=2)

lab1.grid(
    row=0,
    column=3
    )

Entry.grid(
    row=0,
    column=4,padx=2
    )

Ltext.bind("<ButtonPress-1>", WinstartMove)
Ltext.bind('<B1-Motion>',WinMove)
lab1.bind("<ButtonPress-1>", WinstartMove)
lab1.bind('<B1-Motion>',WinMove)
win.bind("<Button-3>", Winattributes)

find_game()

win.mainloop()