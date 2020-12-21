from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import Checkbutton


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
        self.nickname = "Your character name:  {}".format(self.nike_name_txt.get())
        self.nike_name_lbl_result.configure(text=self.nickname, font=("Arial Bold", 10))

    def change_class(self):
        self.number_class = self.selected_class.get()
        if self.number_class == 1:
            self.class_of_character = 'Your class is Warrior'
            self.class_lbl_result.configure(text=self.class_of_character, font=("Arial Bold", 10))
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
            self.class_lbl_result.configure(text=self.class_of_character, font=("Arial Bold", 10))
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
            self.class_lbl_result.configure(text=self.class_of_character, font=("Arial Bold", 10))
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
        self.specialization = "Your specialization:  {}".format(self.specialization_value.get())
        self.specialization_lbl_result.configure(text=self.specialization, font=("Arial Bold", 10))

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
            self.characteristics_text = 'Your characteristics:' + '\n Strength :' + str(self.strenght) \
                                        + '\nAgility: ' + str(self.agility) + '\nIntelligence: ' + str(
                self.intelligence)
            self.characteristics_lbl_result.configure(text=self.characteristics_text, font=("Arial Bold", 10))

    def saved_сhronicle(self):
        self.text_chronicle = self.сhronicle_txt.get(1.0, "end")

    def cancel_create(self):
        exactly_cancel = messagebox.askyesno('!!!', 'Are you sure?')
        if exactly_cancel == True:
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
                save_text_1 = self.nickname
                save_text_2 = self.class_of_character
                save_text_3 = self.specialization
                save_text_4 = self.characteristics_text
                save_text_5 = self.text_chronicle
                with open("Your character.txt", "a") as file_txt:
                    file_txt.write(save_text_1)
                    file_txt.write(save_text_2)
                    file_txt.write(save_text_3)
                    file_txt.write(save_text_4)
                    if self.text_chronicle != '':
                        file_txt.write(save_text_5)

    def create_window(self):
        self.main_window = Tk()
        #self.main_window.geometry('1000x900')
        self.main_window.columnconfigure(8, minsize=30)
        self.main_window.rowconfigure(16, minsize=70)
        self.main_window.title("Creation your character")

        self.hello_lbl = Label(self.main_window, text="Hello, "+self.name, font=("Arial Bold", 15))
        self.hello_lbl.grid(column=1, row=0)
        self.nike_name_lbl = Label(self.main_window, text="Enter character name:", font=("Arial Bold", 10))  # Nickname
        self.nike_name_lbl.grid(column=0, row=1,  columnspan=3, sticky='w', padx=20)
        self.nike_name_lbl_result = Label(self.main_window, text="Nickname will be here", font=("Arial Bold", 8))
        self.nike_name_lbl_result.grid(column=4, row=2, sticky='w', padx=10)
        self.nike_name_txt = Entry(self.main_window, width=50)
        self.nike_name_txt.focus()
        self.nike_name_txt.grid(column=0, row=2, columnspan=5, sticky='w', padx=20)
        self.nike_name_btn = Button(self.main_window, text="Save", width=7, height=1, command=self.save_nickname)
        self.nike_name_btn.grid(column=3, row=2, padx=5)
        self.class_lbl = Label(self.main_window, text="Choose your class:", font=("Arial Bold", 10))  # Class
        self.class_lbl.grid(column=0, row=3, columnspan=3, sticky='w', padx=20)
        self.selected_class = IntVar()
        self.class_lbl_result = Label(self.main_window, text="Class will be here", font=("Arial Bold", 8))
        self.class_lbl_result.grid(column=4, row=4, sticky='w')
        self.first_class = Radiobutton(self.main_window, text='Warrior', value=1, font=("Arial Bold", 10), variable=self.selected_class)
        self.second_class = Radiobutton(self.main_window, text='Mage', value=2, font=("Arial Bold", 10), variable=self.selected_class)
        self.third_class = Radiobutton(self.main_window, text='Rogue', value=3, font=("Arial Bold", 10), variable=self.selected_class)
        self.class_btn = Button(self.main_window, text="Save",  width=7, height=1, command=self.change_class)
        self.first_class.grid(column=0, row=4, sticky='w', padx=20)
        self.second_class.grid(column=1, row=4, sticky='w')
        self.third_class.grid(column=2, row=4, sticky='w', padx=20)
        self.class_btn.grid(column=3, row=4)
        self.specialization_lbl = Label(self.main_window, text="Choose your specialization:",
                                        font=("Arial Bold", 10))  # Specialization
        self.specialization_lbl.grid(column=0, row=5,  columnspan=3, sticky='w', padx=20)
        self.specialization_value = StringVar()
        self.specialization_combo = ttk.Combobox(self.main_window, textvariable=self.specialization_value,
                                                 state='readonly',  width=50)
        if self.number_class == 0:
            self.specialization_combo['value'] = ("At first choose your class")
        self.specialization_combo.grid(column=0, row=6, columnspan=5, sticky='w', padx=20)
        self.specialization_lbl_result = Label(self.main_window, text="Specialization will be here",
                                               font=("Arial Bold", 8))
        self.specialization_lbl_result.grid(column=4, row=6, sticky='w')
        self.specialization_btn = Button(self.main_window, text="Save", width=7, height=1,  command=self.change_specialization)
        self.specialization_btn.grid(column=3, row=6)
        self.starting_characteristics_lbl = Label(self.main_window, text="Change your starting characteristics(add 3):",
                                                  font=("Arial Bold", 10))  # Starting characteristics
        self.starting_characteristics_lbl.grid(column=0, row=8, columnspan=5, sticky='w', padx=20)
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
        self.str_lbl.grid(column=0, row=9, sticky='w', padx=20)
        self.starting_characteristics_strength.grid(column=1, row=9, sticky='w')
        self.agil_lbl.grid(column=0, row=10, sticky='w', padx=20)
        self.starting_characteristics_agility.grid(column=1, row=10, sticky='w')
        self.int_lbl.grid(column=0, row=11, sticky='w', padx=20)
        self.starting_characteristics_intelligence.grid(column=1, row=11, sticky='w')
        self.characteristics_btn = Button(self.main_window, text="Save", width=7, height=1, command=self.change_characteristics)
        self.characteristics_btn.grid(column=2, row=11, padx=20)
        self.characteristics_lbl_result = Label(self.main_window, text="Characteristics will be here:",
                                                font=("Arial Bold", 10))
        self.characteristics_lbl_result.grid(column=3, row=8, columnspan=5, sticky='w')

        self.сhronicle_lbl = Label(self.main_window, text="Please, write backstory of your character:", font=("Arial Bold", 10))  # Starting characteristics
        self.сhronicle_lbl.grid(column=0, row=12, sticky='w', padx=20)
        self.сhronicle_txt = scrolledtext.ScrolledText(self.main_window, width=50, height=10)  # Сhronicle of your character's life
        self.сhronicle_txt.grid(column=0, row=13, sticky='w', padx=20)
        self.сhronicle_btn = Button(self.main_window, text="Save", width=7, height=1, command=self.saved_сhronicle)
        self.сhronicle_btn.grid(column=2, row=13, sticky='s')

        self.chk_license = BooleanVar()
        self.license_chk = Checkbutton(self.main_window, text='I agree to the license agreement',
                                       variable=self.chk_license)
        self.license_chk.grid(column=0, row=15, sticky='w', padx=20)
        self.create_btn = Button(self.main_window, text="Create", command=self.create_character)
        self.create_btn.grid(column=0, row=16, sticky='w', padx=20)
        self.cancel_btn = Button(self.main_window, text="Cancel", command=self.cancel_create)
        self.cancel_btn.grid(column=1, row=16, sticky='w', padx=20)
        self.main_window.mainloop()
