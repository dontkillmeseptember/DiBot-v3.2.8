from misc.util import ReplyKeyboardMarkup, KeyboardButton, types
from misc.loader import bot

from data import yml_loader
from data.start_db import load_user_data, is_user_in_data

def keyboard_igor():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(KeyboardButton(yml_loader.cooking_data["cooking"]["button_cooking"]), KeyboardButton(yml_loader.sport_data["sport"]["button_sport"]))
	keyboard.add(KeyboardButton(yml_loader.news_path["news"]["button_news"]))
	keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

	return keyboard

def keyboard_dinara():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(KeyboardButton(yml_loader.cooking_data["cooking"]["button_cooking"]), KeyboardButton(yml_loader.sport_data["sport"]["button_sport"]))
	keyboard.add(KeyboardButton(yml_loader.news_igor_path["news_igor"]["button_news_igor"]))
	keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

	return keyboard

def keyboard_admin():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(KeyboardButton(yml_loader.cooking_data["cooking"]["button_cooking"]), KeyboardButton(yml_loader.sport_data["sport"]["button_sport"]))
	keyboard.row(
		KeyboardButton(yml_loader.news_path["news"]["button_news"]),
		KeyboardButton(yml_loader.news_life_path["news_life"]["button_news_life"]),
		KeyboardButton(yml_loader.news_igor_path["news_igor"]["button_news_igor"])
	)
	keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

	return keyboard

def keyboard_user():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(KeyboardButton(yml_loader.cooking_data["cooking"]["button_cooking"]), KeyboardButton(yml_loader.sport_data["sport"]["button_sport"]))
	keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

	return keyboard

# Обработчик "Энергия и тренировки"
async def energy_training_menu_handler(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже соотвествующая роль
		if str(user_id) in user_data and "role" in user_data[str(user_id)]:
			selected_role = user_data[str(user_id)]["role"]

			if selected_role == yml_loader.role_path["roles"]["role_igor"]:
				keyboard = keyboard_igor()
				await bot.send_message(message.chat.id, yml_loader.energy_training_data["energy_training_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.role_path["roles"]["role_dinara"]:
				keyboard = keyboard_dinara()
				await bot.send_message(message.chat.id, yml_loader.energy_training_data["energy_training_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.admin_path["admin"]["admin_role"]:
				keyboard = keyboard_admin()
				await bot.send_message(message.chat.id, yml_loader.energy_training_data["energy_training_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.start_bot_path["registor"]["user_role"]:
				keyboard = keyboard_user()
				await bot.send_message(message.chat.id, yml_loader.energy_training_data["energy_training_info"], reply_markup=keyboard)
	else:
		print("User not registor.")

async def energy_training_handler(message: types.Message):
	await energy_training_menu_handler(message)