class FinanceAnalyzer:
    # константы категории расходов
    SPEND_NONE = 0
    SPEND_FOOD = 1
    SPEND_CLOTHES = 2
    SPEND_ENTERTAINMENT = 3
    SPEND_TRANSPORT = 4
    SPEND_COURSERS = 5
    SPEND_PETS = 6
    SPEND_HEALTH = 7
    SPEND_TAXES = 8
    SPEND_OTHERS = 9

    STATUS_TRANSACTION_OK = 1  # Транзакция успешно добавлена.
    STATUS_TRANSACTION_ERR = 0  # Добавление транзакции завершено с ошибкой.

    # команды:
    # предусловие: summ != 0, 0 <= category <= 9.
    # постусловие: транзакция успешно добавлена.
    def add_transaction(self, summ: float, category: int, description: str):
        pass

    # предусловие: транзакция существует.
    # постусловие: транзакция успешно изменена.
    def change_transaction(self, summ: float, category: int, description: str):
        pass

    # предусловие: транзакция существует.
    # постусловие: транзакция успешно удалена.
    def delete_transaction(self, summ: float, category: int, description: str):
        pass

    # запросы:
    # предусловие: year > 0, 0 <= month <= 12.
    def get_month_income(self, year: int, month: int):
        pass

    # предусловие: year > 0, 0 <= month <= 12.
    def get_month_spend(self, year: int, month: int):
        pass

    # предусловие: year > 0, 0 <= month <= 12.
    def get_month_balance(self, year: int, month: int):
        pass

    # предусловие: year >= 2022.
    def get_year_statistics(self, year: int):
        pass

    # предусловие: year >= 2022.
    def get_year_most_spend_category(self, year: int):
        pass

    # предусловие: year >= 2022.
    def get_year_income(self, year: int):
        pass

    # предусловие: year >= 2022.
    def get_year_spend(self, year: int):
        pass

    # предусловие: year >= 2022.
    def get_year_balance(self, year: int):
        pass
