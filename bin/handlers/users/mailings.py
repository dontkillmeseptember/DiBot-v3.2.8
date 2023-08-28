from misc.loader import dp, bot
from misc.util import types

from data import yml_loader
from data.mailings_db import get_all_subscribers, save_subscriber, delete_subscriber, is_subscribed, check_has_visited_ration

# Асинхронная функция для отправки запланированных сообщений календаря
async def send_scheduled_messages_calendar():
    message_text = yml_loader.mailings_path["calendar"]

    if message_text:
        subscribers_data = get_all_subscribers()

        for user_id, user_data in subscribers_data.items():
            is_subscribed = user_data.get("is_subscribed", False)
            if is_subscribed:
                await bot.send_message(int(user_id), message_text)

# Асинхронная функция для отправки запланированных грустных сообщений календаря
async def send_scheduled_messages_calendar_sad():
    message_text = yml_loader.mailings_path["calendar_sad"]

    if message_text:
        subscribers_data = get_all_subscribers()

        for user_id, user_data in subscribers_data.items():
            is_subscribed = user_data.get("is_subscribed", False)
            if is_subscribed:
                await bot.send_message(int(user_id), message_text)

# Изменим функцию send_scheduled_messages
async def send_scheduled_messages(day):
    message_text = yml_loader.mailings_path["ration"]

    dispatch = message_text.get(day)
    if dispatch:
        subscribers_data = get_all_subscribers()

        for user_id, user_data in subscribers_data.items():
            has_visited_ration = user_data.get("has_visited_ration", False)
            if not has_visited_ration:
                await bot.send_message(int(user_id), dispatch)

# Обработчик команды /subscribe
@dp.message_handler(commands=["subscribe"])
async def subscribe_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    if not is_subscribed(user_id):
        save_subscriber(user_id, username)
        await bot.send_message(user_id, yml_loader.mailings_path["info"]["subscribe_info"])
    else:
        await bot.send_message(user_id, yml_loader.mailings_path["info"]["subscribe_yes"])

# Обработчик команды /unsubscribe
@dp.message_handler(commands=["unsubscribe"])
async def unsubscribe_command(message: types.Message):
	user_id = message.from_user.id

	if is_subscribed(user_id):
		delete_subscriber(user_id)
		await bot.send_message(user_id, yml_loader.mailings_path["info"]["unsubscribe_info"])
	else:
		await bot.send_message(user_id, yml_loader.mailings_path["info"]["unsubscribe_yes"])