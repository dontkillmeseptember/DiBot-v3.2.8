from misc.util import json, os

# Функция для создания списка подписщиков
def create_json_file(file_name):
	directory = os.path.join("bin", "db")
	if not os.path.exists(directory):
		os.makedirs(directory)

	file_path = os.path.join(directory, file_name)
	if not os.path.exists(file_path):
		with open(file_path, "w") as file:
			file.write("{}")

create_json_file("admin_data.json")

# Функция для проверки наличия администратора в базе данных
def is_admin_in_data(user_id, admin_data):
	return str(user_id) in admin_data

# Функция для загрузки данных из JSON файла
def load_admin_data():
	file_path = os.path.join("bin", "db", "admin_data.json")

	if os.path.exists(file_path):
		with open(file_path, "r", encoding="utf-8") as file:
			return json.load(file)
	return {}

# Функция для сохранения данных в JSON файл
def save_admin_data(data):
	file_path = os.path.join("bin", "db", "admin_data.json")

	with open(file_path, "w", encoding="utf-8") as file:
		json.dump(data, file, ensure_ascii=False, indent=4)