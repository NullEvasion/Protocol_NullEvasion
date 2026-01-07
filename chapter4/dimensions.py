'''
Author       : NullEvasion
Date         : 07.01.2026
Last edit	 : 07.01.2026
'''



dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250
print("")
for dimension in dimensions:
	print(dimension)
print("")
print("Original dimension:")
for dimension in dimensions:
	print(dimension)
print("")
dimensions=(400,100)
print("Modified dimensions:")
for dimension in dimensions:
	print(dimension)



'''
4.13. Шведский стол: меню "шведского стола" в ресторане состоит всего из пяти пунктов.
Придумайте пять простых блюд и сохраните их в кортеже.
	 Используйте цикл for для вывода всех блюд, предлагаемых рестораном.
	 Попробуйте изменить один из элементов и убедитесь в том, что Python отказывается
	вносить изменения.
	 Ресторан изменяет меню, заменяя два элемента другими блюдами. Добавьте блок
	кода, который заменяет кортеж, и используйте цикл for для вывода каждого элемента
	обновлённого меню.
'''
print(f"\n---4.13---")
foods=('pelmeni','byteri','tortiki','burgers','katletki')
print(f"-Официант: Сегодня у нас в меню:")
for food in foods:
	print(food.title())
print(f"\n-Клиент: Закажу ка я ... БУРГЕРЫ! Они мне дороже РОДИНЫ! ")
print(f"\n*за столом напротив сидит подозрительная фигура с бордовыми волосами в тёмно-бордовом пальто*")
print(f"\n-Неизвестный: Дороже Родины? Ну-ну ... Посмотрим как ты затявкаешь, когда надкусишь бургер своим поганым ртом ...")
print(f"\n-Клиент: Это что угроза? Ты что о себе возомнил? Сиди и ешь свой салат из улиток!")
print(f"\n*Клиент задумался: 'Зря я на него наехал, похоже это обладатель СТЕНДА!'*")
print(f"\n-Неизвестный: Что ты там вякаешь, сопляк? Ты знаешь кто я? \n\tMETALLIKA!")
print(f"\n*Чтобы узнать что было дальше, надо задонатить 10 долларов на носки разработчику*")

#foods[1]='bukli'
#print(foods)
print("")
bluda=('pelmeni','byteri','kolbasa','burgers','makaroni')
for bludo in bluda:
	print(bludo)