from data import yml_loader
from misc.loader import dp

from keyboards.start.start_bot import start_bot
from keyboards.main_menu import info_bot

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Запустить бота"
dp.register_message_handler(start_bot, lambda message: message.text == yml_loader.start_bot_path["start"]["button_bot_run"])

# Кнопка "Информация о боте"
dp.register_message_handler(info_bot, lambda message: message.text == yml_loader.start_bot_path["start"]["button_info"])