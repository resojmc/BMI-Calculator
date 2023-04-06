#Imports tkinter library as tk
import tkinter as tk

#defines root as main keyword, Window size, and title
root = tk.Tk()
root.geometry("300x150")
root.title("Jmc's BMI Calculator")

#Main menu
main_unit = ["Imperial", "Metric"]
menu_options_1 = tk.StringVar()
menu_options_1.set("System of Measurement")

#Height/Length menu
units_h = {"Imperial": ["Inches", "Feet"],
"Metric": ["Meters", "Centimeters"]}
h_menu_options = tk.StringVar()
h_menu_options.set("Height Unit")

#Weight menu
units_w = {"Imperial": ["Pounds", "Stones"],
"Metric": ["Kilograms"]}
w_menu_options = tk.StringVar()
w_menu_options.set("Weight Unit")

#Height and Weight entry boxes
height_entry = tk.Entry(root, )
height_entry.place(relx=0.5, rely=0.35, anchor="w")
weight_entry = tk.Entry(root, )
weight_entry.place(relx=0.5, rely=0.65, anchor="w")

#Functionality and placement for main menu
main_menu = tk.OptionMenu(root, menu_options_1, *main_unit)
main_menu.place(relx=0.5, rely=0.1, anchor="center")

#Functionality and placement for height menu
units_h_menu = tk.OptionMenu(root, h_menu_options, *units_h)
units_h_menu.place(relx=0.5, rely=0.35, anchor="e")

#Functionality and placement for weight menu
units_w_menu = tk.OptionMenu(root, w_menu_options, *units_w)
units_w_menu.place(relx=0.5, rely=0.65, anchor="e")

def update_menu1(*a):
    #A function that updates the height menu following a selection on the main menu
    menu_options_new = units_h[menu_options_1.get()]
    h_menu_options.set(menu_options_new[0])
    units_h_menu['menu'].delete(0, 'end')
    for option in menu_options_new:
        units_h_menu['menu'].add_command(label=option, command=tk._setit(h_menu_options, option))
    update_menu2()

def update_menu2(*a):
    #A function that updates the weight menu following a selection on the height menu
    h2_options_new = units_w[menu_options_1.get()]
    w_menu_options.set(h2_options_new[0])
    units_w_menu['menu'].delete(0, 'end')
    w_menu_options.configure(values=h2_options_new)
    for option in h2_options_new:
        units_w_menu['menu'].add_command(label=option, command=tk._setit(w_menu_options, option))

def find_bmi(h, w):
    #A function that calculates BMI from a given input
    feet, inches, pounds, stones, meters, cm, kg, result = 0, 0, 0, 0, 0, 0, 0, 0
    if menu_options_1.get() == "Imperial":
        if h_menu_options.get() == "Inches":
            inches = float(h)
        elif h_menu_options.get() == "Feet":
            feet = float(h)
            inches = (feet * 12)
        if w_menu_options.get() == "Pounds":
            pounds = float(w)
            kg = pounds / 2.20462
        elif w_menu_options.get() == "Stones":
            stones = float(w)
            pounds = stones * 14
            kg = pounds / 2.20462
        result = kg / ((inches / 39.37) ** 2)
    elif menu_options_1.get() == "Metric":
        if h_menu_options.get() == "Meters":
            meters = float(h)
        elif h_menu_options.get() == "Centimeters":
            cm = float(h)
            meters = cm / 100
        if w_menu_options.get() == "Kilograms":
            kg = float(w)        
        result = kg / (meters ** 2)
    return round(result, 2)

def update_bmi():
    #Updates the result label
    weight = weight_entry.get()
    height = height_entry.get()
    result = find_bmi(height, weight)
    result_label.config(text=f"Your BMI: {result}")

#Updates Menus whenever they're changed
menu_options_1.trace('w', update_menu1)
h_menu_options.trace('w', update_menu2)

#button set to execute a given function
button = tk.Button(root, text="Go", command=update_bmi)
button.place(relx=0.5, rely=0.9, anchor="e")

#Label that displays results
result_label = tk.Label(root, text="Result: ")
result_label.place(relx=0.5, rely=0.9, anchor="w")

#Executes main loop
root.mainloop()