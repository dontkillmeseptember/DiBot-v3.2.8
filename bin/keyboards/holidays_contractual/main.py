from misc.util import ReplyKeyboardMarkup, KeyboardButton, types
from misc.loader import bot

from data import yml_loader
from data.start_db import load_user_data, is_user_in_data

def keyboard_igor():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.calendar_path["calendar"]["button_calendar"]), 
		KeyboardButton(yml_loader.fines_data["fines"]["button_fines"])
	)
	keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"])
	)

	return keyboard

def keyboard_dinara():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.calendar_path["calendar"]["button_calendar"]), 
		KeyboardButton(yml_loader.fines_data["fines"]["button_fines"])
	)
	keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]),
		KeyboardButton(yml_loader.contract_slava_path["contract_slava"]["button_contract_slava"])
	)

	return keyboard

def keyboard_admin():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.calendar_path["calendar"]["button_calendar"]), 
		KeyboardButton(yml_loader.fines_data["fines"]["button_fines"])
	)
	keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]),
		KeyboardButton(yml_loader.contract_slava_path["contract_slava"]["button_contract_slava"])
	)

	return keyboard

def keyboard_user():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.calendar_path["calendar"]["button_calendar"]), 
		KeyboardButton(yml_loader.fines_data["fines"]["button_fines"])
	)
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"])
	)

	return keyboard

# Обработчик "Праздники и договор"
async def holidays_contractual_menu_handler(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже соотвествующая роль
		if str(user_id) in user_data and "role" in user_data[str(user_id)]:
			selected_role = user_data[str(user_id)]["role"]

			if selected_role == yml_loader.role_path["roles"]["role_igor"]:
				keyboard = keyboard_igor()
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_path["holidays_contractual_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.role_path["roles"]["role_dinara"]:
				keyboard = keyboard_dinara()
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_path["holidays_contractual_slava_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.admin_path["admin"]["admin_role"]:
				keyboard = keyboard_admin()
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_path["holidays_contractual_slava_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.start_bot_path["registor"]["user_role"]:
				keyboard = keyboard_user()
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_path["holidays_contractual_info"], reply_markup=keyboard)
	else:
		print("User not registor.")

async def holidays_contractual_handler(message: types.Message):
	await holidays_contractual_menu_handler(message)