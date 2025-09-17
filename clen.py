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
def bm(h,l,t):
    if abs(h-l)<0.1: return (h/2)
    else: 
        i= guess(t,mid(h,l)) 
        if i < cPitch: 
            return (bm(h,mid(h,l),t))
        else: 
            return (bm(mid(h,l),l,t))
def mid(a,b): return ((a+b)/2)
def clen(f,r,c,th):
    return((f/4+f*th/yen+c+r/4-r*th/yen)*2)
def show():         
    v1 = vList[0].get()
    v2 = vList[1].get()
    v3 = vList[2].get()
    f=bm(600,10,v1)
    r=bm(600,10,v2)
    ac=(v3)
    bc=f-r
    ab=sqrt(ac*ac-bc*bc)
    th=asin(bc/ac)
    txt=abs(clen(v1,v2,(ab/cPitch),th))
    label.config(text=str(round(txt,1)))
def callback(arg1, arg2, arg3): show()
root = Tk()
root.title('シングルバイクのチェーン長')
root.protocol("WM_DELETE_WINDOW",exit)
frame1 = ttk.LabelFrame(root,text="front gear(T)")
frame2 = ttk.LabelFrame(root,text="rear sprocket(T)")
frame3 = ttk.LabelFrame(root,text="BB2Hub(mm)")
frame4 = ttk.LabelFrame(root,text="チェーン(links")
for i in [frame1, frame2, frame3, frame4]: i.pack()
vList = [DoubleVar() for i in range(3)]
[i.set(j) for (i,j) in zip(vList,[48,16,405])]
sp1=ttk.Spinbox(frame1,format='%2.0f',state='readonly',textvariable=vList[0],from_=20,to=60,increment=1,command=show)
sp2=ttk.Spinbox(frame2,format='%2.0f',state='readonly',textvariable=vList[1],from_=6,to=40,increment=1,command=show)
sp3=ttk.Spinbox(frame3,format='%3.0f',textvariable=vList[2],from_=100,to=700,increment=1,command=show)
for i in [sp1,sp2,sp3]: i.pack()
label=ttk.Label(frame4)
label.pack()
vList[2].trace_add(('write'),callback)
show()
root.mainloop()
