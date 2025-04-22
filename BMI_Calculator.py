import tkinter
from contextlib import nullcontext
from math import floor
from tkinter import *
from tkinter import StringVar

root=Tk()
root.geometry("400x500")
root.maxsize(height=500, width=400)

#initialization
var_weight=IntVar(root, "")
var_age=IntVar(root, "")
var_height=IntVar(root, "")
var_gender=IntVar(root, 0)

#Function
def BMI_cal():
    #initialization
    age=var_age.get()
    height=var_height.get()/100
    weight=var_weight.get()
    gender= var_gender.get()
    print(age, height, weight, gender)
    #logic
    var_result=floor(weight/(height*height))

    #printing result
    label_result = Label(root, text=var_result, font=('calibre',15,'normal'))
    label_result.grid(row=7, column=0, columnspan=2, pady=10)

#Heading
label_heading = Label(root, text="BMI Calculator", font=('calibre',30,'bold'))

#Age Field
label_age = Label(root, text="Age : ", font=('calibre',15,'normal'), justify="left", anchor="w")
entry_age= Entry(root,textvariable=var_age, font=('calibre',15,'normal'))

#Height Field
label_height = Label(root, text="Height (Cm) : ", font=('calibre',15,'normal'), justify="left", anchor="w")
entry_height= Entry(root,textvariable =var_height, font=('calibre',15,'normal'))

#Weigth Field
label_weight = Label(root, text="Weight (Kg) : ", font=('calibre',15,'normal'), justify="left", anchor="w")
entry_weight= Entry(root,textvariable=var_weight, font=('calibre',15,'normal'))

#Gender
label_gender = Label(root, text="Gender : ", font=('calibre',15,'normal'), justify="left", anchor="w")
btn_gender_male= Radiobutton(root, variable=var_gender, text="Male", value=0, font=('calibre',15,'normal'), justify="left", anchor="w")
btn_gender_female= Radiobutton(root, variable=var_gender, text="Female", value=1, font=('calibre',15,'normal'), justify="left", anchor="w")

#Submit Button
sub_btn=Button(root, text="Submit", command=BMI_cal, font=('calibre',15,'normal'))

#Grid
label_heading.grid(row=0, column=0, pady=15, columnspan=3)

label_age.grid(row=1, column=0, pady=3, sticky="w", padx=10)
entry_age.grid(row=1, column=1, pady=3, padx=5)

label_height.grid(row=2, column=0, pady=3, sticky="w", padx=10)
entry_height.grid(row=2, column=1, pady=3)

label_weight.grid(row=3, column=0, pady=3, sticky="w", padx=10)
entry_weight.grid(row=3, column=1, pady=3)

label_gender.grid(row=4, column=0, pady=0, sticky="w", padx=10)
btn_gender_male.grid(row=4, column=1, pady=0, sticky="w")
btn_gender_female.grid(row=5, column=1, pady=0, sticky="w")

sub_btn.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()