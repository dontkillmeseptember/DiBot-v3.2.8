from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types
from misc.loader import dp, bot

from data.start_db import check_user_data, load_user_data, save_user_data, is_user_in_data
from data.config import PHOTO_THE_WITCHER_ONE

from data import yml_loader

# Обработчик первой части ведьмака
async def start_the_witcher_one(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["start"], callback_data="start_one"))

	# Проверяет какой прогресс боевого пропуска у пользователя
	if is_user_in_data(user_id, user_data):
		# Проверяем, какой квест пройден у пользователя
		if str(user_id) in user_data and "battlepass" in user_data[str(user_id)]:
			selected_quests = user_data[str(user_id)]["battlepass"]
			
			if selected_quests == "0/60":
				await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["quest"]["thewitcherone_info"], reply_markup=inline_keyboard)
			elif selected_quests == "1/60":
				await battlepass_quest_two_message(message)
			elif selected_quests == "2/60":
				await battlepass_quest_three_message(message)
			elif selected_quests == "3/60":
				await battlepass_quest_four_message(message)
			elif selected_quests == "4/60":
				await battlepass_quest_five_message(message)
			elif selected_quests == "5/60":
				await battlepass_quest_six_message(message)
			elif selected_quests == "6/60":
				await battlepass_quest_seven_message(message)
			elif selected_quests == "7/60":
				await battlepass_quest_eight_message(message)
			elif selected_quests == "8/60":
				await battlepass_quest_nine_message(message)
			elif selected_quests == "9/60":
				await battlepass_quest_ten_message(message)
	else:
		print("Error")

# Задание #1
async def battlepass_quest_one(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_two"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Задание #2
async def battlepass_quest_two(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "1/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_three"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_two_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_three"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_two"], reply_markup=inline_keyboard)

# Задание #3
async def battlepass_quest_three(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "2/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_four"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_three"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_three_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_four"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_three"], reply_markup=inline_keyboard)

# Задание #4
async def battlepass_quest_four(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "3/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_five"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_four"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_four_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_five"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_four"], reply_markup=inline_keyboard)

# Задание #5
async def battlepass_quest_five(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "4/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_six"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_five"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_five_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_six"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_five"], reply_markup=inline_keyboard)

# Задание #6
async def battlepass_quest_six(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "5/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_seven"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_six"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_six_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_seven"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_six"], reply_markup=inline_keyboard)

# Задание #7
async def battlepass_quest_seven(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "6/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_eight"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_seven"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_seven_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_eight"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_seven"], reply_markup=inline_keyboard)

# Задание #8
async def battlepass_quest_eight(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "7/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_nine"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_eight"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_eight_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_nine"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_eight"], reply_markup=inline_keyboard)

# Задание #9
async def battlepass_quest_nine(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "8/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_ten"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_nine"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_nine_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_ten"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_nine"], reply_markup=inline_keyboard)

# Задание #10
async def battlepass_quest_ten(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "9/60"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_thousand"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_ten"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_ten_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["contnt"], callback_data="start_thousand"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_ten"], reply_markup=inline_keyboard)

# Обработчики для каждой кнопки
handlers_battlepass = {
	"start_one": battlepass_quest_one,
	"start_two": battlepass_quest_two,
	"start_three": battlepass_quest_three,
	"start_four": battlepass_quest_four,
	"start_five": battlepass_quest_five,
	"start_six": battlepass_quest_six,
	"start_seven": battlepass_quest_seven,
	"start_eight": battlepass_quest_eight,
	"start_nine": battlepass_quest_nine,
	"start_ten": battlepass_quest_ten
}

# Обработчик для кнопок вкладки "В путь!"
@dp.callback_query_handler(lambda query: query.data in handlers_battlepass)
async def contract_callback_handler(callback_query: types.CallbackQuery):
	handler_func = handlers_battlepass[callback_query.data]
	await handler_func(callback_query)