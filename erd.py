from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import subprocess ,sys
def show():         
    v1 = vList[0].get()
    v2 = vList[1].get()
    v3 = vList[2].get()
    label.config(text= (v1-(v3-v2)*2))
def exit(): 
    s=label.cget('text')
    with open("erd.txt",'w') as f:
        f.write(str(s))
    subprocess.run(['python','spcal.py'])
    root.destroy()
def callback(a,b,c): show()
root = Tk()
root.title('erd')
root.protocol("WM_DELETE_WINDOW",exit)
textList =["rim diameter(mm)", ",t(mm)", "depth(mm)","erd(mm)"]
frameList = [ttk.LabelFrame(root,text=i) for i in textList]
for i in frameList: i.pack()
vList=[DoubleVar() for i in range(3)]
for i in range(3): vList[i].set([600,1,15][i])
sp1=ttk.Spinbox(frameList[0],format='%3.1f',textvariable=vList[0],from_=500,to=700,increment=0.5,command=show)
sp1.pack()
sp2=ttk.Spinbox(frameList[1],format='%3.1f',state='readonly',textvariable=vList[1],from_=0,to=2,increment=0.1,command=show)
sp2.pack()
sp3=ttk.Spinbox(frameList[2],format='%3.1f',state='readonly',textvariable=vList[2],from_=0,to=30,increment=0.1,command=show)
sp3.pack()
label=ttk.Label(frameList[3])
label.pack()
vList[0].trace_add(('write'),callback)
show()
root.mainloop()
