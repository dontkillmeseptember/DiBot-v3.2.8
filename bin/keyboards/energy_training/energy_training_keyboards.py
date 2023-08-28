from data import yml_loader
from misc.loader import dp

from keyboards.energy_training.main import energy_training_menu_handler
from keyboards.energy_training.sport.sport_func import sport_handler

from keyboards.energy_training.news.news_func import news_handler
from keyboards.energy_training.cooking.cooking_func import cooking_handler

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Праздники и договор"
dp.register_message_handler(energy_training_menu_handler, lambda message: message.text == yml_loader.energy_training_data["button_energy_training"])

# Кнопка "Упражнения на неделю"
dp.register_message_handler(sport_handler, lambda message: message.text == yml_loader.sport_data["sport"]["button_sport"])

# Кнопка "Новости от Динары"
dp.register_message_handler(news_handler, lambda message: message.text == yml_loader.news_path["news"]["button_news"])

# Кнопка "Кулинарная лихорадка"
dp.register_message_handler(cooking_handler, lambda message: message.text == yml_loader.cooking_data["cooking"]["button_cooking"])