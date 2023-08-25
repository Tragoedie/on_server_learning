import pymonad.tools

'''2.3.1. Напишите каррированную функцию с двумя строковыми параметрами, которая вычисляет их сцепленное значение. 
Создайте на её основе функцию, которая получает один параметр и возвращает
Hello, значение-параметра
Это требуется, чтобы можно было выводить стандартное приветствие, задавая только имя.'''


@pymonad.tools.curry(2)
def concat(greeting, name):
    return greeting + name


# 1.
def greet_1(name):
    return concat('Hello, ', name)


print(type(greet_1).__name__)
print(greet_1('Petya_1'))

# 2.
greet_2 = concat('Hello, ')
print(type(greet_2).__name__)
print(greet_2('Petya_2'))


# 3.
def concat(greeting):
    def greet_3(name):
        return greeting + name

    return greet_3


greet_3 = concat('Hello, ')
print(type(greet_3).__name__)
print(greet_3('Petya_3'))

'''2.3.2. Придумайте функцию, которая получает на вход четыре аргумента: слово привествия, 
знак препинания за ним, имя приветствуемого, и заключительный знак.

Как сделать так, чтобы вариант её частичного применения получал бы в качестве единственного параметра только имя, 
а все остальные параметры настраивались бы другим вызовом?'''


# 1.
@pymonad.tools.curry(4)
def print_greeting(greet_word, separator, last_sign, name):
    return '{0}{1} {2}{3}'.format(greet_word, separator, name, last_sign)


# 2.1

def greet_4(name):
    return print_greeting("Hello")(",")("!")(name)


print(type(greet_4).__name__)
print(greet_4('Petya_4'))

# 2.2

greet_5 = print_greeting("Hello")(",")("!")
print(type(greet_5).__name__)
print(greet_5("Petya_5"))


# 2.3
def greet_deeply_curried(greeting, separator, last_sign):
    def with_name(name):
        return greeting + separator + name + last_sign

    return with_name


greet_6 = greet_deeply_curried("Hello", ", ", "!")
print(type(greet_6).__name__)
print(greet_6('Petya_6'))
