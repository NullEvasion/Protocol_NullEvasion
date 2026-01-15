'''
Author       : NullEvasion
Date         : 13.01.2026
Last edit    : 15.01.2026
'''




'''
5.1. Проверка условий: напишите последовательности условий. Выведите описание 
каждой проверки и ваш прогноз относительно её результата. Код должен выглядеть 
примерно так:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
     Внимательно просмотрите результаты. Убедидесь в том, что вы понимаете, 
    почему результат каждой строки равен True или False.
     Создайте как минимум 10 условий. Не менее пяти одних должны давать 
    результат True, а не менее пяти других - результат False.
'''
print(f"\n---5.1---")
pizzas = ['pepperoni', 'makaroni', 'fusilioni', 'mafiozoni', 'properdone']
print("Количество pizzas == '5'? Думаю True.")
print(len(pizzas) == 5)

print("\nЕсть ли тут pizzas == 'properdone'? Думаю это True.")
print('properdone' in pizzas)

print("\nЕсть ли тут pizzas == 'kakolini'? Думаю False.")
print('kakolini' in pizzas)

pizzas = 'makaroni'
print("\nСтрока состоит из pizzas == 'makaroni'? Думаю True.")
print(pizzas == 'makaroni')

pizzas = 'makaroni', 'pepperoni'
print("\nА теперь строка pizzas == 'makaroni', 'pepperoni'? Думаю True.")
print(pizzas == ('makaroni', 'pepperoni'))

audio = 'bm800', 'behringer umc22', 'easy effects'
print("\nМикрофон у меня audio == BM800? Наверное False.")
print('bm801' in audio)

print("\nНаверное приложение для аудио audio == adobe audition? Думаю False.")
print(audio == 'adobe audition')

age = 17
print("\nИнтересно, ей больше age == 17? Думаю False")
print(age > 18)

print("\nМожет ей просто age == 16? Думаю False")
print(age <= 16)

print("\nОй ну это просто отлично, всё таки ей age == 17? Вероятно True")
print(age == 17)