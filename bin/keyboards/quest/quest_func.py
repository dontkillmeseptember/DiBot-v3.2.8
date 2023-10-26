from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, datetime, InlineKeyboardMarkup, InlineKeyboardButton
from misc.loader import bot, moscow_tz, dp

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data
from data.start_db import check_user_data, load_user_data, is_user_in_data

from data.config import PHOTO_PATH, PHOTO_PATH_PREVIEW, PHOTO_REWARD

from keyboards.quest.witcherone_func import start_the_witcher_one
from keyboards.quest.witchertwo_func import start_the_witcher_two
# from keyboards.quest.witcherthree_func import start_the_witcher_three

def create_quest_keyboard(message):
	# Выводим информацию о пользователе для кнопки "Ваш прогресс"
	user = message.from_user
	user_id = user.id
	user_data = check_user_data(user_id)
	battlepass = user_data.get("battlepass", "Uxknow")
	quest = user_data.get("quest", "Начать")

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.quest_data["quest_buttons"]["awards"]),
		KeyboardButton(yml_loader.quest_data["quest_buttons"]["info"])
	)
	keyboard.add(KeyboardButton(f"🗺️ В путь • {quest}"))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]),
		KeyboardButton(f"📈 Ваш прогресс — {battlepass}")
	)

	return keyboard

# Обработчик вкладки "Задания"
async def quest_handler(message: types.Message):
	# Переменная для кнопок
	keyboard = create_quest_keyboard(message)

	await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["battlepass_info"], reply_markup=keyboard)

# Обработчик вкладки "В путь!"
async def start_battlepass(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже выбранная часть у пользователя
		if str(user_id) in user_data and "active_chapter" in user_data[str(user_id)]:
			selected_chapters = user_data[str(user_id)]["active_chapter"]

			if selected_chapters is None:
				await start_the_witcher_one(message)
			elif selected_chapters == "the_witcher_two":
				await start_the_witcher_two(message)
			elif selected_chapters == "the_witcher_three":
				await start_the_witcher_three(message)
	else:
		print("User not registor.")

# Обработчик вкладки "Награды боевого пропуска"
async def info_rewards(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже выбранная часть у пользователя
		if str(user_id) in user_data and "active_chapter" in user_data[str(user_id)]:
			selected_chapters = user_data[str(user_id)]["active_chapter"]

			if selected_chapters is None:
				await rewards_selected_one(message)
			elif selected_chapters == "the_witcher_two":
				await rewards_selected_two(message)
			elif selected_chapters == "the_witcher_three":
				await rewards_selected_three(message)
	else:
		print("User not registor.")

# Обработчик выбора наград для частей
async def rewards_selected_one(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_one"], callback_data="rewards_one"))

	await bot.send_photo(message.chat.id, photo=PHOTO_REWARD, caption=yml_loader.quest_data["quest"]["reward_info"], reply_markup=inline_keyboard)

async def rewards_selected_two(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_one"], callback_data="rewards_one_two"),
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_two"], callback_data="rewards_two")
	)

	await bot.send_photo(message.chat.id, photo=PHOTO_REWARD, caption=yml_loader.quest_data["quest"]["reward_info"], reply_markup=inline_keyboard)

async def rewards_selected_three(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_one"], callback_data="rewards_one_three"),
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_two"], callback_data="rewards_two")
	)

	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_three"], callback_data="rewards_three"))

	await bot.send_photo(message.chat.id, photo=PHOTO_REWARD, caption=yml_loader.quest_data["quest"]["reward_info"], reply_markup=inline_keyboard)

# Обработчик наград для первой части
@dp.callback_query_handler(lambda c: c.data == 'rewards_one')
async def rewards_one_one(callback_query: types.CallbackQuery):
	await bot.edit_message_caption(caption=yml_loader.quest_data["quest"]["reward_info_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

@dp.callback_query_handler(lambda c: c.data == 'rewards_one_two')
async def rewards_one_two(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_two"], callback_data="rewards_two"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["quest"]["reward_info_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'rewards_one_three')
async def rewards_one_three(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_two"], callback_data="rewards_two_two"),
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_three"], callback_data="rewards_three")
	)

	await bot.edit_message_caption(caption=yml_loader.quest_data["quest"]["reward_info_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик наград для второй части
@dp.callback_query_handler(lambda c: c.data == 'rewards_two')
async def rewards_two_one(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_one"], callback_data="rewards_one_two"))

	await bot.edit_message_caption(caption=yml_loader.quest_data["quest"]["reward_info_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'rewards_two_two')
async def rewards_two_two(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_one"], callback_data="rewards_one_three"),
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_three"], callback_data="rewards_three")
	)

	await bot.edit_message_caption(caption=yml_loader.quest_data["quest"]["reward_info_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик наград для третей части
@dp.callback_query_handler(lambda c: c.data == 'rewards_three')
async def rewards_three(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_one"], callback_data="rewards_one_three"),
		InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["rewards_two"], callback_data="rewards_two_two")
	)

	await bot.edit_message_caption(caption=yml_loader.quest_data["quest"]["reward_info_three"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик вкладки "Информация о боевом пропуске"
async def info_handler(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже выбранная часть у пользователя
		if str(user_id) in user_data and "active_chapter" in user_data[str(user_id)]:
			selected_chapters = user_data[str(user_id)]["active_chapter"]

			if selected_chapters is None:
				await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info_one"])
			elif selected_chapters == "the_witcher_two":
				await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info_two"])
			elif selected_chapters == "the_witcher_three":
				await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info_three"])
	else:
		print("User not registor.")
