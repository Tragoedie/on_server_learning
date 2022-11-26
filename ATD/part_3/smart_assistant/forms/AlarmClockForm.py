from tkinter import *
from tkinter import ttk, font
from on_server_learning.ATD.part_3.smart_assistant.forms.AlarmChange import AlarmAdd

ALARM_WIDTH = 400
ALARM_HEIGHT = 250
FRAME_WIDTH = ALARM_WIDTH // 2 * 0.9
FRAME_HEIGHT = ALARM_HEIGHT * 0.9


class AlarmClockForm:

    def __init__(self):
        self.selected = -1

        self.win_alarm = Tk()
        self.win_alarm.geometry('{0}x{1}'.format(ALARM_WIDTH, ALARM_HEIGHT))
        self.win_alarm.title("Будильник")

        self.left_frame = ttk.Frame(self.win_alarm, width=FRAME_WIDTH, height=FRAME_HEIGHT, borderwidth=1, relief=SOLID)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)
        self.name_label = ttk.Label(self.left_frame, text="Будильники:", font=("Arial", 12))
        self.f = font.Font(self.name_label, self.name_label.cget("font"))
        self.f.configure(underline=True), self.name_label.configure(font=self.f)
        self.name_label.grid(row=0, column=0, sticky="nsw")

        self.alarm_tree = ttk.Treeview(self.left_frame, column="alarm", show="")
        self.alarm_tree.grid(row=1, column=0, sticky="nsew")
        self.alarm_tree.column("#1", stretch=NO, width=160)

        def select(event):
            self.selected = self.alarm_tree.selection()[0]
        self.alarm_tree.bind("<<TreeviewSelect>>", select)

        self.alarm_tree.insert("", END, values='09:20:00')
        self.alarm_tree.insert("", END, values='10:20:00')
        self.alarm_tree.insert("", END, values='11:20:00')

        self.scrollbar = ttk.Scrollbar(self.left_frame, orient=VERTICAL, command=self.alarm_tree.yview)
        self.alarm_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=0, sticky="nse")

        self.right_frame = ttk.Frame(self.win_alarm, width=FRAME_WIDTH, height=FRAME_HEIGHT // 2, borderwidth=1, relief=SOLID)
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")
        self.btn_add = Button(self.right_frame, text="Добавить", width=20, command=self.AddAlarm)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.btn_change = Button(self.right_frame, text="Изменить", width=20, command='')
        self.btn_change.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.btn_delete = Button(self.right_frame, text="Удалить", width=20, command='')
        self.btn_delete.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.win_alarm.mainloop()

    def AddAlarm(self):
        AlarmAdd()


test = AlarmClockForm()