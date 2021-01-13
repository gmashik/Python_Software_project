from tkinter import *

window=Tk()
window.title("Mile to KM Converter")
#window.config(width=600,height=300)
#window.config(padx=50,pady=20)
ml=Entry()
ml.grid(column=1,row=0)
lab1=Label(text="Miles")
lab1.grid(column=2,row=0)
lab2=Label(text="is equal to")
lab2.grid(column=0,row=1)
res=Label(text="0")
res.grid(column=1,row=1)
lab4=Label(text="Kilometers")
lab4.grid(column=2,row=1)
def calc():
    m=float(ml.get())
    r=1.609*m
    res.config(text=f"{r}")
b1=Button(text="Calculate",command=calc)
b1.grid(column=1,row=2)



window.mainloop()
