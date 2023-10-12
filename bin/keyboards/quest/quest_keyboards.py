from data import yml_loader
from misc.loader import dp

from keyboards.quest.quest_func import quest_handler, info_handler, info_rewards, start_battlepass

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Главное меню"
dp.register_message_handler(quest_handler, lambda message: message.text == yml_loader.quest_data["quest"]["button_quest"])

# Кнопка "Информация о боевом пропуске"
dp.register_message_handler(info_handler, lambda message: message.text == yml_loader.quest_data["quest_buttons"]["info"])

# Кнопка "Награды боевого пропуска"
dp.register_message_handler(info_rewards, lambda message: message.text == yml_loader.quest_data["quest_buttons"]["awards"])

# Кнопка "В путь!"
dp.register_message_handler(start_battlepass, lambda message: message.text == yml_loader.quest_data["quest_buttons"]["quest"])