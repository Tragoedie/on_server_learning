from Word_Excel.word_function import find_and_replace

document = input("Введите название документа: ")
# poisk_i_zamena.docx
find_line = input("Введите искомую строку: ")
# Но воды поблизости нет
replace_line = input("Введите заменяемую строку: ")
# Да есть там вода

find_and_replace(document, find_line, replace_line)

