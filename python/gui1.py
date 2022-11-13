#Import tkinter modules
from tkinter import *

#creating a window from tkinter and configuration 
windows1 = Tk()
windows1.title("Tkinter Radiobutton Selection")
windows1.geometry('400x400')
windows1.configure(bg="lightgray")

#creating a reset function 
def reset():
    return my_var1.set(7)

#declare a variables and program 
my_var1 = IntVar()
frame1 = LabelFrame(windows1, text="Pick your favourite fruit", padx=70, bg='black')
frame1.pack()
Radiobutton(frame1, text='Apple', variable=my_var1, value=1).pack(anchor=W)
Radiobutton(frame1, text='watermelon', variable=my_var1, value=2).pack(anchor=W)
Radiobutton(frame1, text='Coconut', variable=my_var1, value=3).pack(anchor=W)
Radiobutton(frame1, text='Mango', variable=my_var1, value=4).pack(anchor=W)
Radiobutton(frame1, text='Banana', variable=my_var1, value=5).pack(anchor=W)
Radiobutton(frame1, text='Grape', variable=my_var1, value=6).pack(anchor=W)
none_Rb = Radiobutton(frame1, text='None', variable=my_var1, value=7).pack(anchor=W)
Button(windows1, text='Reset', command=reset, padx=15, pady=15).pack(pady=8)

windows1,mainloop()