from misc.util import ReplyKeyboardMarkup, KeyboardButton, types
from misc.loader import bot

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data

# Обработчик "Энергия и тренировки"
async def energy_training_menu_handler(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Создаем клавиатуру с вкладками
		keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(KeyboardButton(yml_loader.news_life_path["news_life"]["button_news_life"]))
		keyboard.add(KeyboardButton(yml_loader.cooking_data["cooking"]["button_cooking"]), KeyboardButton(yml_loader.sport_data["sport"]["button_sport"]))
		keyboard.add(KeyboardButton(yml_loader.news_path["news"]["button_news"]))
		keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

		await bot.send_message(message.chat.id, yml_loader.energy_training_data["energy_training_info"], reply_markup=keyboard)
	else:
		# Создаем клавиатуру с вкладками
		keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(KeyboardButton(yml_loader.cooking_data["cooking"]["button_cooking"]), KeyboardButton(yml_loader.sport_data["sport"]["button_sport"]))
		keyboard.add(KeyboardButton(yml_loader.news_path["news"]["button_news"]))
		keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

		await bot.send_message(message.chat.id, yml_loader.energy_training_data["energy_training_info"], reply_markup=keyboard)

async def energy_training_handler(message: types.Message):
	await energy_training_menu_handler(message)