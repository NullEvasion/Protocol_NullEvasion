'''
Author       : NullEvasion
Date         : 09.01.2026
Last edit    : 09.01.2026
'''



'''
4.14. Просмотрите исходное руководство по стилю PEP 8 по адресу https://
python.org/dev/peps/pep-0008/ Пока вы будете пользоваться им относительно редко,
 но просмотреть его будет интересно.
'''



'''
4.15. Анализ кода: выберите три программы, написанные в этой главе, и измените 
каждую в соответствии с рекомендациями PEP 8:
     Используйте четыре пробела для каждого уровня отступов. Настройте текстовый
    редактор так, чтобы он вставлял четыре пробела при каждом нажатии клавиши
    табуляции, если это не было сделано ранее (за инструкциями обращайтесь к 
    приложению Б).
     Используйте менее 80 символов в каждой строке. Настройте редактор так, 
    чтобы он отображал вертикальную черту в позиции 80-го символа.
     Не злоупотребляйте пустыми строками в файлах программ.

'''
print(f"\n---4.15---")

for value in range(1, 5):
    print(value)
for value in range(1, 6):
    print(value)
numbers = list(range(1, 6))
print(numbers)

players = ['\ncharles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

dimensions = (200, 50)
print(f"\n{dimensions[0]}")
print(dimensions[1])
#dimensions[0] = 250
for dimension in dimensions:
    print(dimension)
print("Original dimension:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)