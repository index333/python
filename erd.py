from tkinter import *
from tkinter import ttk
import subprocess
def show():         
    [rd,t,dp] = [i.get() for i in vList]
    label.config(text=(rd/2-(dp-t))*2)
def exit(): 
    s=label.cget('text')
    with open("erd.txt",'w') as f:
        f.write(str(s))
    subprocess.run(['python3','spcal.py'])
    w.destroy()
def callback(a,b,c): show()
w = Tk()
w.title('erd')
w.protocol("WM_DELETE_WINDOW",exit)
textList =["rim diameter(mm)", ",t(mm)", "depth(mm)","erd(mm)"]
frameList = [ttk.LabelFrame(w,text=i) for i in textList]
for i in frameList: i.pack()
vList=[DoubleVar() for i in range(3)]
for i in range(3): vList[i].set([600,1,15][i])
sp1=ttk.Spinbox(frameList[0],format='%3.1f',textvariable=vList[0],from_=500,to=700,increment=0.5,command=show)
sp2=ttk.Spinbox(frameList[1],format='%3.1f',state='readonly',textvariable=vList[1],from_=0,to=2,increment=0.1,command=show)
sp3=ttk.Spinbox(frameList[2],format='%3.1f',state='readonly',textvariable=vList[2],from_=0,to=30,increment=0.1,command=show)
for i in [sp1,sp2,sp3]: i.pack()
label=ttk.Label(frameList[3])
label.pack()
vList[0].trace_add(('write'),callback)
show()
w.mainloop()
