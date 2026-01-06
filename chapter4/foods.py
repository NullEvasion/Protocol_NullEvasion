'''
Author       : NullEvasion
Date         : 06.01.2026
Last edit	 : 06.01.2026
'''



my_foods=['pizza','falafel','carrot cake']
friends_foods=my_foods[:]
#friends_foods=my_foods

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)



'''
4.10. Сегменты: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
который делает следующее:
	 Выводит сообщение "The first three items in the list are:", а затем использует сегмент
	для вывода первых трёх элементов из списка.
	 Выводит сообщение "Three items from the middle of the list are:", а затем использует сегмент
	для вывода первых трёх элементов из середины списка.
	 Выводит сообщение "The last three items in the list are:", а затем использует сегмент
	для вывода последних трёх элементов из списка.
'''
print(f"\n---4.10---")
players=['charles','martina','michael','florence','eli']
print(f"The first three items in the list are:{players[:3]}")
print(f"Three items from the middle of the list are:{players[2:5]}")
print(f"The last three items in the list are:{players[-3:]}")



'''
4.11. Моя пицца, твоя пицца: начните с программы из упражнения 4.1. Создайте копию
списка с видами пиццы, присвойте ему имя friends_pizzas. Затем сделайте следующее:
	 Добавьте новую пиццу в исходный список.
	 Добавьте другую пиццу в список friend_pizzas.
	 Докажите, что в программе существуют два разных списка. Выведите сообщение
	"My favorite pizzas are:", а затем первый список в цикле for. Выведите сообщение
	"My friend's favorite pizzas are:", а затем второй список в цикле for. Убедитесь в том,
	что каждая новая пицца находится в соответствующем списке.
'''
print(f"\n---4.11---")
my_pizzas=['pineapple', 'pepperoni', 'domashnyaya']
friend_pizzas=my_pizzas[:]

my_pizzas.append('myasonioni')
friend_pizzas.append('carbonara')

print(f"My favorite pizzas are:")
for pizza in my_pizzas:
	print(f"\t{pizza.title()}")

print("")

print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(f"\t{pizza.title()}")



'''
4.12. Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования
цикла for при выводе для экономии места. Выберите версию foods.py и напишите два цикла
for для вывода каждого списка.
'''
print(f"\n---4.12---")
my_foods2=['pizza','falafel','carrot cake']
friends_foods2=my_foods[:]

my_foods2.append('cannoli')
friends_foods2.append('ice cream')

print("My favorite foods are:")
for foods in my_foods2:
	print(foods.upper())

print("\nMy friend's favorite foods are:")
for foods2 in friends_foods:
	print(foods2.upper())