from misc.util import os, json

# Функция для создания списка зарегистрированных пользователей
def create_json_file(file_name):
	directory = os.path.join("bin", "db")
	if not os.path.exists(directory):
		os.makedirs(directory)

	file_path = os.path.join(directory, file_name)
	if not os.path.exists(file_path):
		with open(file_path, "w") as file:
			file.write("{}")

create_json_file("basket_data.json")

# Функция для проверки наличия пользователя в базе данных
def is_basket_in_data(user_id, user_data):
	return str(user_id) in user_data

# Функция для загрузки данных из JSON файла
def load_basket_data():
	user_path = os.path.join("bin", "db", "basket_data.json")

	if os.path.exists(user_path):
		with open(user_path, "r", encoding="utf-8") as file:
			return json.load(file)
	return {}

def check_basket_data(user_id):
    user_path = os.path.join("bin", "db", "basket_data.json")

    if os.path.exists(user_path):
        with open(user_path, "r", encoding="utf-8") as file:
            user_data = json.load(file)
            return user_data.get(str(user_id), {})
    return {}

# Функция для сохранения данных в JSON файл
def save_basket_data(data):
	user_path = os.path.join("bin", "db", "basket_data.json")

	with open(user_path, "w", encoding="utf-8") as file:
		json.dump(data, file, ensure_ascii=False, indent=4)