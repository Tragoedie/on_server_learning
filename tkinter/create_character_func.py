from on_server_learning.tkinter.class_create_place import create_character
from tkinter import *
from tkinter import messagebox


def get_name():
    check_exactly_cancel = messagebox.askyesno('!!!', 'Are you sure?')
    if check_exactly_cancel is False:
        return
    else:
        human_name = "{}".format(name_enter.get())
        character = create_character(human_name)
        window.destroy()
        character.create_window()


window = Tk()
window.geometry('250x100')
window.title("Hello =)")
name_lbl = Label(text="Enter your name, please: ", font=("Arial Bold", 10))
name_enter = Entry()
name_btn = Button(window, text="Ok", width=7, height=1, command=get_name)
name_lbl.pack(padx=5, pady=5, ipadx=5, ipady=5)
name_enter.pack()
name_btn.pack(padx=5, pady=5, ipadx=5, ipady=5)
window.mainloop()


