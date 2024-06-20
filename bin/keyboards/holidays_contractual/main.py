from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, datetime
from misc.loader import bot

from data import yml_loader
from data.start_db import load_user_data, is_user_in_data
from data.eth_db import calculate_interest

from data.base_glossary import get_russian_month

def keyboard_igor(message: types.Message):
	# Получаем текущую дату и форматируем её
	current_date = datetime.datetime.now()
	russian_month = get_russian_month(current_date.month)

	formatted_date = f"{current_date.day} {russian_month}"

	# Получаем сумму платежа
	interest_summ = calculate_interest(message)
	formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(f"📁📅 Календарь • {formatted_date}"), 
		KeyboardButton(f"📁💳 RedSlavBank • {formatted_interest_summ} ₽")
	)
	keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"])
	)

	return keyboard

def keyboard_dinara(message: types.Message):
	# Получаем текущую дату и форматируем её
	current_date = datetime.datetime.now()
	russian_month = get_russian_month(current_date.month)

	formatted_date = f"{current_date.day} {russian_month}"

	# Получаем сумму платежа
	interest_summ = calculate_interest(message)
	formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(f"📁📅 Календарь • {formatted_date}"), 
		KeyboardButton(f"📁💳 RedSlavBank • {formatted_interest_summ} ₽")
	)
	keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]),
		KeyboardButton(yml_loader.contract_slava_path["contract_slava"]["button_contract_slava"])
	)

	return keyboard

def keyboard_admin(message: types.Message):
	# Получаем текущую дату и форматируем её
	current_date = datetime.datetime.now()
	russian_month = get_russian_month(current_date.month)

	formatted_date = f"{current_date.day} {russian_month}"

	# Получаем сумму платежа
	interest_summ = calculate_interest(message)
	formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(f"📁📅 Календарь • {formatted_date}"), 
		KeyboardButton(f"📁💳 RedSlavBank • {formatted_interest_summ} ₽")
	)
	keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]),
		KeyboardButton(yml_loader.contract_slava_path["contract_slava"]["button_contract_slava"])
	)

	return keyboard

def keyboard_user(message: types.Message):
	# Получаем текущую дату и форматируем её
	current_date = datetime.datetime.now()
	russian_month = get_russian_month(current_date.month)

	formatted_date = f"{current_date.day} {russian_month}"

	# Получаем сумму платежа
	interest_summ = calculate_interest(message)
	formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(f"📁📅 Календарь • {formatted_date}"), 
		KeyboardButton(f"📁💳 RedSlavBank • {formatted_interest_summ} ₽")
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
				keyboard = keyboard_igor(message)
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_data["holidays_contractual_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.role_path["roles"]["role_dinara"]:
				keyboard = keyboard_dinara(message)
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_data["holidays_contractual_slava_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.admin_path["admin"]["admin_role"]:
				keyboard = keyboard_admin(message)
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_data["holidays_contractual_slava_info"], reply_markup=keyboard)
			elif selected_role == yml_loader.start_bot_path["registor"]["user_role"]:
				keyboard = keyboard_user(message)
				await bot.send_message(message.chat.id, yml_loader.holidays_contractual_data["holidays_contractual_info"], reply_markup=keyboard)
	else:
		print("User not registor.")

async def holidays_contractual_handler(message: types.Message):
	await holidays_contractual_menu_handler(message)