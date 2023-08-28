from data import yml_loader
from misc.loader import dp

from keyboards.quest.quest_func import quest_handler, info_handler

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Главное меню"
dp.register_message_handler(quest_handler, lambda message: message.text == yml_loader.quest_data["quest"]["button_quest"])

# Кнопка "Информация о боевом пропуске"
dp.register_message_handler(info_handler, lambda message: message.text == yml_loader.quest_data["quest_buttons"]["info"])