import pywinhandle as py
import tkinter as tk
import psutil
import threading

gamelist=[]

def M_DelProcess():
    D2RL=[]
    try:
        D2RL= py.find_handles_key(None,'D2R','DiabloII Check For Other Instances')
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

def process_del():
    PD=threading.Thread(target=M_DelProcess,daemon=True)
    PD.start()

def find_game():
    global gamelist
    Chgamelist=[]
    for p in psutil.process_iter(['pid','name']):
        if p.info['name'] == 'D2R.exe':
            pid=p.info['pid']
            Chgamelist.append(pid)
    if len(Chgamelist) != len(gamelist):
        gamelist=Chgamelist
        process_del()
    Var_Ltext.set('DiabloII:'+str(len(gamelist)))
    win.after(1000,find_game)

def Winclose():
    win.destroy()

def WinstartMove(event):
    global oldx,oldy
    oldx=event.x
    oldy=event.y

def WinMove(event):
    global Win_size,oldx,oldy
    win.geometry('{}+{}+{}'.format('150x40',event.x-oldx+win.winfo_x(),event.y-oldy+win.winfo_y()))
win=tk.Tk()
win.title('多窗小工具')
win.geometry('150x40')
win.resizable(0,0)
win.attributes('-toolwindow',2)
win.attributes("-topmost", 1)
win.overrideredirect(1)

Var_Ltext=tk.StringVar()
Var_Ltext.set('DiabloII：`0',)
Ltext=tk.Label(win,textvariable=Var_Ltext,font=('Algerian',16))
Ltext.place(x=25,y=5)

B_Exit=tk.Button(win,text='X',relief='groove',bg='Linen',command=Winclose)
B_Exit.place(x=5,y=7)

win.bind("<ButtonPress-1>", WinstartMove)
win.bind('<B1-Motion>',WinMove)


find_game()
win.mainloop()