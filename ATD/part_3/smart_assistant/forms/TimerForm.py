from tkinter import *

TIMER_WIDTH = 300
TIMER_HEIGHT = 280


class TimerForm:

    def __init__(self):
        self.win_timer = Tk()
        self.win_timer.geometry('{0}x{1}'.format(TIMER_WIDTH, TIMER_HEIGHT))
        self.win_timer.title("Таймер")

        self.timer_label = Label(self.win_timer, text="00:00:00", font=('Helvetica', 48))
        self.timer_label.grid(row=0, column=0, columnspan=2, ipadx=6, ipady=55, padx=15, pady=5)

        self.start_btn = Button(self.win_timer, text="Старт", width=15, command='')
        self.start_btn.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

        self.stop_btn = Button(self.win_timer, text="Стоп", width=15, command='')
        self.stop_btn.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        self.win_timer.mainloop()
