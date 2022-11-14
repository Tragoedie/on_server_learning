class MainForm:
    # константы
    STATUS_START_ALARM_ERR = 0  # запуск будильника завершен с ошибкой
    STATUS_START_ALARM_OK = 1  # запуск будильника отработал нормально
    STATUS_START_TIMER_ERR = 0  # запуск таймера завершен с ошибкой
    STATUS_START_TIMER_OK = 1  # запуск таймера отработал нормально
    STATUS_START_STOPWATCH_ERR = 0  # запуск секундомера завершен с ошибкой
    STATUS_START_STOPWATCH_OK = 1  # запуск секундомера отработал нормально
    STATUS_START_CALCULATOR_ERR = 0  # запуск калькулятора завершен с ошибкой
    STATUS_START_CALCULATOR_OK = 1  # запуск калькулятора отработал нормально
    STATUS_START_NOTES_ERR = 0  # запуск заметок завершен с ошибкой
    STATUS_START_NOTES_OK = 1  # запуск заметок отработал нормально
    STATUS_START_SCHEDULE_ERR = 0  # запуск календаря завершен с ошибкой
    STATUS_START_SCHEDULE_OK = 1  # запуск календаря отработал нормально
    STATUS_START_FINANCE_ERR = 0  # запуск финансового анализатора завершен с ошибкой
    STATUS_START_FINANCE_OK = 1  # запуск финансового анализатора отработал нормально

    # конструктор:
    # постусловие: приложение запущено
    def __init__(self):
        pass

    # команды:
    # вызов будильника.
    # постусловие: форма будильника создана.
    def start_alarmclock(self):
        pass

    # вызов таймера.
    # постусловие: форма таймера создана.
    def start_timer(self):
        pass

    # вызов секундомера.
    # постусловие: форма секундомера создана.
    def start_stopwatch(self):
        pass

    # вызов калькулятора.
    # постусловие: форма калькулятора создана.
    def start_calculator(self):
        pass

    # вызов заметок.
    # постусловие: форма заметок создана.
    def start_notes(self):
        pass

    # вызов календаря c напоминаниями.
    # постусловие: форма календаря создана.
    def start_schedule(self):
        pass

    # вызов финансового анализатора.
    # постусловие: форма финансового анализатора создана.
    def start_finance_analyser(self):
        pass

    # завершение приложения.
    # постусловие: приложение выключено.
    def quit(self):
        pass
