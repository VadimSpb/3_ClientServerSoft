"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов
не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

LS = [b'class', b'function', b'method']
[print(el, type(el), len(el)) for el in LS]

