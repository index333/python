from cmath import *
from tkinter import *
from tkinter import ttk
cPitch = 12.7
yen = 2*pi
def guess (t,d): 
    r=d/2
    c0=r+0j
    c1=rect(r,(yen/t))
    return(abs(c0-c1))
def pcr(h,l,t):
    if abs(h-l)<0.1: return (h/2)
    else: 
        i= guess(t,mid(h,l)) 
        if i < cPitch: return (pcr(h,mid(h,l),t))
        else: return (pcr(mid(h,l),l,t))
def mid(a,b): return ((a+b)/2)
def clen(f,r,c,th): return((f/4+f*th/yen+c+r/4-r*th/yen)*2)
def show():         
    vs = [i.get() for i in vList]
    f=pcr(600,10,vs[0])
    r=pcr(600,10,vs[1])
    ac=(vs[2])
    bc=f-r
    ab=sqrt(ac*ac-bc*bc)
    th=asin(bc/ac)
    d=abs(clen(vs[0],vs[1],(ab/cPitch),th))
    label.config(text=str(round(d,1)))
def callback(a,b,c): show()
w = Tk()
w.title('シングルバイクのチェーン長')
w.protocol("WM_DELETE_WINDOW",exit)
fList = [ttk.LabelFrame(w,text=i) for i in ["front gear(T)","rear sprocket(T)","BB2Hub(mm)","チェーン(links)"]]
for i in fList: i.pack()
vList = [DoubleVar() for i in range(3)]
[i.set(j) for (i,j) in zip(vList,[48,16,405])]
sp1=ttk.Spinbox(fList[0],format='%2.0f',state='readonly',textvariable=vList[0],from_=20,to=60,increment=1,command=show)
sp2=ttk.Spinbox(fList[1],format='%2.0f',state='readonly',textvariable=vList[1],from_=6,to=40,increment=1,command=show)
sp3=ttk.Spinbox(fList[2],format='%3.0f',textvariable=vList[2],from_=100,to=700,increment=1,command=show)
for i in [sp1,sp2,sp3]: i.pack()
label=ttk.Label(fList[3])
label.pack()
vList[2].trace_add(('write'),callback)
show()
w.mainloop()
