import time

import threading
from tkinter import *
import datetime
def timerupdate():
    i=60
    while i!=0:
        timerval.set(f"{i}")
        canvas.pack()
        root.after(1000,root.update())
        i=i-1
        
    
        
def timer(sno,state,signalcolor):
    
    i=60
    threadname=threading.current_thread().getName()
    
    
    while i!=0:
        
            
        print(f" {i} ")
        
        
            
        if i==5 and state=="green" and sno<len(Signals):
               
                print()
                print(f"|  SIGNAL {sno} YELLOW SIGNAL SLOW DOWN  \n")
                
                
                
                canvas.itemconfig(Signals[sno-1][2],fill='grey')
                canvas.itemconfig(Signals[sno-1][1],fill='yellow')
                canvas.itemconfig(Signals[sno][0],fill='grey')              
##              canvas.itemconfig(Signals[sno][1],fill='yellow')
                canvas.pack()
                #root.update()
                root.after(2000, root.update())
                
                canvas.itemconfig(Signals[sno-1][1],fill='grey')
                #canvas.itemconfig(Signals[sno][1],fill='grey')
                canvas.pack()
                root.update()

        time.sleep(1)
        
        
        i-=1
        
    print()
    
def signal(signalno,state,signalcolor):
    
        
    if state=="red":
        print(f"|  SIGNAL {signalno} RED SIGNAL STOP  \n")
        
        timer(signalno,state,signalcolor)
        
        
        
    elif state=="green":
        print(f"|  SIGNAL {signalno} GREEN SIGNAL GO  \n")
        
        timer(signalno,state,signalcolor)
    
       
def main():
    """timerval=StringVar()
    timerval.set("Timer")
    timerentry=Entry(canvas,textvariable=timerval,font="comicsansms 18")
    timerentry.place(relx=.80, rely=.41)
    canvas.pack()
    root.update()"""      
    
    signals=["red"]*4
    
            
    hour=int(datetime.datetime.now().strftime("%H"))
    while hour<24 and hour>=7:
        for j in range(0,len(signals)):
            
            signals[j]="green"
            
            
            for i in range(0,len(signals)):
                
                if signals[i]=="red":
                    canvas.itemconfig(Signals[i][0],fill='red')
                    canvas.pack()
                    root.update()
                elif signals[i]=="green":
                    canvas.itemconfig(Signals[i][2],fill='green')
                    canvas.pack()
                    root.update()
                
                    
                t=threading.Thread(target=signal,args=(i+1,signals[i],canvas.itemcget(Signals[i][2], 'fill')),name=f"Signal{i+1}")
                t.start()
                
                
                
            t.join()
            if len(signals)-1==j:
                canvas.itemconfig(Signals[j][2],fill='grey')
                canvas.itemconfig(Signals[0][0],fill='grey')
                canvas.pack()
                root.update()
            signals[j]="red"
            
    else:
        while 1:
            for j in range(0,len(signals)):
                for i in range(0,len(signals)):
                    canvas.itemconfig(Signals[i][1],fill='yellow')
                    canvas.pack()
                    root.update()
                    
            time.sleep(3)
            for j in range(0,len(signals)):
                for i in range(0,len(signals)):
                    canvas.itemconfig(Signals[i][1],fill='grey')
                    canvas.pack()
                    root.update()        
            time.sleep(2)    
            
        
        
        
        
        
        
    
    
root=Tk()
root.title("Signal Simulation")
width,height=1580,1200
root.geometry(f"{width}x{height}")
root.minsize(width,height)
canvas=Canvas(root,width=width,height=height)
signal1=[]
r1=canvas.create_rectangle(40,30,290,750,fill="black")
s1=canvas.create_oval(70, 50, 270, 240,fill='grey',outline="black",width=20)
signal1.append(s1)
s2=canvas.create_oval(70,260,270,470,fill='grey',outline="black",width=20)
signal1.append(s2)

s3=canvas.create_oval(70,490,270,700,fill='grey',outline="black",width=20)
signal1.append(s3)
signal2=[]
r2=canvas.create_rectangle(310,30,570,750,fill="black")
s1=canvas.create_oval(340, 50, 550, 240,fill='grey',outline="black",width=20)
signal2.append(s1)
s2=canvas.create_oval(340,260,550,470,fill='grey',outline="black",width=20)
signal2.append(s2)

s3=canvas.create_oval(340,490,550,700,fill='grey',outline="black",width=20)
signal2.append(s3)
signal3=[]
r3=canvas.create_rectangle(590,30,850,750,fill="black")
s1=canvas.create_oval(620, 50, 830, 240,fill='grey',outline="black",width=20)
signal3.append(s1)
s2=canvas.create_oval(620,260,830,470,fill='grey',outline="black",width=20)
signal3.append(s2)
s3=canvas.create_oval(620,490,830,700,fill='grey',outline="black",width=20)
signal3.append(s3)
signal4=[]
r4=canvas.create_rectangle(870,30,1130,750,fill="black")
s1=canvas.create_oval(900, 50, 1110, 240,fill='grey',outline="black",width=20)
signal4.append(s1)
s2=canvas.create_oval(900,260,1110,470,fill='grey',outline="black",width=20)
signal4.append(s2)

s3=canvas.create_oval(900,490,1110,700,fill='grey',outline="black",width=20)

signal4.append(s3)
Signals=[]
Signals.append(signal1)
Signals.append(signal2)
Signals.append(signal3)
Signals.append(signal4)

canvas.pack()
start=Button(text="Start",command=main,bd=5,font="comicsansms 15")
start.place(relx=.80, rely=.31)
root.mainloop()      
            
        
        
        
        
        
    
        
    

            
    
    
    
