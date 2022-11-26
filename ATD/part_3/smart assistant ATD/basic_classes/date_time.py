class DateTime:
    # константы
    DATETIME_STATUS_VALID = 0
    DATETIME_STATUS_NULL = -1
    DATETIME_STATUS_INVALID = 1

    # конструктор:
    # cоздание объекта ДатаВремя.
    def __init__(self):
        pass

    # команды:
    # установить дату.
    # предусловие: dt > 0.
    # постусловие: установлено дата/время, дата валидна.
    def set_date(self, dt: float):
        pass

    # установить текущее время.
    # постусловие: записана текущая системная дата.
    def set_current_time(self):
        pass

    #  запросы:
    #  Получить год/месяц/день/час/минуту/секунду.
    #  предусловие: дата валидна.
    #  постусловие: получено целое значение > 0.
    def get_year(self):  # /month/day/hour/minute/second
        pass
