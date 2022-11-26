from tkinter import *


class Calculator:

    def __init__(self):
        self.windows = Tk()
        self.windows.geometry("312x324")
        self.windows.resizable(0, 0)
        self.windows.title("Calculator")

        self.expression = ""
        self.input_text = StringVar()
        self.input_frame = Frame(
            self.windows,
            width=312,
            height=50,
            bd=0,
            highlightbackground="black",
            highlightcolor="black",
            highlightthickness=2,
        )
        self.input_frame.pack(side=TOP)
        self.input_field = Entry(
            self.input_frame,
            font=('arial', 18, 'bold'),
            textvariable=self.input_text,
            width=50,
            bg="#eee",
            bd=0,
            justify=RIGHT
        )
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)

        self.btns_frame = Frame(self.windows, width=312, height=272.5, bg="grey")
        self.btns_frame.pack()
        self.clear = Button(self.btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                            command=lambda: self.bt_clear())
        self.clear.grid(row=0, column=0, padx=1, pady=1)
        self.bracket_open = Button(
            self.btns_frame,
            text="(",
            fg="black",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self.btn_click("("),
        )
        self.bracket_open.grid(row=0, column=1, padx=1, pady=1)
        self.bracket_close = Button(self.btns_frame, text=")", fg="black", width=10, height=3, bd=0, bg="#eee",
                                    cursor="hand2",
                                    command=lambda: self.btn_click(")"))
        self.bracket_close.grid(row=0, column=2, padx=1, pady=1)
        self.divide = Button(self.btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                             command=lambda: self.btn_click("/"))
        self.divide.grid(row=0, column=3, padx=1, pady=1)
        self.seven = Button(self.btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                            command=lambda: self.btn_click(7))
        self.seven.grid(row=1, column=0, padx=1, pady=1)
        self.eight = Button(self.btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                            command=lambda: self.btn_click(8))
        self.eight.grid(row=1, column=1, padx=1, pady=1)
        self.nine = Button(self.btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                           command=lambda: self.btn_click(9))
        self.nine.grid(row=1, column=2, padx=1, pady=1)
        self.multiply = Button(self.btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                               cursor="hand2",
                               command=lambda: self.btn_click("*"))
        self.multiply.grid(row=1, column=3, padx=1, pady=1)
        self.four = Button(self.btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                           command=lambda: self.btn_click(4))
        self.four.grid(row=2, column=0, padx=1, pady=1)
        self.five = Button(self.btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                           command=lambda: self.btn_click(5))
        self.five.grid(row=2, column=1, padx=1, pady=1)
        self.six = Button(self.btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: self.btn_click(6))
        self.six.grid(row=2, column=2, padx=1, pady=1)
        self.minus = Button(self.btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                            command=lambda: self.btn_click("-"))
        self.minus.grid(row=2, column=3, padx=1, pady=1)
        self.one = Button(self.btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: self.btn_click(1))
        self.one.grid(row=3, column=0, padx=1, pady=1)
        self.two = Button(self.btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: self.btn_click(2))
        self.two.grid(row=3, column=1, padx=1, pady=1)
        self.three = Button(self.btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                            command=lambda: self.btn_click(3))
        self.three.grid(row=3, column=2, padx=1, pady=1)
        self.plus = Button(self.btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                           command=lambda: self.btn_click("+"))
        self.plus.grid(row=3, column=3, padx=1, pady=1)
        self.zero = Button(self.btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
                           command=lambda: self.btn_click(0))
        self.zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        self.point = Button(self.btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                            command=lambda: self.btn_click("."))
        self.point.grid(row=4, column=2, padx=1, pady=1)
        self.equals = Button(self.btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                             command=lambda: self.bt_equal())
        self.equals.grid(row=4, column=3, padx=1, pady=1)
        self.windows.mainloop()

    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def bt_clear(self):
        self.expression = ""
        self.input_text.set("")

    def bt_equal(self):
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression = ""
