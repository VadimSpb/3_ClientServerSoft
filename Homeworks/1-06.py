"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect

LS = ['сетевое программирование', 'сокет', 'декоратор']

with open('test.txt', 'w') as file:
    for line in LS:
        file.write(f'{line}\n')
file.close()

with open('test.txt', 'rb') as file:
    CONTENT = file.read()
ENCODING = detect(CONTENT)['encoding']
print('кодировка: ', ENCODING, end='\n\n')
print('Текст:')
with open('test.txt', 'r', encoding=ENCODING) as file:
    CONTENT = file.read()
print(CONTENT)