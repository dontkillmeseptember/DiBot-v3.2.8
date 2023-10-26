from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types
from misc.loader import dp, bot

from data.start_db import load_user_data, save_user_data, is_user_in_data
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
			elif selected_quests == "10/60":
				await battlepass_quest_thousand_message(message)
			elif selected_quests == "11/60":
				await battlepass_quest_twelve_message(message)
			elif selected_quests == "12/60":
				await battlepass_quest_thirteen_message(message)
			elif selected_quests == "13/60":
				await battlepass_quest_fourteen_message(message)
			elif selected_quests == "14/60":
				await battlepass_quest_fifteen_message(message)
	else:
		print("Error")

# Задание #1
async def battlepass_quest_one(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["quest"] = "Задание #1"
	save_user_data(user_data)

	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_one"], callback_data="start_two"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Задание #2
async def battlepass_quest_two(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "1/60"
	user_data[str(user_id)]["quest"] = "Задание #2"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_two"], callback_data="start_three"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_two_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_two"], callback_data="start_three"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_two"], reply_markup=inline_keyboard)

# Задание #3
async def battlepass_quest_three(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "2/60"
	user_data[str(user_id)]["quest"] = "Задание #3"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_three"], callback_data="start_four"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_three"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_three_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_three"], callback_data="start_four"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_three"], reply_markup=inline_keyboard)

# Задание #4
async def battlepass_quest_four(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "3/60"
	user_data[str(user_id)]["quest"] = "Задание #4"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_four"], callback_data="start_five"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_four"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_four_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_four"], callback_data="start_five"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_four"], reply_markup=inline_keyboard)

# Задание #5
async def battlepass_quest_five(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "4/60"
	user_data[str(user_id)]["quest"] = "Задание #5"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_five"], callback_data="start_six"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_five"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_five_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_five"], callback_data="start_six"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_five"], reply_markup=inline_keyboard)

# Задание #6
async def battlepass_quest_six(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "5/60"
	user_data[str(user_id)]["quest"] = "Задание #6"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_six"], callback_data="start_seven"))

	await bot.answer_callback_query(callback_query.id, text=yml_loader.quest_data["notification_rewards"]["unlock_pages"])

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_six"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_six_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_six"], callback_data="start_seven"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_six"], reply_markup=inline_keyboard)

# Задание #7
async def battlepass_quest_seven(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "6/60"
	user_data[str(user_id)]["quest"] = "Задание #7"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_seven"], callback_data="start_eight"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_seven"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_seven_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_seven"], callback_data="start_eight"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_seven"], reply_markup=inline_keyboard)

# Задание #8
async def battlepass_quest_eight(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "7/60"
	user_data[str(user_id)]["quest"] = "Задание #8"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_eight"], callback_data="start_nine"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_eight"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_eight_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_eight"], callback_data="start_nine"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_eight"], reply_markup=inline_keyboard)

# Задание #9
async def battlepass_quest_nine(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "8/60"
	user_data[str(user_id)]["quest"] = "Задание #9"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_nine"], callback_data="start_ten"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_nine"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_nine_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_nine"], callback_data="start_ten"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_nine"], reply_markup=inline_keyboard)

# Задание #10
async def battlepass_quest_ten(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "9/60"
	user_data[str(user_id)]["quest"] = "Задание #10"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_ten"], callback_data="start_thousand"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_ten"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_ten_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_ten"], callback_data="start_thousand"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_ten"], reply_markup=inline_keyboard)

# Задание #11
async def battlepass_quest_thousand(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "10/60"
	user_data[str(user_id)]["quest"] = "Задание #11"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_thousand"], callback_data="start_twelve"))

	await bot.answer_callback_query(callback_query.id, text=yml_loader.quest_data["notification_rewards"]["unlock_pages"])

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_thousand"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_thousand_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_thousand"], callback_data="start_twelve"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_thousand"], reply_markup=inline_keyboard)

# Задание #12
async def battlepass_quest_twelve(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "11/60"
	user_data[str(user_id)]["quest"] = "Задание #12"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_twelve"], callback_data="start_thirteen"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_twelve"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_twelve_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_twelve"], callback_data="start_thirteen"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_twelve"], reply_markup=inline_keyboard)

# Задание #13
async def battlepass_quest_thirteen(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "12/60"
	user_data[str(user_id)]["quest"] = "Задание #13"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_thirteen"], callback_data="start_fourteen"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_thirteen"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_thirteen_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_thirteen"], callback_data="start_fourteen"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_thirteen"], reply_markup=inline_keyboard)

# Задание #14
async def battlepass_quest_fourteen(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "13/60"
	user_data[str(user_id)]["quest"] = "Задание #14"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_fourteen"], callback_data="start_fifteen"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_fourteen"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_fourteen_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_fourteen"], callback_data="start_fifteen"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_fourteen"], reply_markup=inline_keyboard)

# Задание #15
async def battlepass_quest_fifteen(callback_query: types.CallbackQuery):
	# Изменяет прогресс боевого пропуска у пользователя
	user_id = callback_query.from_user.id
	user_data = load_user_data()
	user_data[str(user_id)]["battlepass"] = "14/60"
	user_data[str(user_id)]["quest"] = "Задание #15"
	save_user_data(user_data)

	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_fifteen"], callback_data="start_sixteen_the_witcher_two"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_fifteen"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def battlepass_quest_fifteen_message(message: types.Message):
	# Добавляет клавиатуру с кнопкой "Выполнить"
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["the_witcher_one_quests"]["button_quest_fifteen"], callback_data="start_sixteen_the_witcher_two"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_ONE, caption=yml_loader.quest_data["the_witcher_one_quests"]["quest_fifteen"], reply_markup=inline_keyboard)

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
	"start_ten": battlepass_quest_ten,
	"start_thousand": battlepass_quest_thousand,
	"start_twelve": battlepass_quest_twelve,
	"start_thirteen": battlepass_quest_thirteen,
	"start_fourteen": battlepass_quest_fourteen,
	"start_fifteen": battlepass_quest_fifteen
}

# Обработчик для кнопок вкладки "В путь!"
@dp.callback_query_handler(lambda query: query.data in handlers_battlepass)
async def contract_callback_handler(callback_query: types.CallbackQuery):
	handler_func = handlers_battlepass[callback_query.data]
	await handler_func(callback_query)