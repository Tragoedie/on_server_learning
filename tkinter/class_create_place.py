from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import Checkbutton
from PIL import Image, ImageTk


class create_character:

    def __init__(self, name):
        self.nickname = ''
        self.number_class = 0
        self.class_of_character = ''
        self.specialization = ''
        self.strenght = 0
        self.agility = 0
        self.intelligence = 0
        self.text_chronicle = ''
        self.characteristics_text = ''
        self.name = name

    def save_nickname(self):
        self.nickname = "{}".format(self.nike_name_txt.get())
        self.nike_name_lbl_result.configure(text=self.nickname, font=("Arial Bold", 12))
        self.nike_name_lbl_result.place(x=160, y=50)

    def change_class(self):
        self.number_class = self.selected_class.get()
        if self.number_class == 1:
            self.class_of_character = 'Your class is Warrior'
            self.class_lbl_result.configure(text=self.class_of_character, font=("Arial Bold", 12))
            self.specialization_combo['values'] = ('Tank', 'Warrior')
            self.specialization_combo.current(0)
            self.var_str = IntVar()
            self.var_str.set(7)
            self.starting_characteristics_strength.config(from_=7, to=10, textvariable=self.var_str)
            self.var_agil = IntVar()
            self.var_agil.set(5)
            self.starting_characteristics_agility.config(from_=5, to=8, textvariable=self.var_agil)
            self.var_int = IntVar()
            self.var_int.set(3)
            self.starting_characteristics_intelligence.config(from_=3, to=6, textvariable=self.var_int)
        elif self.number_class == 2:
            self.class_of_character = 'Your class is Mage'
            self.class_lbl_result.configure(text=self.class_of_character, font=("Arial Bold", 12))
            self.specialization_combo['values'] = ('Mage', 'Priest')
            self.specialization_combo.current(0)
            self.var_str = IntVar()
            self.var_str.set(3)
            self.starting_characteristics_strength.config(from_=3, to=6, textvariable=self.var_str)
            self.var_agil = IntVar()
            self.var_agil.set(5)
            self.starting_characteristics_agility.config(from_=5, to=8, textvariable=self.var_agil)
            self.var_int = IntVar()
            self.var_int.set(7)
            self.starting_characteristics_intelligence.config(from_=7, to=10, textvariable=self.var_int)
        else:
            self.class_of_character = 'Your class is Rogue'
            self.class_lbl_result.configure(text=self.class_of_character, font=("Arial Bold", 12))
            self.specialization_combo['values'] = ('Rogue', 'Hunter')
            self.specialization_combo.current(0)
            self.var_str = IntVar()
            self.var_str.set(5)
            self.starting_characteristics_strength.config(from_=5, to=8, textvariable=self.var_str)
            self.var_agil = IntVar()
            self.var_agil.set(7)
            self.starting_characteristics_agility.config(from_=7, to=10, textvariable=self.var_agil)
            self.var_int = IntVar()
            self.var_int.set(3)
            self.starting_characteristics_intelligence.config(from_=3, to=6, textvariable=self.var_int)

    def change_specialization(self):
        text_specialization = self.specialization_value.get()
        self.specialization = 'Your specialization: ' + text_specialization
        self.specialization_lbl_result.configure(text=self.specialization, font=("Arial Bold", 12))
        if text_specialization == 'Tank':
            img_tank = ImageTk.PhotoImage(Image.open("tank.jpg"))
            self.panel.configure(image=img_tank)
            self.panel.image = img_tank
        elif text_specialization == 'Warrior':
            img_tank = ImageTk.PhotoImage(Image.open("warrior.jpg"))
            self.panel.configure(image=img_tank)
            self.panel.image = img_tank
        elif text_specialization == 'Mage':
            img_tank = ImageTk.PhotoImage(Image.open("mage.jpg"))
            self.panel.configure(image=img_tank)
            self.panel.image = img_tank
        elif text_specialization == 'Priest':
            img_tank = ImageTk.PhotoImage(Image.open("priest.jpg"))
            self.panel.configure(image=img_tank)
            self.panel.image = img_tank
        elif text_specialization == 'Rogue':
            img_tank = ImageTk.PhotoImage(Image.open("rogue.jpg"))
            self.panel.configure(image=img_tank)
            self.panel.image = img_tank
        elif text_specialization == 'Hunter':
            img_tank = ImageTk.PhotoImage(Image.open("hunter.jpg"))
            self.panel.configure(image=img_tank)
            self.panel.image = img_tank


    def change_characteristics(self):
        self.strenght = int(self.starting_characteristics_strength.get())
        self.agility = int(self.starting_characteristics_agility.get())
        self.intelligence = int(self.starting_characteristics_intelligence.get())
        sum_of_characteristics = self.strenght + self.agility + self.intelligence
        if sum_of_characteristics < 18:
            messagebox.showinfo('Error', 'Add more characteristics')
        elif sum_of_characteristics > 18:
            messagebox.showinfo('Error', 'Reduce characteristics')
        else:
            self.characteristics_text = 'Your characteristics:' + '\nStrength :' + str(self.strenght) \
                                        + '\nAgility: ' + str(self.agility) + '\nIntelligence: ' + str(
                self.intelligence)
            self.characteristics_lbl_result.configure(text=self.characteristics_text, font=("Arial Bold", 10))
            self.characteristics_lbl_result.place(x=250, y=350)

    def saved_сhronicle(self):
        self.text_chronicle = self.сhronicle_txt.get(1.0, "end")

    def cancel_create(self):
        exactly_cancel = messagebox.askyesno('!!!', 'Are you sure?')
        if exactly_cancel is True:
            self.main_window.destroy()
        else:
            return

    def create_character(self):
        if self.nickname == '':
            messagebox.showinfo('Error', 'Enter character name')
        elif self.number_class == 0:
            messagebox.showinfo('Error', 'Enter character class')
        elif self.specialization == '':
            messagebox.showinfo('Error', 'Enter character specialization')
        elif self.strenght == 0 or self.agility == 0 or self.intelligence == 0:
            messagebox.showinfo('Error', 'Check character characteristics')
        elif self.chk_license.get() is False:
            messagebox.showinfo('Error', 'Please agree to the license agreement')
        else:
            check_exactly_cancel = messagebox.askyesno('!!!', 'Are you sure?')
            if check_exactly_cancel is False:
                return
            else:
                save_text_1 = 'Your nickname is ' + self.nickname + '!' + '\n'
                save_text_2 = self.class_of_character + '.' + '\n'
                save_text_3 = self.specialization + '.' + '\n'
                save_text_4 = self.characteristics_text
                save_text_5 = '\n' + 'Сhronicle of your character: ' + self.text_chronicle
                with open("Your character.txt", "a") as file_txt:
                    file_txt.write(save_text_1)
                    file_txt.write(save_text_2)
                    file_txt.write(save_text_3)
                    file_txt.write(save_text_4)
                    if self.text_chronicle != '':
                        file_txt.write(save_text_5)
                    self.main_window.destroy()

    def create_window(self):
        self.main_window = Tk()
        self.main_window.geometry('900x950')
        self.main_window.title("Creation your character")
        self.hello_lbl = Label(self.main_window, text="Hello, " + self.name + '!', font=("Arial Bold", 15))
        self.hello_lbl.place(x=400, y=20)
        self.nike_name_lbl = Label(self.main_window, text="Character name:", font=("Arial Bold", 12))  # Nickname
        self.nike_name_lbl.place(x=20, y=50)
        self.nike_name_lbl_result = Label(self.main_window, text="Nickname will be here", font=("Arial Bold", 8))
        self.nike_name_lbl_result.place(x=160, y=53)
        self.nike_name_txt = Entry(self.main_window, width=50)
        self.nike_name_txt.focus()
        self.nike_name_txt.place(x=22, y=84)
        self.nike_name_btn = Button(self.main_window, text="Save", width=7, height=1, command=self.save_nickname)
        self.nike_name_btn.place(x=370, y=80)
        self.class_lbl = Label(self.main_window, text="Choose your class:", font=("Arial Bold", 12))  # Class
        self.class_lbl.place(x=20, y=125)
        self.selected_class = IntVar()
        self.class_lbl_result = Label(self.main_window, text="Class will be here", font=("Arial Bold", 8))
        self.class_lbl_result.place(x=250, y=175)
        self.first_class = Radiobutton(self.main_window, text='Warrior', value=1, font=("Arial Bold", 10),
                                       variable=self.selected_class)
        self.second_class = Radiobutton(self.main_window, text='Mage', value=2, font=("Arial Bold", 10),
                                        variable=self.selected_class)
        self.third_class = Radiobutton(self.main_window, text='Rogue', value=3, font=("Arial Bold", 10),
                                       variable=self.selected_class)
        self.class_btn = Button(self.main_window, text="Save",  width=7, height=1, command=self.change_class)
        self.first_class.place(x=20, y=150)
        self.second_class.place(x=20, y=175)
        self.third_class.place(x=20, y=200)
        self.class_btn.place(x=170, y=175)
        self.specialization_lbl = Label(self.main_window, text="Choose your specialization:",
                                        font=("Arial Bold", 12))  # Specialization
        self.specialization_lbl.place(x=20, y=240)
        self.specialization_value = StringVar()
        self.specialization_combo = ttk.Combobox(self.main_window, textvariable=self.specialization_value,
                                                 state='readonly',  width=15)
        if self.number_class == 0:
            self.specialization_combo['value'] = ("At first choose your class")
        self.specialization_combo.place(x=20, y=275)
        self.specialization_lbl_result = Label(self.main_window, text="Specialization will be here",
                                               font=("Arial Bold", 8))
        self.specialization_lbl_result.place(x=250, y=273)
        self.specialization_btn = Button(self.main_window, text="Save", width=7, height=1,
                                         command=self.change_specialization)
        self.specialization_btn.place(x=170, y=272)
        self.starting_characteristics_lbl = Label(self.main_window, text="Change your starting characteristics(add 3):",
                                                  font=("Arial Bold", 12))  # Starting characteristics
        self.starting_characteristics_lbl.place(x=20, y=320)
        self.var_str = IntVar()
        self.var_str.set(0)
        self.starting_characteristics_strength = Spinbox(self.main_window, from_=0, to=0, width=5,
                                                         textvariable=self.var_str)
        self.str_lbl = Label(self.main_window, text="Strength:", font=("Arial Bold", 10))
        self.var_agil = IntVar()
        self.var_agil.set(0)
        self.starting_characteristics_agility = Spinbox(self.main_window, from_=0, to=0, width=5,
                                                        textvariable=self.var_agil)
        self.agil_lbl = Label(self.main_window, text="Agility:", font=("Arial Bold", 10))
        self.var_int = IntVar()
        self.var_int.set(0)
        self.starting_characteristics_intelligence = Spinbox(self.main_window, from_=0, to=0, width=5,
                                                             textvariable=self.var_int)
        self.int_lbl = Label(self.main_window, text="Intelligence:", font=("Arial Bold", 10))
        self.str_lbl.place(x=20, y=350)
        self.starting_characteristics_strength.place(x=110, y=350)
        self.agil_lbl.place(x=20, y=375)
        self.starting_characteristics_agility.place(x=110, y=376)
        self.int_lbl.place(x=20, y=400)
        self.starting_characteristics_intelligence.place(x=110, y=402)
        self.characteristics_btn = Button(self.main_window, text="Save", width=7, height=1,
                                          command=self.change_characteristics)
        self.characteristics_btn.place(x=170, y=376)
        self.characteristics_lbl_result = Label(self.main_window, text="Characteristics will be here:",
                                                font=("Arial Bold", 8))
        self.characteristics_lbl_result.place(x=250, y=376)
        self.сhronicle_lbl = Label(self.main_window, text="Please, write backstory of your character:",
                                   font=("Arial Bold", 12))  # Starting characteristics
        self.сhronicle_lbl.place(x=20, y=440)
        self.сhronicle_txt = scrolledtext.ScrolledText(self.main_window, width=103, height=20)  # Сhronicle character's
        self.сhronicle_txt.place(x=20, y=475)
        self.сhronicle_btn = Button(self.main_window, text="Save", width=7, height=1, command=self.saved_сhronicle)
        self.сhronicle_btn.place(x=793, y=805)
        self.chk_license = BooleanVar()
        self.license_chk = Checkbutton(self.main_window, text='I agree to the license agreement',
                                       variable=self.chk_license, font=("Arial Bold", 12))
        self.license_chk.place(x=20, y=840)
        self.create_btn = Button(self.main_window, text="Create", width=10, height=2, command=self.create_character)
        self.create_btn.place(x=170, y=885)
        self.cancel_btn = Button(self.main_window, text="Cancel", width=10, height=2, command=self.cancel_create)
        self.cancel_btn.place(x=600, y=885)
        img = ImageTk.PhotoImage(Image.open("pic.bmp"))
        self.panel = Label(self.main_window, image=img)
        self.panel.place(x=490, y=70)
        self.main_window.mainloop()
