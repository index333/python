from cmath import *
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
def dist(a,b): 
    return abs(a-b)
hosei = 2.4 / 2 
yen = pi * 2
def fh (pcd, h, k): 
    pcr= (pcd / 2)
    return (rect (pcr, (yen / (h / 2) * (k - 1) / 2)) )
def fr (d, h):
    a =( d / 2)
    return (rect (a, (yen / h * (-1)))) 
def hypo (l, z):
    a = 0
    b = l + (z * 1j)
    return (dist (a, b))
def len (erd, h ,pcd, flc,k): 
    a = fh (pcd, h, k)
    b = fr (erd, h)
    c = dist (a,b)
    d = hypo(c, flc)  
    return (d - hosei)
def len0 (erd, h,k,endW,pcd, e2c):
    flc = endW/2-e2c
    return len(erd, h,pcd, flc, k)
with open("erd.txt") as f:
    s=f.read()
    print(s)
def show():
    v1=float(val1.get())
    v2=float(val2.get())
    v3=float(val3.get())
    v4=float(val4.get())
    v41=float(val41.get())
    v5=float(val5.get())
    label.config(text=str(round(len0(v1,v2,v5,v4,v41,v3),1)))
root = Tk()
root.title('spoke length')
frame1 = ttk.LabelFrame(root,text="rim erd(mm)")
frame2 = ttk.LabelFrame(root,text="穴数")
frame3 = ttk.LabelFrame(root,text="end-flange(mm)")
frame4 = ttk.LabelFrame(root,text="end幅(mm)")
frame41 = ttk.LabelFrame(root,text="pcd(mm)")
frame5 = ttk.LabelFrame(root,text="組数")
frame6 = ttk.LabelFrame(root,text="spoke length(mm)")
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()
frame41.pack()
frame5.pack()
frame6.pack()
val1= StringVar()
val1.set(s)
sp1=ttk.Spinbox(frame1,format='%3.1f',state='readonly',textvariable=val1,from_=500,to=700,increment=0.1,command=show)
sp1.pack()
val2= StringVar()
val2.set("32")
sp2=ttk.Spinbox(frame2,format='%3.1f',state='readonly',textvariable=val2,from_=20,to=40,increment=4,command=show)
sp2.pack()
val3= StringVar()
val3.set("16")
sp3=ttk.Spinbox(frame3,format='%3.1f',state='readonly',textvariable=val3,from_=10,to=100,increment=0.1,command=show)
sp3.pack()
val4= StringVar()
val4.set("100")
sp4=ttk.Spinbox(frame4,format='%3.1f',state='readonly',textvariable=val4,from_=100,to=135,increment=1,command=show)
sp4.pack()
val41= StringVar()
val41.set("38")
sp41=ttk.Spinbox(frame41,format='%3.1f',state='readonly',textvariable=val41,from_=10,to=70,increment=1,command=show)
sp41.pack()
val5= StringVar()
val5.set("6")
sp5=ttk.Spinbox(frame5,format='%3.1f',state='readonly',textvariable=val5,from_=0,to=8,increment=2,command=show)
sp5.pack()
label=ttk.Label(frame6)
label.pack()
show()
root.mainloop()
