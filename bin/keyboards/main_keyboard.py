from data import yml_loader
from misc.loader import dp

from keyboards.main_menu import main_menu

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Главное меню"
dp.register_message_handler(main_menu, lambda message: message.text == yml_loader.main_path["main_menu"]["button_main_menu"])