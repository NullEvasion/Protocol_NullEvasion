'''
Author       : NullEvasion
Date         : 13.01.2026
Last edit    : 13.01.2026
'''




answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(f"\n{age < 21}")
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
print(f"\n{age_0 >= 21 and age_1 >= 21}")
age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))

age_0 = 22
age_1 = 18
print(f"\n{age_0 >= 21 or age_1 >= 21}")
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f"\n{'mushrooms' in requested_toppings}")
print('pepperoni' in requested_toppings)
