from misc.loader import dp, bot
from misc.util import types, InlineKeyboardMarkup, InlineKeyboardButton

from data import yml_loader
from data.mailings_db import get_all_subscribers, save_subscriber, delete_subscriber, is_subscribed
from data.start_db import check_user_data

from keyboards.energy_training.sport.sport_func import sport_handler
from keyboards.energy_training.cooking.ration.ration_func import ration_weekly_callback

# Асинхронная функция для отправки запланированных сообщений упражнений
async def send_scheduled_messages_sport():
	subscribers_data = get_all_subscribers()
	 
	for user_id, user_data in subscribers_data.items():
		has_visited_sport = user_data.get("has_visited_sport", False)
		if not has_visited_sport:
			inline_keyboard = InlineKeyboardMarkup()
			inline_keyboard.add(InlineKeyboardButton(yml_loader.mailings_data["buttons"]["check_sport"], callback_data="check_sport"))

			user_data_user = check_user_data(user_id)
			sport = user_data_user.get("selected_sport", "Uxknow")
			
			message_text = f"<b>👩🏻‍🦰💬 Сегодня - день для твоей физической активности! Почувствуй заряд энергии и подготовься к тренировке.</b>\n\n" \
							f"<b> • Ваш список упражнений: {sport}</b>"

			await bot.send_message(int(user_id), message_text, reply_markup=inline_keyboard)

# Коллбак обработчик для вызова спорта
@dp.callback_query_handler(lambda c: c.data == 'check_sport')
async def check_sport_button(callback_query: types.CallbackQuery):
	await sport_handler(callback_query.message)

# Асинхронная функция для отправки запланированных сообщений календаря
async def send_scheduled_messages_calendar():
	message_text = yml_loader.mailings_data["calendar"]

	if message_text:
		subscribers_data = get_all_subscribers()

		for user_id, user_data in subscribers_data.items():
			is_subscribed = user_data.get("is_subscribed", False)
			if is_subscribed:
				await bot.send_message(int(user_id), message_text)

# Асинхронная функция для отправки запланированных грустных сообщений календаря
async def send_scheduled_messages_calendar_sad():
	message_text = yml_loader.mailings_data["calendar_sad"]

	if message_text:
		subscribers_data = get_all_subscribers()

		for user_id, user_data in subscribers_data.items():
			is_subscribed = user_data.get("is_subscribed", False)
			if is_subscribed:
				await bot.send_message(int(user_id), message_text)

# Изменим функцию send_scheduled_messages
async def send_scheduled_messages(day):
	message_text = yml_loader.mailings_data["ration"]

	dispatch = message_text.get(day)
	if dispatch:
		subscribers_data = get_all_subscribers()

		for user_id, user_data in subscribers_data.items():
			has_visited_ration = user_data.get("has_visited_ration", False)
			if not has_visited_ration:
				inline_keyboard = InlineKeyboardMarkup()
				inline_keyboard.add(InlineKeyboardButton(yml_loader.mailings_data["buttons"]["check_ration"], callback_data="check_ration"))

				dp.register_message_handler(ration_weekly_callback, lambda c: c.data == 'check_ration')

				await bot.send_message(int(user_id), dispatch, reply_markup=inline_keyboard)

# Обработчик команды /subscribe
@dp.message_handler(commands=["subscribe"])
async def subscribe_command(message: types.Message):
	user_id = message.from_user.id
	username = message.from_user.username

	if not is_subscribed(user_id):
		save_subscriber(user_id, username)
		await bot.send_message(user_id, yml_loader.mailings_data["info"]["subscribe_info"])
	else:
		await bot.send_message(user_id, yml_loader.mailings_data["info"]["subscribe_yes"])

# Обработчик команды /unsubscribe
@dp.message_handler(commands=["unsubscribe"])
async def unsubscribe_command(message: types.Message):
	user_id = message.from_user.id

	if is_subscribed(user_id):
		delete_subscriber(user_id)
		await bot.send_message(user_id, yml_loader.mailings_data["info"]["unsubscribe_info"])
	else:
		await bot.send_message(user_id, yml_loader.mailings_data["info"]["unsubscribe_yes"])