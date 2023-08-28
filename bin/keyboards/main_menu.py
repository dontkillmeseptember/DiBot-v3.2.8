from misc.util import ReplyKeyboardMarkup, KeyboardButton, types
from misc.loader import bot

from data import yml_loader

# Создание клавитуры для меню
def create_menu_keyboard():
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	keyboard.add(KeyboardButton(yml_loader.energy_training_data["button_energy_training"]), KeyboardButton(yml_loader.holidays_contractual_path["button_holidays_contractual"]))
	keyboard.add(KeyboardButton(yml_loader.quest_data["quest"]["button_quest"]))
	keyboard.add(KeyboardButton(yml_loader.version_data["version"]["button_update"]), KeyboardButton(yml_loader.start_bot_path["start"]["button_info"]))

	return keyboard

async def info_bot(message: types.Message):
	await bot.send_message(message.chat.id, yml_loader.start_bot_path["start"]["base_info"])

# Обработчик "Главное меню"
async def main_menu(message: types.Message):
	keyboard = create_menu_keyboard()
	
	await bot.send_message(message.chat.id, yml_loader.main_path["main_menu"]["main_menu_info"], reply_markup=keyboard)