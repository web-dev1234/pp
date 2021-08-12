from tkinter import *
root=Tk()
def send():
    send="mein:"+a.get()
    text.insert(END,"\n"+send)
    if (a.get()=='Namaste'):
        text.insert(END,"\n" + "yantra:Namaste")
    elif(a.get()=='Aap kaise ho?'):
        text.insert(END,"\n" + "yantra:Main theek hoon. Aap kaise ho?")
    elif(a.get()=='Main bhi theek hoon'):
        text.insert(END,"\n" + "yantra:Sun kar accha lga")
    else:
        text.insert(END,"\n" + "yantra:Mujhe samaj nhi aya")
text=Text(root,bg='white')
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(text='Bheje',bg='Orange',width=20,command=send).grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('simple chatbot')
root.mainloop()
        