"""
3. Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""
"""
Любое слово можно передать в байтовом виде. Хотя бы в виде попиксельной картинки.
"""
def try_encoding(ls, code='cp1251'):
    print(f'кодировка {code}')
    for el in ls:
        try:
            bytes(el, code)
            print(f'Слово "{el}" успешно перекодировано в кодировку {code}')
        except UnicodeEncodeError:
            print(f'Слово "{el}" невозможно записать в виде байтовой строки в кодировке {code}')
    print()


LS = ['разработка', 'администрирование', 'protocol', 'standard']

print(try_encoding(LS))
print(try_encoding(LS, code='ascii'))