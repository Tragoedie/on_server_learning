from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import Checkbutton



nickname = ''
number_class = 0
class_of_character = ''
specialization = ''
strenght = 0
agility = 0
intelligence = 0
text_chronicle = ''
characteristics_text = ''


def save_nickname():
    global nickname
    nickname = "Your character name:  {}".format(nike_name_txt.get())
    nike_name_lbl_result.configure(text=nickname, font=("Arial Bold", 10))
def change_class():
    global number_class
    global starting_characteristics_strength
    global starting_characteristics_agility
    global starting_characteristics_intelligence
    global class_of_character
    number_class = selected_class.get()
    if number_class == 1:
        class_of_character = 'Your class is Warrior'
        class_lbl_result.configure(text=class_of_character, font=("Arial Bold", 10))
        specialization_combo['values'] = ('Tank', 'Warrior')
        specialization_combo.current(0)
        var_str = IntVar()
        var_str.set(7)
        starting_characteristics_strength.config(from_=7, to=10, textvariable=var_str)
        var_agil = IntVar()
        var_agil.set(5)
        starting_characteristics_agility.config(from_=5, to=8, textvariable=var_agil)
        var_int = IntVar()
        var_int.set(3)
        starting_characteristics_intelligence.config(from_=3, to=6, textvariable=var_int)
    elif number_class == 2:
        class_of_character = 'Your class is Mage'
        class_lbl_result.configure(text=class_of_character, font=("Arial Bold", 10))
        specialization_combo['values'] = ('Mage', 'Priest')
        specialization_combo.current(0)
        var_str = IntVar()
        var_str.set(3)
        starting_characteristics_strength.config(from_=3, to=6, textvariable=var_str)
        var_agil = IntVar()
        var_agil.set(5)
        starting_characteristics_agility.config(from_=5, to=8, textvariable=var_agil)
        var_int = IntVar()
        var_int.set(7)
        starting_characteristics_intelligence.config(from_=7, to=10, textvariable=var_int)
    else:
        class_of_character ='Your class is Rogue'
        class_lbl_result.configure(text = class_of_character, font=("Arial Bold", 10))
        specialization_combo['values'] = ('Rogue', 'Hunter')
        specialization_combo.current(0)
        var_str = IntVar()
        var_str.set(5)
        starting_characteristics_strength.config(from_=5, to=8, textvariable=var_str)
        var_agil = IntVar()
        var_agil.set(7)
        starting_characteristics_agility.config(from_=7, to=10, textvariable=var_agil)
        var_int = IntVar()
        var_int.set(3)
        starting_characteristics_intelligence.config(from_=3, to=6, textvariable=var_int)

def change_specialization():
    global specialization
    specialization = "Your specialization:  {}".format(specialization_value.get())
    specialization_lbl_result.configure(text=specialization, font=("Arial Bold", 10))

def change_characteristics():
    global strenght
    global agility
    global intelligence
    global characteristics_text
    strenght = int(starting_characteristics_strength.get())
    agility = int(starting_characteristics_agility.get())
    intelligence = int(starting_characteristics_intelligence.get())
    sum_of_characteristics = strenght + agility + intelligence
    if sum_of_characteristics < 18:
        messagebox.showinfo('Error', 'Add more characteristics')
    elif sum_of_characteristics > 18:
        messagebox.showinfo('Error', 'Reduce characteristics')
    else:
        characteristics_text = 'Your characteristics:' + '\n Strength :' + str(strenght)\
                               + '\nAgility: ' + str(agility) + '\nIntelligence: ' + str(intelligence)
        characteristics_lbl_result.configure(text=characteristics_text, font=("Arial Bold", 10))

def saved_сhronicle():
    global text_chronicle
    text_chronicle = сhronicle_txt.get(1.0, "end")
    print(text_chronicle)

def cancel_create():
    exactly_cancel = messagebox.askyesno('!!!', 'Are you sure?')
    if exactly_cancel == True:
        main_window.destroy()
    else:
        return

def create_character():
    global nickname
    global number_class
    global specialization
    global strenght
    global agility
    global intelligence
    global text_chronicle
    global chk_license
    global  class_of_character
    if nickname == '':
        messagebox.showinfo('Error', 'Enter character name')
    elif number_class == 0:
        messagebox.showinfo('Error', 'Enter character class')
    elif specialization == '':
        messagebox.showinfo('Error', 'Enter character specialization')
    elif strenght == 0 or agility == 0 or intelligence == 0:
        messagebox.showinfo('Error', 'Check character characteristics')
    elif chk_license.get() is False:
        messagebox.showinfo('Error', 'Please agree to the license agreement')
    else:
        check_exactly_cancel = messagebox.askyesno('!!!', 'Are you sure?')
        if check_exactly_cancel is False:
            return
        else:
            save_text = nickname + class_of_character + specialization +  characteristics_text + text_chronicle
            with open("Your character.txt", "a") as file_txt:
                file_txt.write(save_text)



