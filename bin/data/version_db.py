from misc.util import os, json

# Функция для загрузки данных из JSON файла
def load_version_data():
	version_path = os.path.join("bin", "db", "version_data.json")

	if os.path.exists(version_path):
		with open(version_path, "r", encoding="utf-8") as file:
			return json.load(file)
	return {}

def get_bot_version():
    version_data = load_version_data()
    version_bot = version_data.get("version_bot", {}).get("version", "")
    return version_bot