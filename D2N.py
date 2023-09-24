# plan is to make a gui which asks for the base value and converts the decimal number to appropriate numeric system
import tkinter
from tkinter import *
from tkinter import messagebox

   

window = tkinter.Tk()
window.title("D2N Converter!")
frame = tkinter.Frame(window)
frame.pack()

#title
title= tkinter.LabelFrame(frame,borderwidth=0,highlightthickness=0)
title.grid(row=0,column=0)
head= tkinter.Label(title,text="DECIMAL NUMBER CONVERTER", font=("Arial",15,"bold"))
head.grid(row=0,column=0,ipadx=100)
window.minsize(width=500, height=400)
window.maxsize(width=500, height=400)

#Telling the user about the converter
frame1 = tkinter.LabelFrame(frame,borderwidth=0,pady=5)
frame1.grid(row=1,column=0)
label1=tkinter.Label(frame1,text=("This converter will convert Your Decimal(10) Value to:\nBinary(2),\nOctal(8),\nHexa-Decimal(16)."), font=("Arial", 12,"italic"))
label1.grid(row=0,column=0)

#taking input from the user
frame2 = tkinter.LabelFrame(frame,text="",borderwidth=0,highlightthickness=0)
frame2.grid(row=2,column=0)
label3 = tkinter.Label(frame2,text=("Enter the decimal number: "), font=("Arial",10,"italic"))
label3.grid(row=0,column=0)
entry_num=tkinter.Entry(frame2,width=28)
entry_num.grid(row=0, column=1)

#taking base from the user
label4 = tkinter.Label(frame2, text=("Select the base: "),font=("Arial",10,"italic"))
label4.grid(row=1,column=0)
menu = tkinter.StringVar()
menu.set("Select from the options")
base =tkinter.OptionMenu(frame2,menu,"Binary(2)","Octal(8)","Hexa-Decimal(16)")
base.grid(row=1, column=1)
#function for the button

def check_num():
        num = (entry_num.get())
        bas = menu.get()
        if bas == "Binary(2)":
                bin1 = bin(int(num))
                label5 = tkinter.Label(window, text =(f"The Binary conversion is {bin1}"), font = ("Times New Roman", 12, "italic")) 
                label5.pack()         
        elif bas == "Octal(8)":
                oct1 = oct(int(num))
                label6 = tkinter.Label(window, text =(f"The Octal conversion is {oct1}"),font = ("Times New Roman", 12, "italic"))
                label6.pack()  
        else:
                hex1 = hex(int(num))
                label7 = tkinter.Label(window, text=(f"The Hexa-Decimal conversion is {hex1}"),font = ("Times New Roman", 12, "italic"))
                label7.pack()   
                      

#converting button
frame3 = tkinter.LabelFrame(frame, borderwidth=0)
frame3.grid(row=5,column=0)
btn = tkinter.Button(frame3,text="CONVERT!", height=2, width=10,font=("Arial",12,"bold"), command =check_num)
btn.grid(row=2,column=0, pady=5)



window.mainloop()
