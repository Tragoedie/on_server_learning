from tkinter import *
from tkinter import messagebox
from datetime import datetime


class AlarmAdd:
    def __init__(self):
        self.time = datetime.now()

        self.win_add = Tk()
        self.win_add.geometry("250x200")
        self.win_add.title("Добавление/Изменение")

        self.label_frame = Frame(self.win_add)
        self.label_frame.grid(column=0, row=0)
        self.name_lbl = Label(self.label_frame, text="Введите время: ", font=("Arial Bold", 10))
        self.name_lbl.grid(row=0, column=0, sticky='nwse', pady=20)

        self.time_frame = Frame(self.win_add)
        self.time_frame.grid(column=0, row=1)
        self.hour = StringVar()
        self.minute = StringVar()
        self.second = StringVar()
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
        self.hourEntry = Entry(self.time_frame, width=3, font=("Arial", 18, ""),
                          textvariable=self.hour)
        self.hourEntry.grid(row=1, column=0, pady=10)
        self.minuteEntry = Entry(self.time_frame, width=3, font=("Arial", 18, ""),
                            textvariable=self.minute)
        self.minuteEntry.grid(row=1, column=1, pady=10)
        self.secondEntry = Entry(self.time_frame, width=3, font=("Arial", 18, ""),
                            textvariable=self.second)
        self.secondEntry.grid(row=1, column=2, pady=10)

        self.btn_frame = Frame(self.win_add)
        self.btn_frame.grid(column=0, row=2)
        self.btn_OK = Button(self.btn_frame, text='Добавить/Изменить', bd='5', command=self.confirm_change)
        self.btn_OK.grid(row=0, column=0, columnspan=2, padx=10, pady=30)
        self.btn_NO = Button(self.btn_frame, text='Отмена', bd='5', command=self.confirm_cancel)
        self.btn_NO.grid(row=0, column=2, padx=10, pady=30)
        self.win_add.mainloop()

    def confirm_change(self):
        check_cancel = messagebox.askyesno("Добавить/удалить", "Сохранить будильник?")
        if check_cancel:
            #  тут save
            self.win_add.destroy()

    def confirm_cancel(self):
        self.win_add.destroy()
