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

create_json_file("subscribers.json")

# Функция для проверки подписки
def is_subscribed(user_id):
    subscribers_data = get_all_subscribers()
    return str(user_id) in subscribers_data

# Функция для проверки статуса has_visited_ration у пользователя
def check_has_visited_ration(user_id):
    subscribers_data = get_all_subscribers()
    return subscribers_data.get(str(user_id), {}).get("has_visited_ration", False)

# Функция для получения списка подписчиков из JSON файла
def get_all_subscribers():
    file_path = os.path.join("bin", "db", "subscribers.json")
    
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file:
            subscribers_data = json.load(file)
        return subscribers_data
    else:
        return {}

# Функция для сохранения подписчиков в JSON файл
def save_subscriber(user_id, username):
    subscribers_data = get_all_subscribers()
    if user_id not in subscribers_data:
        subscribers_data[user_id] = {
            "username": username,
            "has_visited_ration": False,
            "is_subscribed": True
        }
        file_path = os.path.join("bin", "db", "subscribers.json")
        with open(file_path, "w") as file:
            json.dump(subscribers_data, file, indent=4)

# Функция для удаления подписчика из JSON файла
def delete_subscriber(user_id):
    subscribers_data = get_all_subscribers()
    if str(user_id) in subscribers_data:
        del subscribers_data[str(user_id)]
        file_path = os.path.join("bin", "db", "subscribers.json")
        with open(file_path, "w") as file:
            json.dump(subscribers_data, file, indent=4)

# Функция для установки ежедневного сброса флага has_visited_sport
async def daily_reset_has_visited_sport():
	file_path = os.path.join("bin", "db", "subscribers.json")
	
	with open(file_path, "r") as file:
		subscribers_data = json.load(file)
	
	for user_id, user_data in subscribers_data.items():
		user_data["has_visited_sport"] = False
	
	with open(file_path, "w") as file:
		json.dump(subscribers_data, file, indent=4)