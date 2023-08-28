from data import yml_loader
from misc.loader import dp

from keyboards.update.update_func import (
    update_bot_button_handler,
    process_callback_next_update
)

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Обновить бота"
dp.register_message_handler(update_bot_button_handler, lambda message: message.text == yml_loader.update_data["update_bot"]["button_update_bot"])

# Кнопка "Завершить обновление"
dp.register_callback_query_handler(process_callback_next_update, lambda c: c.data == 'next_update')
