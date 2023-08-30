from misc.util import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton,
	types,
	datetime
)

from misc.loader import bot, moscow_tz, dp

from data import yml_loader

# Обработчик вкладки "Обновления бота"
async def version_handler(message: types.Message):
	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))
	keyboard.row(
		KeyboardButton(yml_loader.version_data["version_0_0_1"]["button_update_jule_zero_zero_one"]),
		KeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_zero_two"]),
		KeyboardButton(yml_loader.version_data["version_0_0_3"]["button_update_september_zero_zero_three"])
	)

	# Получение текущей даты и времени
	current_datetime = datetime.datetime.now(moscow_tz)
	target_datetime = datetime.datetime(current_datetime.year, month=7, day=16, hour=23, minute=0, second=0)  # Целевая дата и время (17 июля, 00:00)
	target_datetime = moscow_tz.localize(target_datetime)
	
	time_diff = target_datetime - current_datetime

	# Рассчитываем оставшееся время до целевой даты и времени
	days = time_diff.days
	hours = time_diff.seconds // 3600
	minutes = (time_diff.seconds % 3600) // 60

	if time_diff.total_seconds() > 0:
		await bot.send_message(message.chat.id, f"<b>🧑🏻‍🦱💬 Вкладка — <code>{yml_loader.version_data['version']['button_update']}</code> будет доступна через: <code>{days} дней {hours} часов и {minutes} минут.</code></b>")
	else: 
		await bot.send_message(
			message.chat.id, 
			yml_loader.version_data["version"]["button_update_info"], 
			reply_markup=keyboard
		)

# Обработчик вкладки "Обновление за 01.09.2023"
async def update_zero_zero_three_handler(callback_query: types.CallbackQuery):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_3"]["button_update_august_3_3_8"], callback_data="update_3_3_8"))

	await bot.send_message(
			callback_query.chat.id, 
			yml_loader.version_data["version_0_0_3"]["button_update_jule_zero_two_three_info"],
			reply_markup=inline_keyboard
		)

@dp.callback_query_handler(lambda query: query.data == "update_3_3_8")
async def update_3_3_8_handler(callback_query: types.CallbackQuery):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_3"]["button_update_september_zero_zero_three"], callback_data="update_3_2_8"))

	await bot.edit_message_text(
			yml_loader.version_data["version_0_0_3"]["button_update_jule_3.3.8_info"],
			callback_query.from_user.id,
			callback_query.message.message_id, 
			reply_markup=inline_keyboard
		)

@dp.callback_query_handler(lambda query: query.data == "update_3_2_8")
async def update_zero_zero_three_handler_two(callback_query: types.CallbackQuery):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_3"]["button_update_august_3_3_8"], callback_data="update_3_3_8"))

	await bot.edit_message_text(
			yml_loader.version_data["version_0_0_3"]["button_update_jule_zero_two_three_info"],
			callback_query.from_user.id,
			callback_query.message.message_id, 
			reply_markup=inline_keyboard
		)

# Обработчик вкладки "Обновление за 06.08.2023"
async def update_zero_zero_two_handler(message: types.Message):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_one_two"], callback_data="update_0_1_2"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_two_two"], callback_data="update_0_2_2"))

	await bot.send_message(
			message.chat.id, 
			yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_zero_two_info"], 
			reply_markup=inline_keyboard
		)

@dp.callback_query_handler(lambda query: query.data == "update_0_1_2")
async def update_zero_one_two_handler(callback_query: types.CallbackQuery):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_zero_two"], callback_data="update_0_0_2"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_two_two"], callback_data="update_0_2_2"))

	await bot.edit_message_text(
			yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_one_two_info"],
			callback_query.from_user.id,
			callback_query.message.message_id, 
			reply_markup=inline_keyboard
		)

@dp.callback_query_handler(lambda query: query.data == "update_0_2_2")
async def update_zero_two_two_handler(callback_query: types.CallbackQuery):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_zero_two"], callback_data="update_0_0_2"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_one_two"], callback_data="update_0_1_2"))

	await bot.edit_message_text(
			yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_two_two_info"],
			callback_query.from_user.id,
			callback_query.message.message_id, 
			reply_markup=inline_keyboard
		)

@dp.callback_query_handler(lambda query: query.data == "update_0_0_2")
async def update_zero_one_two_handler_two(callback_query: types.CallbackQuery):
	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_one_two"], callback_data="update_0_1_2"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_two_two"], callback_data="update_0_2_2"))

	await bot.edit_message_text(
			yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_zero_two_info"],
			callback_query.from_user.id,
			callback_query.message.message_id, 
			reply_markup=inline_keyboard
		)

# Обработчик вкладки "Обновление за 17.07.2023"
async def update_zero_zero_one_handler(message: types.Message):
	await bot.send_message(message.chat.id, yml_loader.version_data["version_0_0_1"]["button_update_jule_zero_zero_one_info"])
