'''
Author       : NullEvasion
Date         : 15.01.2026
Last edit    : 15.01.2026
'''



'''
5.2. Больше условий: количество условий не ограничивается десятью. Попробуйте 
написать другие условия и включить их в conditional_tests.py. Программа должна 
выдавать по крайней мере один истинный и один ложный результат для следующих 
видов проверок:
      Проверка равенства и неравенства строк
      Проверки с использованием функции lower()
      Числовые проверки равенства и неравенства, условий "больше", "меньше", 
     "больше или равно", "меньше или равно".
      Проверки с ключевым словом and и or.
      Проверка вхождения элемента в список.
      Проверка отсутствия элемента в списке.
'''
print(f"\n---5.2---")

age = 18
print(age != 18)
print(f"{age != 71}\n")

boobs = 'Третий'
print('Третий' in boobs.lower())
print(f"{boobs.lower() == 'третий'}\n")

trees = 29
print(trees > 29)
print(trees < 30)
print(trees <= 17)
print(trees >= 22)
print(f"{trees != 29}\n")

chest_1 = 12
chest_2 = 24
print(chest_1 >= 12 and chest_2 <= 24)
print(chest_1 > 13 and chest_2 < 141)
print(chest_1 < 7 or chest_2 != 5)
print(f"{chest_1 >= 16 or chest_2 <= 23}\n")

spisok = ['white', 'blue', 'red']
print('blue' in spisok)
print(f"{'purple' in spisok}\n")

color = 'green'
if color not in spisok:
      print(f"{color.title()} нету в списке!")
color = 'teal'
if color in spisok:
      print(f"{color.title()} есть в списке! Победа!")
else:
      print(f"О нееет! {color.title()} отсутствует в списке!")