main_window = Tk()
main_window.title("Creation your character")
main_window.geometry('800x900')
hello_lbl = Label(main_window, text="Hello", font=("Arial Bold", 15))
hello_lbl.grid(column=1, row=0)
nike_name_lbl = Label(main_window, text="Enter character name:", font=("Arial Bold", 10))  # Nickname
nike_name_lbl.grid(column=0, row=1)
nike_name_lbl_result = Label(main_window, text="Nickname will be here", font=("Arial Bold", 8))
nike_name_lbl_result.grid(column=2, row=2)
nike_name_txt = Entry(main_window, width=50)
nike_name_txt.focus()
nike_name_txt.grid(column=0, row=2)
nike_name_btn = Button(main_window, text="Oк", width=5, height=1, command=save_nickname)
nike_name_btn.grid(column=1, row=2)
class_lbl = Label(main_window, text="Choose your class:", font=("Arial Bold", 10))  # Class
class_lbl.grid(column=0, row=3)
selected_class = IntVar()
class_lbl_result = Label(main_window, text="Class will be here", font=("Arial Bold", 8))
class_lbl_result.grid(column=4, row=4)
first_class = Radiobutton(main_window, text='Warrior', value=1, variable=selected_class)
second_class = Radiobutton(main_window, text='Mage', value=2, variable=selected_class)
third_class = Radiobutton(main_window, text='Rogue', value=3, variable=selected_class)
class_btn = Button(main_window, text="Ok", command=change_class)
first_class.grid(column=0, row=4)
second_class.grid(column=1, row=4)
third_class.grid(column=2, row=4)
class_btn.grid(column=3, row=4)
specialization_lbl = Label(main_window, text="Choose your specialization:", font=("Arial Bold", 10))  # Specialization
specialization_lbl.grid(column=0, row=5)
specialization_value = StringVar()
specialization_combo = ttk.Combobox(main_window, textvariable=specialization_value, state='readonly')
if number_class == 0:
    specialization_combo['value'] = ("At first choose your class")
specialization_combo.grid(column=0, row=6)
specialization_lbl_result = Label(main_window, text="Specialization will be here", font=("Arial Bold", 8))
specialization_lbl_result.grid(column=2, row=6)
specialization_btn = Button(main_window, text="Ok", command=change_specialization)
specialization_btn.grid(column=1, row=6)
starting_characteristics_lbl = Label(main_window, text="Change your starting characteristics(add 3):",
                                     font=("Arial Bold", 10))  # Starting characteristics
starting_characteristics_lbl.grid(column=0, row=7)
var_str = IntVar()
var_str.set(0)
starting_characteristics_strength = Spinbox(main_window, from_=0, to=0, width=5, textvariable=var_str)
str_lbl = Label(main_window, text="Strength", font=("Arial Bold", 12))
var_agil = IntVar()
var_agil.set(0)
starting_characteristics_agility = Spinbox(main_window, from_=0, to=0, width=5, textvariable=var_agil)
agil_lbl = Label(main_window, text="Agility", font=("Arial Bold", 12))
var_int = IntVar()
var_int.set(0)
starting_characteristics_intelligence = Spinbox(main_window, from_=0, to=0, width=5, textvariable=var_int)
int_lbl = Label(main_window, text="Intelligence", font=("Arial Bold", 12))
str_lbl.grid(column=0, row=8)
starting_characteristics_strength.grid(column=1, row=8)
agil_lbl.grid(column=2, row=8)
starting_characteristics_agility.grid(column=3, row=8)
int_lbl.grid(column=4, row=8)
starting_characteristics_intelligence.grid(column=5, row=8)
characteristics_btn = Button(main_window, text="Ok", command=change_characteristics)
characteristics_btn.grid(column=6, row=8)
characteristics_lbl_result = Label(main_window, text="Characteristics will be here", font=("Arial Bold", 8))
characteristics_lbl_result.grid(column=0, row=9)
сhronicle_txt = scrolledtext.ScrolledText(main_window, width=40, height=10)  # Сhronicle of your character's life
сhronicle_txt.grid(column=0, row=10)
сhronicle_btn = Button(main_window, text="Ok", command=saved_сhronicle)
сhronicle_btn.grid(column=1, row=10)

chk_license = BooleanVar()
license_chk = Checkbutton(main_window, text='I agree to the license agreement', variable=chk_license)
license_chk.grid(column=0, row=11)

create_btn = Button(main_window, text="Create", command=create_character)
create_btn.grid(column=0, row=12)
cancel_btn = Button(main_window, text="Cancel", command=cancel_create)
cancel_btn.grid(column=1, row=12)




main_window.mainloop()
