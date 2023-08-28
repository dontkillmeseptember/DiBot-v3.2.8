from misc.util import types, logging
from misc.loader import dp, bot

from data.notices_db import send_message_to_subscribers_except_admin
from data.admin_db import load_admin_data, is_admin_in_data

from data import yml_loader

# Обработчик команды /nt
@dp.message_handler(commands=['nt'])
async def send_nt_message_command(message: types.Message):
    # Сообщение для отправки
    message_text = yml_loader.notices_path["notices"]["notices_info"]

    # Проверяем, является ли пользователь администратором
    user_id = message.from_user.id
    admin_data = load_admin_data()

    if is_admin_in_data(user_id, admin_data):
        # Отправляем сообщение всем подписчикам, кроме администратора
        await send_message_to_subscribers_except_admin(message_text, user_id)

        await bot.send_message(message.chat.id, yml_loader.notices_path["notices"]["notices_end"])
    else:
        await bot.send_message(message.chat.id, yml_loader.admin_path["delete_admin"]["user_not_admin"])
