from misc.util import json, logging, os
from misc.loader import bot

from data.admin_db import load_admin_data
from keyboards.update.update_func import keyboard_update_bot

# Загрузка списка подписчиков из файла subscribers.json
def load_subscribers():
	# Путь к файлу subscribers.json
	SUBSCRIBERS_FILE_PATH = os.path.join('bin', 'db', 'subscribers.json')

	with open(SUBSCRIBERS_FILE_PATH, 'r') as file:
		subscribers_data = json.load(file)
		return subscribers_data

# Отправка сообщения всем подписчикам, кроме администратора
async def send_message_to_subscribers_except_admin(message_text, sender_id):
    keyboard = keyboard_update_bot()

    # Проверяем, является ли пользователь администратором
    subscribers = load_subscribers()
    admin_data = load_admin_data()
    
    for subscriber_id in subscribers:
        if subscriber_id != sender_id and subscriber_id not in admin_data:
            try:
                await bot.send_message(subscriber_id, message_text, reply_markup=keyboard)
            except Exception as e:
                logging.exception(f"Ошибка отправки сообщения в {subscriber_id}: {e}")