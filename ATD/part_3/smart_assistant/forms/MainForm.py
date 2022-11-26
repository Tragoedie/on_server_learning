from tkinter import *
from on_server_learning.ATD.part_3.smart_assistant.forms.AlarmClockForm import AlarmClockForm
from on_server_learning.ATD.part_3.smart_assistant.forms.CalculatorForm import Calculator
from on_server_learning.ATD.part_3.smart_assistant.forms.StopWatchForm import StopWatchForm
from on_server_learning.ATD.part_3.smart_assistant.forms.TimerForm import TimerForm
from on_server_learning.ATD.part_3.smart_assistant.forms.NotesForm import NotesForm
from on_server_learning.ATD.part_3.smart_assistant.forms.ScheduleForm import ScheduleForm


class MainForm:
    STATUS_START_ALARM_ERR = 0
    STATUS_START_ALARM_OK = 1
    STATUS_START_TIMER_ERR = 0
    STATUS_START_TIMER_OK = 1
    STATUS_START_STOPWATCH_ERR = 0
    STATUS_START_STOPWATCH_OK = 1
    STATUS_START_CALCULATOR_ERR = 0
    STATUS_START_CALCULATOR_OK = 1
    STATUS_START_NOTES_ERR = 0
    STATUS_START_NOTES_OK = 1
    STATUS_START_SCHEDULE_ERR = 0
    STATUS_START_SCHEDULE_OK = 1
    STATUS_START_FINANCE_ERR = 0
    STATUS_START_FINANCE_OK = 1

    def __init__(self):

        self.alarmclock_form = None
        self.status_start_alarm = MainForm.STATUS_START_ALARM_ERR
        self.calculator_form = None
        self.status_start_calculator = MainForm.STATUS_START_CALCULATOR_ERR
        self.stopwatch_form = None
        self.status_start_stopwatch = MainForm.STATUS_START_STOPWATCH_ERR
        self.notes_form = None
        self.status_start_notes = MainForm.STATUS_START_NOTES_ERR
        self.timer_form = None
        self.status_start_timer = MainForm.STATUS_START_TIMER_ERR
        self.schedule_form = None
        self.status_start_schedule = MainForm.STATUS_START_SCHEDULE_ERR

        self.window = Tk()
        self.window.geometry('710x40')
        self.window.update_idletasks()
        s = self.window.geometry()
        s = s.split('+')
        s = s[0].split('x')
        self.width_window = int(s[0])
        w = self.window.winfo_screenwidth()
        w = w - self.width_window
        h = 0

        self.window.geometry('+{0}+{1}'.format(w, h))
        self.window.resizable(False, False)
        self.window.title("Добро пожаловать в приложение Умный ассистент")

        self.name_btn_alarm = Button(text="Будильник", width=12, height=1, command=self.start_alarmclock)
        self.name_btn_alarm.place(x=10, y=8)

        self.name_btn_timer = Button(text="Таймер", width=12, height=1, command=self.start_timer)
        self.name_btn_timer.place(x=110, y=8)

        self.name_btn_stopwatch = Button(self.window, text="Секундомер", width=12, height=1,
                                         command=self.start_stopwatch)
        self.name_btn_stopwatch.place(x=210, y=8)

        self.name_btn_calc = Button(self.window, text="Калькулятор", width=12, height=1, command=self.start_calculator)
        self.name_btn_calc.place(x=310, y=8)

        self.name_btn_notes = Button(self.window, text="Заметки", width=12, height=1, command=self.start_notes)
        self.name_btn_notes.place(x=410, y=8)

        self.name_btn_reminders = Button(self.window, text="Напоминания", width=12, height=1,
                                         command=self.start_schedule)
        self.name_btn_reminders.place(x=510, y=8)

        self.name_btn_finances = Button(self.window, text="Финансы", width=12, height=1, command='')
        self.name_btn_finances.place(x=610, y=8)

        self.window.mainloop()

    def start_alarmclock(self):
        try:
            self.alarmclock_form = AlarmClockForm()
            self.status_start_alarm = MainForm.STATUS_START_ALARM_OK
        except:
            self.status_start_alarm = MainForm.STATUS_START_ALARM_ERR

    def start_timer(self):
        try:
            self.timer_form = TimerForm()
            self.status_start_timer = MainForm.STATUS_START_TIMER_OK
        except:
            self.status_start_timer = MainForm.STATUS_START_TIMER_ERR

    def start_stopwatch(self):
        try:
            self.stopwatch_form = StopWatchForm()
            self.status_start_stopwatch = MainForm.STATUS_START_STOPWATCH_OK
        except:
            self.status_start_stopwatch = MainForm.STATUS_START_STOPWATCH_ERR

    def start_calculator(self):
        try:
            self.calculator_form = Calculator()
            self.status_start_calculator = MainForm.STATUS_START_CALCULATOR_OK
        except:
            self.status_start_calculator = MainForm.STATUS_START_CALCULATOR_ERR

    def start_notes(self):
        try:
            self.notes_form = NotesForm()
            self.status_start_notes = MainForm.STATUS_START_NOTES_OK
        except:
            self.status_start_notes = MainForm.STATUS_START_NOTES_ERR

    def start_schedule(self):
        try:
            self.schedule_form = ScheduleForm()
            self.status_start_schedule = MainForm.STATUS_START_SCHEDULE_OK
        except:
            self.status_start_schedule = MainForm.STATUS_START_SCHEDULE_ERR

    def start_finance_analyser(self):
        pass

