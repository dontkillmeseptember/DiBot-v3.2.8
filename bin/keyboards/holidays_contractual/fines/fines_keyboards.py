from data import yml_loader
from misc.loader import dp

from keyboards.holidays_contractual.fines.fines_func import fines_igor_handler, fines_slava_handler

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Штрафы Игоря"
dp.register_message_handler(fines_igor_handler, lambda message: message.text == yml_loader.fines_data["fines_igor"]["button_fines_igor"])

# Кнопка "Штрафы Вячеслава"
dp.register_message_handler(fines_slava_handler, lambda message: message.text == yml_loader.fines_data["fines_slava"]["button_fines_slava"])