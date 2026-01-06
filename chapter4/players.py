'''
Author       : NullEvasion
Date         : 06.01.2026
Last edit	 : 06.01.2026
'''



players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[0:5:3])	# Третий элемент говорит сколько надо пропускать объектов в заданном диапазоне

for player in players[:3]:
	print(player.title())
