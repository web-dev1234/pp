from tkinter import*

window=Tk()

def km_to_miles():
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

def clear_output():
    km=float(e1_value.get())*0
    t1.insert(END,km)    
    

b1=Button(window,text="execute",command=km_to_miles)
b1.grid(row=0,column=0)

b2=Button(window,text="close",command=window.destroy)
b2.grid(row=3,column=5)

b3=Button(window,text="clear",command=clear_output)
b3.grid(row=1,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)



window.mainloop()