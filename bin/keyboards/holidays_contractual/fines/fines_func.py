from misc.util import ReplyKeyboardMarkup, KeyboardButton, types
from misc.loader import bot

from data import yml_loader

# Вкладка выбора штрафов
async def fines_handler(message: types.Message):
    # Создаем клавиатуру с вкладками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton(yml_loader.fines_data["fines_igor"]["button_fines_igor"]))
    keyboard.add(KeyboardButton(yml_loader.fines_data["fines_slava"]["button_fines_slava"]))
    keyboard.add(KeyboardButton(yml_loader.holidays_contractual_path["button_holidays_contractual"]), KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

    await bot.send_message(message.chat.id, yml_loader.fines_data["fines"]["fines_info"], reply_markup=keyboard)

# Обработчик выбора вкладки "Штрафы Игоря"
async def fines_igor_handler(message: types.Message):
    # Создаем клавиатуру с вкладками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton(yml_loader.fines_data["fines_slava"]["button_fines_slava"]))
    keyboard.add(KeyboardButton(yml_loader.holidays_contractual_path["button_holidays_contractual"]), KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

    await bot.send_message(message.chat.id, yml_loader.fines_data["fines_igor"]["fines_menu_igor"], reply_markup=keyboard)

# Обработчик выбора вкладки "Штрафы Вячеслава"
async def fines_slava_handler(message: types.Message):
    # Создаем клавиатуру с вкладками
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(KeyboardButton(yml_loader.fines_data["fines_igor"]["button_fines_igor"]))
    keyboard.add(KeyboardButton(yml_loader.holidays_contractual_path["button_holidays_contractual"]), KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

    await bot.send_message(message.chat.id, yml_loader.fines_data["fines_slava"]["fines_menu_slava"], reply_markup=keyboard)