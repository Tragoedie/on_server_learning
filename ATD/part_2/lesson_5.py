# В python поддерживаются все 5 принципов повторного использования кода
# 1) Обобщённые типы (generic types) реализуются при помощи модуля typing, например:
from typing import Sequence, TypeVar

T = TypeVar('T')  # Declare type variable


def first(l: Sequence[T]) -> T:  # Generic function
    return l[0]
# 2), 3) Данные принципы реализуется при помощи import/from ... import ... .
from proj1.formatters.formatter_json import formatter_json
from proj1.formatters.formatter_xml import formatter_xml
from proj1.formatters.formatter_csv import formatter_csv
from proj1.parser_file import parse_file

def generate(file_path1, file_path2, formatter_name):
    content_one = parse_file(file_path1)
    content_two = parse_file(file_path2)
    return _select_formatter(formatter_name)(
        format_(content_one, content_two),
    )

def format_(first_dict, second_dict):
    # Some actions
    pass

def _select_formatter(formatter_name):
    formatters = {
        'json': formatter_json,
        'xml': formatter_xml,
        'csv': formatter_csv,
    }
    return formatters[formatter_name]

# 4) Принцип достигается путём перегрузки (overload), исключением является перегрузка методов с одинаковым числом
# параметров, т.к. пусть Python и строго-типизированный язык, но при этом типизация динамическая, в отличие от,
# например, C++, где типизация статическая. Задание типов через :, например x: int ровным счётом ни на что не влияет,
# т.к. данный функционал носит рекомендательный характер для других программистов.

class test:
    def func(self, x: int, y: int) -> int:
        return x * y

    def func(self, x: str, y: str) -> str:
        return x + y
# Выполняться будет всегда последняя реализация, вне записимости от типов передаваемых параметров.

# 5)
# engine.py
import game1
import game2

def start(game_name):
    if game_name == 'calc':
        engine(game1)
    elif game_name == 'paint':
        engine(game2)

def engine(game_pack):
  game_pack.print_name()
  game_pack.game()
  game_pack.exit()

# game1.py
class game1:
    def print_name(self):
        # Some actions
        pass
    def game(self):
        # Some actions
        pass
    def exit(self):
        # Some actions
        pass

# game2.py
class game2:
    def print_name(self):
        # Some actions
        pass
    def game(self):
        # Some actions
        pass
    def exit(self):
        # Some actions
        pass