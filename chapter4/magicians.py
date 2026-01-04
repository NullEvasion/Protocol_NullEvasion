'''
Author       : NullEvasion
Date         : 04.01.2026
'''



magicians=['alice','david','carolina']
for magician in magicians:
#print(magician)	Попытка запустить программу без отступа в цикле for
	print(f"{magician.title()}, that was a great trick!")
#print(f"I can't wait to see your next trick, {magician.title()}.\n")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")



'''
4.1. Пицца: вспомните по крайней мере три названия ваших любимых видов пиццы.
Сохраните их в списке и используйте цикл for для вывода всех названий.
	 Измените цикл for так, чтобы вместо простого названия пиццы выводилось
	сообщение, включающее это название. Таким образом для каждого элемента должна
	выводиться строка с простым текстом, например: "I like pepperoni pizza".
	 Добавьте в конец программы (после цикла for) строку с завершающим сообщением.
	Таким образом, вывод должен состоять из трёх (и более) строк с названиями пиццы
	и дополнительного сообщения - скажем, "I really love pizza!".
'''
pizzas=[]
pizzas.append('domashnyaya')
pizzas.insert(-1, 'pepperoni')
pizzas.insert(0, 'pineapple')
for pizza in pizzas:
	print(f"Yo, i like {pizza.title()} pizza, HUH!")
print(f"Hey, Mr. White, i really love this {len(pizzas)} pizzas on your roof!")



'''
4.2. Животные: создайте списков из трёх (и более) животных, обладающих общей характеристикой.
Используйте цикл for для вывода названий всех животных.
	 Измените программу так, чтобы вместо простого названия выводилось сообщение,
	включающее это название, - например, "A dog would make a great pet".
	 Добавьте в конец программы строку с описанием общего свойства. Например, можно
	вывести сообщение "Any of these animals would make a great pet!".
'''
print("")
pets=[]
pets.append('Мозазавр')
pets.append('Плезиозавр')
pets.insert(-1, 'Ихтиозавр')
pets.append('Мегалодон')
for pet in pets:
	print(f"I think {pet}, would be a great pet fish.")
print(f"I think every one of these fish would make a flex in my aquarium.")
