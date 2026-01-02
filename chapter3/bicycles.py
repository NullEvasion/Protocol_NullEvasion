'''
Author       : NullEvasion
Date         : 02.01.2026
'''



bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

print(bicycles[0].title())

print(bicycles[1]) # Индексы начинаются с 0, а не с 1, поэтому 1 будет cannondale (а не trek)
print(bicycles[3])

print(bicycles[-1]) # С конца отсчёт индексов начинается не с 0, а с -1.

message=f"My first bicycle was a {bicycles[0].title()}."
print(message)



'''
3.1. Имена: сохраните имена нескольких своих друзей в списке с именем names. Выведите
имя каждого друга, обратившись к каждому элементу списка (по одному за раз).
'''
print("")
names=['michelle','brevnovka']
print(names[-1].title())
print(names[0].title())



'''
3.2 Сообщения: начните со списка, использованного в упражнении 3.1, но вместо вывода
имени каждого человека выведите сообщение. Основной текст для всех сообщений должен 
быть одинаковым, но каждое сообщение должнол включать имя адресата.
'''
print("")
names=['michelle','brevnovka']
print(f"Hello {names[0].title()}, how are you? Are you tired of working in Turtle Bay?")
print(f"Sup {names[-1].title()}! What's poppin' in Rome?")



'''
3.3. Собственный список: выберите свой любимый вид транспорта (например, мотоциклы
или машины) и создайте список с примерами. Используйте свой список для вывода
утверждений об элементах типа: "Я хотел бы купить мотоцикл Honda"
'''
print("")
transport=['Т-90М «Прорыв»','Ка-52 «Аллигатор»','Хромая блоха']
print(f"Хотел бы заехать в цирк на - {transport[-3]}")
print(f"Какой классный вертолёт - {transport[1]}. Думаю отличная идея - пролететь в нём, на низкой высоте, над центром города!")
print(f"Да тебя и {transport[-1].lower()} обгонит!")