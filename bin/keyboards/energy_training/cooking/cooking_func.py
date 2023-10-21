from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, WebAppInfo
from misc.loader import bot

from data import yml_loader
from data.config import FORTUNEWHEEL

# Обработчик вкладки "Кулинарная лихорадка"
async def cooking_handler(message: types.Message):
    # Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	keyboard.add(KeyboardButton(f"{yml_loader.ration_data['ration']['button_ration']}{yml_loader.ration_data['ration']['name_ration']}"))
	keyboard.add(KeyboardButton(yml_loader.casino_path["casino"]["button_casino"], web_app=WebAppInfo(url=FORTUNEWHEEL)))
	keyboard.add(KeyboardButton(yml_loader.energy_training_data["button_energy_training"]), KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

	await bot.send_message(message.chat.id, yml_loader.cooking_data["cooking"]["cooking_info"], reply_markup=keyboard)