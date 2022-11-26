from datetime import datetime


class DateTime:
    # константы
    DATETIME_STATUS_VALID = 0
    DATETIME_STATUS_NULL = -1
    DATETIME_STATUS_INVALID = 1

    # конструктор:
    # cоздание объекта ДатаВремя.
    def __init__(self):
        self.__dt = 0.0
        self.__status = self.DATETIME_STATUS_NULL

    # команды:
    # установить дату.
    # предусловие: dt > 0.
    # постусловие: установлено дата/время, дата валидна.
    def set_date(self, dt):
        if dt > 0:
            self.__status = self.DATETIME_STATUS_VALID
            self.__dt = dt
        else:
            self.__status = self.DATETIME_STATUS_INVALID
            self.__dt = 0.0

    def is_valid(self):
        return self.__status == self.DATETIME_STATUS_VALID

    # установить текущее время.
    # постусловие: записана текущая системная дата.
    def set_current_time(self):
        self.__dt = datetime.now()

    #  запросы:
    #  Получить год/месяц/день/час/минуту/секунду.
    #  предусловие: дата валидна.
    #  постусловие: получено целое значение > 0.
    def get_year(self):  # /month/day/hour/minute/second
        pass

dt = DateTime()
dt.set_current_time()