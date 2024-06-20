from data import yml_loader
from misc.loader import dp, moscow_tz
from misc.util import datetime

from keyboards.quest.quest_func import quest_handler, info_handler, info_rewards, start_battlepass

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Главное меню"
# Отсчет времени до остановки батлпасса
current_datetime = datetime.datetime.now(moscow_tz)
target_datetime = datetime.datetime(year=2024, month=1, day=15, hour=0, minute=0, second=0)
target_datetime = moscow_tz.localize(target_datetime)

time_diff = target_datetime - current_datetime

# Рассчитываем оставшееся время до целевой даты и времени
days = time_diff.days
hours = time_diff.seconds // 3600

dp.register_message_handler(quest_handler, lambda message: message.text == f"🐺 Белый Волк • Летопись Ведьмака • {days}Д {hours}Ч 🗡️")

# Кнопка "Информация о боевом пропуске"
dp.register_message_handler(info_handler, lambda message: message.text == yml_loader.quest_data["quest_buttons"]["info"])

# Кнопка "Награды боевого пропуска"
dp.register_message_handler(info_rewards, lambda message: message.text == yml_loader.quest_data["quest_buttons"]["awards"])

# Кнопка "В путь!"
dp.register_message_handler(start_battlepass, lambda message: message.text == "🗺️ В путь • Начать")

for progress in range(61):
    full_text = f"🗺️ В путь • Задание #{progress}"
    dp.register_message_handler(start_battlepass, lambda message, text=full_text: message.text == text)