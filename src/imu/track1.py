from Tkinter import *
#global Kp1,Ki1,Kd1,Kp2,Ki2,Kd2

def show_values():
 master = Tk() 
 w1 = Scale(master, from_=0, to= 100, orient=HORIZONTAL)
 w1.set(0)
 w1.pack()
 w2 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
 w2.set(0)
 w2.pack()
 w3 = Scale(master, from_=0, to=100, orient=HORIZONTAL)
 w3.set(0)
 w3.pack()
 Button(master, text='Show', command=show_values).pack()
 Kp1 = w1.get()
 Ki1 = w2.get()
 Kd1 = w3.get()
 
 print(Kp1,Ki1,Kd1)





while 1 :
 
 show_values()



