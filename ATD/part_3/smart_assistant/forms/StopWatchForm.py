from tkinter import *
from on_server_learning.ATD.part_3.smart_assistant.classes.stopwatch import StopWatch

TIMER_WIDTH = 300
TIMER_HEIGHT = 280


class StopWatchForm:

    # конструктор:
    # создание формы секундомера.
    def __init__(self):
        self.is_active = False

        self.win_watch = Tk()
        self.win_watch.geometry('{0}x{1}'.format(TIMER_WIDTH, TIMER_HEIGHT))
        self.win_watch.title("Секундомер")

        self.timer_label = Label(self.win_watch, text="00:00:00:0", font=('Helvetica', 42))
        self.timer_label.grid(row=0, column=0, columnspan=2, ipadx=6, ipady=55, padx=15, pady=5)

        self.start_btn = Button(self.win_watch, text="Старт", width=15, command=self.start)
        self.start_btn.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

        self.stop_btn = Button(self.win_watch, text="Стоп", width=15, command=self.stop)
        self.stop_btn.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

        self.win_watch.mainloop()

    # команды:
    # запустить секундомер
    # предусловие: секундомер неактивен
    # постусловие: начался отчёт
    def start(self):
        if self.is_active:
            return
        sw = StopWatch()
        self.is_active = True

        def update_clock():
            if self.is_active:
                self.timer_label.configure(text=sw.print())
                self.timer_label.after(100, update_clock)
        update_clock()

    # установить чекпоинт.
    # предусловие: секундомер активен.
    # постусловие: сохранен интервал.
    def place_checkpoint(self):
        pass

    # остановить секундомер.
    # предусловие:	секундомер активен.
    # постусловие: секундомер неактивен.
    def stop(self):
        if self.is_active:
            self.is_active = False
            # self.timer_label.configure(text="00:00:00:0")

