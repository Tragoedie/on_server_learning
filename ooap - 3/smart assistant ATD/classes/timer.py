class Timer:

    # конструктор:
    # создание объекта таймера.
    def __init__(self):
        pass

    # команды:
    # установить таймер.
    # предусловие: dt валиден.
    # постусловие: запущен обратный отсчёт.
    def set_enddate(self, dt: DateTime):
        pass

    # предусловие: таймер запущен.
    # постусловие: отсчёт приостановлен.
    def pause(self):
        pass

    # вызвать уведомление
    # предусловие: наступило событие напоминания.
    # постусловие: воспроизведение звукового оповещения.
    def notify(self):
        pass
