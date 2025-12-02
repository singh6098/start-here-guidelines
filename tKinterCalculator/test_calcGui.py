
import tkinter as tk
from tkinter import ttk
import customtkinter
from CTkToolTip import *
import time
import matplotlib.pyplot as plt
import numpy as np

xlist = [0]
index = 0

ylist = [0]
yindex = 0

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    if value == 'ON':
       entry.insert(0, current + '1')
       xlist.append(int(current + '1'))


       ylist.append(int(current + '2'))


    elif value == 'OFF':
       entry.insert(0, current + '0')
    elif value == 'OPEN':
       entry.insert(0, current + '11')
    elif value == 'D':
       t_l = str(time.asctime())
       entry.insert(0, current + t_l[0:10])
    elif value == 'T':
       t_l = str(time.asctime())
       entry.insert(0, current + t_l[10:20])
    elif value == 'SHOWD':
       #t_l = str(time.asctime())
       #entry.insert(0, current + t_l[10:20])   
       graph_show(True)

    elif value == 'HIDED':
       #t_l = str(time.asctime())
       #entry.insert(0, current + t_l[10:20])   
       graph_show(False) 
    elif value == 'CLOSE':
        entry.insert(0, current + '00')
    else:
        entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def graph_show(bShowData):
    if bShowData == True :
        xpoints = np.array([0, 6])
        ypoints = np.array([0, 250])
        #plt.plot(xpoints, ypoints)
        print('x list is : {}'.format(xlist) )
        print('y list is : {}'.format(ylist) )
        plt.plot(xlist, ylist)
        plt.show()
    else:
        plt.plot([0], [0])
        plt.show()

def convert_temperature():
    try:
        #result = eval(entry.get())
        
        result = entry.get()
        entry.delete(0, tk.END)
        if result.find('F'):
            sget = result.replace('F','')
            rget = ((int(sget) - 32)*5)/9
        entry.insert(0, rget)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def show_slider_value(value):
    tooltip_sl.configure(message=int(value))

#root = tk.Tk()
root = customtkinter.CTk()
#root = tix .Tk()
#root.title("Simple Calculator")
root.title("GUI APP")
root.resizable(True,True)
root.configure(bg="#B9C6C9")
notebook = ttk.Notebook(root)




#frame1 =  customtkinter.CTkFrame(notebook, width= 400, height= 200)
#frame2 = customtkinter.CTkFrame(notebook, width= 400, height= 200)
#frame3 = customtkinter.CTkFrame(notebook, width= 400, height= 200)

frame1 = tk.Frame(notebook, width= 400, height= 200)
frame2 = tk.Frame(notebook, width= 400, height= 200)
frame3 = tk.Frame(notebook, width= 400, height= 200)



frame1.pack(fill="both", padx=20, pady=20)
frame2.pack(fill="both", padx=20, pady=20)
frame3.pack(fill="both", padx=20, pady=20)

notebook.pack(expand=True, fill= 'both',padx=20, pady=20)

notebook.add(frame1, text='Calculator')
notebook.add(frame2, text='Tab 2')
notebook.add(frame3, text='Tab 3')

# Entry field
#entry = tk.Entry(root, width=18, font=('Arial', 14))
#entry = tk.Entry(frame1, width=18, font=('Arial', 14))
entry = tk.Entry(frame1, width=18, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0,"Calculator Button 7"),       ('8', 1, 1,"Calculator Button 8"),              ('9', 1, 2,"Calculator Button 9"),                  ('/', 1, 3,"Calculator Button Divison"),
    ('4', 2, 0,"Calculator Button 4"),       ('5', 2, 1,"Calculator Button 5"),              ('6', 2, 2,"Calculator Button 6"),                  ('*', 2, 3,"Calculator Button Multiply"),
    ('1', 3, 0,"Calculator Button 1"),       ('2', 3, 1,"Calculator Button 2"),              ('3', 3, 2,"Calculator Button 3"),                  ('-', 3, 3,"Calculator Button Subtract"),
    ('0', 4, 0,"Calculator Button 0"),       ('C', 4, 1,"Clear Button C"),                   ('=', 4, 2,"Result Button "),                               ('+', 4, 3,"Calculator Button Add"),
    ('ON', 5, 0,"Button ON"),                ('OFF', 5, 1," Button OFF"),                     ('OPEN', 5, 2,"Button OPEN 2bits"),                              ('CLOSE', 5, 3,"Button Close 2 bits"),
    ('F', 6, 0,"Enter Temperature value in digits and click this button[Fahrnheit]"),       ('Tdeg', 6, 1,"Calculate Temperature in deg from Fahrnheit"),('D', 6, 2,"Display Date"),         ('T', 6, 3,"Display Time"),
    ('SHOWD', 7, 0,"Show Data"),                ('HIDED', 7, 1," Hide data")
]



for (text, row, column, message) in buttons:
    #button = tk.Button(root, text=text, width=6, height=2, command=lambda t=text: click_button(t))
    #button = tk.Button(frame1, text=text, width=6, height=2, command=lambda t=text: click_button(t))
    button =  customtkinter.CTkButton(frame1, text=text, width=16, height=12, command=lambda t=text: click_button(t))
    tooltip_1 = CTkToolTip(button, delay=0.5, message=message)
    #tooltip_1.bind
    button.grid(row=row, column=column)



# Special case for the clear button
#clear_button = tk.Button(root, text="C", width=6, height=2, command=clear_entry)
clear_button = customtkinter.CTkButton(frame1, text="C", width=16, height=12, command=clear_entry)
tooltip_cl = CTkToolTip(clear_button, delay=0.5, message=buttons[13][3])
clear_button.grid(row=4, column=1)


# Special case for the equals button
#equals_button = tk.Button(root, text="=", width=6, height=2, command=calculate_result)
equals_button = customtkinter.CTkButton(frame1, text="=", width=16, height=12, command=calculate_result)
tooltip_eq = CTkToolTip(equals_button, delay=0.5, message=buttons[14][3])
equals_button.grid(row=4, column=2)

# Special case for the Tdeg button
#Tdeg_button = tk.Button(root, text="Tdeg", width=6, height=2, command=convert_temperature)
Tdeg_button = customtkinter.CTkButton(frame1, text="Tdeg", width=16, height=12, command=convert_temperature)
tooltip_tdeg = CTkToolTip(Tdeg_button, delay=0.5, message=buttons[21][3])
Tdeg_button.grid(row=6, column=1)


slider = customtkinter.CTkSlider(frame2, from_=0, to=100,  fg_color= "white",progress_color= "green", command=show_slider_value)
slider.pack(fill="both", padx=20, pady=20)

tooltip_sl = CTkToolTip(slider, message="10")

root.mainloop()