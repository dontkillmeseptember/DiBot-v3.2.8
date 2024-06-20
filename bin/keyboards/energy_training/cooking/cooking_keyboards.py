from misc.loader import dp
from data import yml_loader

from keyboards.energy_training.cooking.ration.ration_func import ration_weekly_callback

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Рацион на неделю"
dp.register_message_handler(ration_weekly_callback, lambda message: message.text == f"{yml_loader.ration_data['ration']['button_ration']}{yml_loader.ration_data['ration']['name_ration']}")