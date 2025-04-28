#Simple Password Generator
from math import floor
import random
from tkinter import *
from tkinter import BooleanVar

import ttkbootstrap as tb

#Setup
root = tb.Window()
style = tb.Style("litera")
root.geometry("400x500")
# root.maxsize(height=500, width=400)
root.grid_columnconfigure(0, weight=1)  # Allow column to expand


#Initialization
len_var = tb.IntVar(root, '')
number_tog=BooleanVar(root, False)
char_tog=BooleanVar(root, False)
sp_char_tog=BooleanVar(root,False)
set_int=[1,2,3,4,5,6,7,8,9,0]
set_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
set_symbol=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':',',','.','<','>','?','/','~']
options = []
i=5
while(i<=20):
    options.append(i)
    i+=1

def generate():
    len_var_value=len_var.get()
    number_tog_value=number_tog.get()
    char_tog_value=char_tog.get()
    sp_char_tog_value=sp_char_tog.get()
    print(number_tog_value)
    print(char_tog_value)
    print(sp_char_tog_value)
    print(len_var_value)
    if(number_tog_value==TRUE and char_tog_value==FALSE and sp_char_tog_value==FALSE):
        all_char=[set_int]
        result=[]
        j=0
        while(j<len_var_value):
            result.append(random.choice(set_int))
            j+=1
    elif(number_tog_value==TRUE and char_tog_value==FALSE and sp_char_tog_value==FALSE)
    result_joined = "".join(str(item) for item in result)
    label_result = tb.Label(root, text=result_joined, font=("Helvetica", 10, "bold"))
    label_result.grid(row=6, column=0, pady=10)

#Heading
heading = tb.Label(root, text="Simple Password Generator", font=("Helvetica", 17, "bold"), foreground="navy")
heading.grid(row=0, column=0, pady=70)

#Lenght of Password
entry_len = tb.Combobox(values=options, textvariable=len_var)
entry_len.set('Lenght')
entry_len.grid(row=1, column=0, padx=20, pady=10, sticky='w')


#Int Checkbox
btn_int=tb.Checkbutton(root, text="Include Numbers", variable=number_tog, bootstyle='round-toggle')
btn_int.grid(row=2, column=0, padx=20, pady=10, sticky='w')

#Character Checkbox
btn_char=tb.Checkbutton(root, text="Include Characters", variable=char_tog, bootstyle='round-toggle')
btn_char.grid(row=3, column=0, padx=20, pady=10, sticky='w')

#Special Character Checkbox
btn_sp_char=tb.Checkbutton(root, text="Include Special Characters", variable=sp_char_tog, bootstyle='round-toggle')
btn_sp_char.grid(row=4, column=0, padx=20, pady=10, sticky='w')

#Submit
btn_sub=tb.Button(root, text='Enter', command=generate)
btn_sub.grid(row=5, column=0,ipadx=10,ipady=5, padx=100, pady=20)


root.mainloop()