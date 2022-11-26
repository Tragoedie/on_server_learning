from tkinter import *
import calendar
import datetime


class ScheduleForm:
    def __init__(self):
        self.win_schedule = Tk()
        self.win_schedule.title('Calendar')

        self.days = []
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month

        self.prew_button = Button(self.win_schedule, text='<', command=self.prev)
        self.prew_button.grid(row=0, column=0, sticky='nsew')
        self.next_button = Button(self.win_schedule, text='>', command=self.next)
        self.next_button.grid(row=0, column=6, sticky='nsew')
        self.info_label = Label(
            self.win_schedule, text='0', width=1, height=1, font=('Verdana', 16, 'bold'), fg='blue'
        )
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')
        for n in range(7):
            self.lbl = Label(
                self.win_schedule, text=calendar.day_abbr[n], width=1, height=1, font=(
                    'Verdana', 10, 'normal'
                ), fg='darkblue'
            )
            self.lbl.grid(row=1, column=n, sticky='nsew')

        for row in range(6):
            for col in range(7):
                self.lbl = Label(
                    self.win_schedule, text='0', width=4, height=2, font=('Verdana', 16, 'bold')
                )
                self.lbl.grid(row=row+2, column=col, sticky='nsew')
                self.days.append(self.lbl)

        self.fill()
        self.win_schedule.mainloop()

    def prev(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def fill(self):
        self.info_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
        month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            prew_month_days = calendar.monthrange(self.year-1, 12)[1]
        else:
            prew_month_days = calendar.monthrange(self.year, self.month - 1)[1]
        week_day = calendar.monthrange(self.year, self.month)[0]
        for n in range(month_days):
            self.days[n + week_day]['text'] = n+1
            self.days[n + week_day]['fg'] = 'black'
            if self.year == self.now.year and self.month == self.now.month and n == self.now.day:
                self.days[n + week_day]['background'] = 'green'
            else:
                self.days[n + week_day]['background'] = 'lightgray'
        for n in range(week_day):
            self.days[week_day - n - 1]['text'] = prew_month_days - n
            self.days[week_day - n - 1]['fg'] = 'gray'
            self.days[week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6*7 - month_days - week_day):
            self.days[week_day + month_days + n]['text'] = n+1
            self.days[week_day + month_days + n]['fg'] = 'gray'
            self.days[week_day + month_days + n]['background'] = '#f3f3f3'
