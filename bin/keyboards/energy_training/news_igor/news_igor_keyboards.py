from data import yml_loader
from misc.loader import dp

from keyboards.energy_training.news_igor.news_igor_func import (
    backward_month_handler_igor,
    message_december_handler_igor,
    message_november_handler_igor,
    message_september_handler_igor,
    message_оctober_handler_igor
)

from keyboards.energy_training.news_igor.message_igor_func import (
    # Сообщения за 05.09.2023
	month_september_05_handler
)

# Свяжите функции обработки сообщений с диспетчером
# Сообщения за Сентябрь
dp.register_message_handler(message_september_handler_igor, lambda message: message.text == yml_loader.news_igor_path["buttons"]["button_message_september"])

# Сообщения за Октябрь
dp.register_message_handler(message_оctober_handler_igor, lambda message: message.text == yml_loader.news_igor_path["buttons"]["button_message_оctober"])

# Сообщения за Ноябрь
dp.register_message_handler(message_november_handler_igor, lambda message: message.text == yml_loader.news_igor_path["buttons"]["button_message_november"])

# Сообщения за Декабрь
dp.register_message_handler(message_december_handler_igor, lambda message: message.text == yml_loader.news_igor_path["buttons"]["button_message_december"])

# Вернутся к выбору Месяца
dp.register_message_handler(backward_month_handler_igor, lambda message: message.text == yml_loader.news_igor_path["news_igor"]["button_backward_month"])

# Вкладки "Сообщения за 05.09.2023"
dp.register_message_handler(month_september_05_handler, lambda message: message.text == yml_loader.news_igor_path["buttons_month"]["button_nine"])