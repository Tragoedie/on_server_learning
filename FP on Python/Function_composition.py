"""
3.1. Напишите функцию частичного применения tag(), которая получает на вход два строковых параметра:
название HTML-тега, и значение. Эта функция оборачивает значение тегом с
учётом открывающего и закрывающего тега, например:
tag('b', 'string') # <b>string</b>
На основе tag подготовьте две функции bold и italic, которые оборачивают значение в теги b и i.

3.2. Расширьте функцию tag третьим параметром attr (тип словарь),
который добавляет к тегу набор свойств (их может быть несколько).

Например:
tag('li', {'class': 'list-group'}, 'item 23')
Результатом будет
<li class="list-group">item 23</li>
"""

from pymonad import curry
from pymonad import *


def tag(name, content):
    return "<{0}>{1}</{2}>".format(name, content, name)


@curry
def bold(content):
    return tag('b', content)


@curry
def italic(content):
    return tag('i', content)


bold_and_italic = bold * italic


def tag_ext(name, content, attributes: dict):
    attributes_string = ""
    for attribute, value in attributes.items():
        attributes_string += " {0}=\"{1}\"".format(attribute, value)
    return "<{0}{1}>{2}</{3}>".format(name, attributes_string, content, name)


print(tag('h1', 'Здесь будет ваш заголовок'))
print(bold('Жирный текст'))
print(italic('Текст курсив'))
print(bold_and_italic('Текст жирный и курсив'))

print(tag_ext('li', 'item 23', {'class': 'list-group', 'href': 'www'}))

