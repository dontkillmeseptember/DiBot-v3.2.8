from misc.util import ReplyKeyboardMarkup, KeyboardButton, types
from misc.loader import bot

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data

# Обработчик "Праздники и договор"
async def holidays_contractual_menu_handler(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Создаем клавиатуру с вкладками
		keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(KeyboardButton(yml_loader.contract_slava_path["contract_slava"]["button_contract_slava"]))
		keyboard.add(KeyboardButton(yml_loader.calendar_path["calendar"]["button_calendar"]), KeyboardButton(yml_loader.fines_data["fines"]["button_fines"]))
		keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
		keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

		await bot.send_message(message.chat.id, yml_loader.holidays_contractual_path["holidays_contractual_slava_info"], reply_markup=keyboard)
	else:
		# Создаем клавиатуру с вкладками
		keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(KeyboardButton(yml_loader.calendar_path["calendar"]["button_calendar"]), KeyboardButton(yml_loader.fines_data["fines"]["button_fines"]))
		keyboard.add(KeyboardButton(yml_loader.contract_path["contract"]["button_contract"]))
		keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

		await bot.send_message(message.chat.id, yml_loader.holidays_contractual_path["holidays_contractual_info"], reply_markup=keyboard)

async def holidays_contractual_handler(message: types.Message):
	await holidays_contractual_menu_handler(message)