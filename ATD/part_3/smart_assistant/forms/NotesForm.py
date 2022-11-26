from tkinter import *
from tkinter import ttk, font

NOTES_WIDTH = 380
NOTES_HEIGHT = 250
FRAME_WIDTH = NOTES_WIDTH // 2 * 0.9
FRAME_HEIGHT = NOTES_HEIGHT * 0.9


class NotesForm:

    def __init__(self):
        self.win_notes = Tk()
        self.win_notes.geometry('{0}x{1}'.format(NOTES_WIDTH, NOTES_HEIGHT))
        self.win_notes.title("Заметки")

        self.left_frame = ttk.Frame(self.win_notes, width=FRAME_WIDTH, height=FRAME_HEIGHT, borderwidth=1, relief=SOLID)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)

        self.name_label = ttk.Label(self.left_frame, text="Заметки:", font=("Arial", 12))
        self.f = font.Font(self.name_label, self.name_label.cget("font"))
        self.f.configure(underline=True), self.name_label.configure(font=self.f)
        self.name_label.grid(row=0, column=0, sticky="nsw")

        self.alarm_tree = ttk.Treeview(self.left_frame, column="alarm", show="")
        self.alarm_tree.grid(row=1, column=0, sticky="nsew")
        self.alarm_tree.column("#1", stretch=NO, width=160)
        self.scrollbar = ttk.Scrollbar(self.left_frame, orient=VERTICAL, command=self.alarm_tree.yview)
        self.alarm_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=0, sticky="nse")

        self.right_frame = ttk.Frame(self.win_notes, width=FRAME_WIDTH, height=FRAME_HEIGHT // 2, borderwidth=1, relief=SOLID)
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")
        self.btn_add = Button(self.right_frame, text="Добавить", width=20, command='')
        self.btn_add.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.btn_change = Button(self.right_frame, text="Изменить", width=20, command='')
        self.btn_change.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.btn_delete = Button(self.right_frame, text="Удалить", width=20, command='')
        self.btn_delete.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.win_notes.mainloop()
