'''
Author       : NullEvasion
Date         : 29.12.2025
'''



import os
import shutil
import time
import subprocess

WATCH_DIR="/home/super/Загрузки/torrent"
DEST_DIR="/media/super/DATA/download"
CHECK_INTERVAL=30

def is_file_busy(filepath):
	try:
		subprocess.check_output(['lsof', filepath])
		return True
	except subprocess.CalledProcessError:
		return False

print(f"--- Сортировщик Аски запущен! Слежу за {WATCH_DIR} ---")

while True:
	if not os.path.exists(WATCH_DIR):
			os.makedirs(WATCH_DIR)

	if os.path.exists(DEST_DIR):
		for item in os.listdir(WATCH_DIR):
			full_path = os.path.join(WATCH_DIR, item)

			if os.path.isdir(full_path):
				continue

			if not is_file_busy(full_path):
				print(f"Нашла готовый объект: {item}. Начинаю переброску...")
				try:
					shutil.move(full_path, os.path.join(DEST_DIR, item))
					print(f"Успешно! {item} теперь на SSD.")
				except Exception as e:
					print(f"Ошибка при переносе: {e}")
			else:
				print(f"Файл {item} ещё занят системой, жду...")
	else:
		print("Папка назначения недоступна")

	time.sleep(CHECK_INTERVAL)