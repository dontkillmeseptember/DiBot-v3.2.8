from misc.util import types, InlineKeyboardMarkup, InlineKeyboardButton, json, os
from misc.loader import dp, bot

from data.start_db import load_user_data, is_user_in_data, save_user_data

from data import yml_loader

# Обработчик "Кодекс силы"
async def sport_handler(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже выбранный интерфейс у пользователя
		if str(user_id) in user_data and "sport" in user_data[str(user_id)]:
			selected_sport = user_data[str(user_id)]["sport"]
			
			if selected_sport is None:
				await sport_selected(message)
			elif selected_sport == "legs":
				await sport_legs_selected(message)
			elif selected_sport == "hand":
				await sport_hand_selected(message)
			elif selected_sport == "heart":
				await sport_heart_selected(message)

	else:
		print("User not registor.")

# Обработчик выбора упражнений
async def sport_selected(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.sport_data["sport"]["sport_legs"], callback_data="sport_legs"),
		InlineKeyboardButton(yml_loader.sport_data["sport"]["sport_hand"], callback_data="sport_hand")
	)

	inline_keyboard.add(InlineKeyboardButton(yml_loader.sport_data["sport"]["sport_heart"], callback_data="sport_heart"))

	await message.answer(yml_loader.sport_data["sport"]["sport_start"], reply_markup=inline_keyboard)

# Обработчик выбора упражений на ноги
@dp.callback_query_handler(lambda c: c.data == 'sport_legs')
async def sport_legs(callback_query: types.CallbackQuery):
	user_id = callback_query.from_user.id
	file_path = os.path.join("bin", "db", "subscribers.json")
	user_data = load_user_data()

	with open(file_path, "r") as file:
		subscribers_data = json.load(file)

	user_data_sport = subscribers_data.get(str(user_id), {})
	has_visited_sport = user_data_sport.get("has_visited_sport", False)

	user_data[str(user_id)]["selected_sport"] = yml_loader.sport_data["sport"]["sport_legs"]
	user_data[str(user_id)]["sport"] = "legs"
	save_user_data(user_data)

	if not has_visited_sport:
		await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_legs"])
		await bot.edit_message_text(yml_loader.sport_data["sport"]["sport_legs_info"], callback_query.from_user.id, callback_query.message.message_id)

		user_data_sport["has_visited_sport"] = True
		subscribers_data[str(user_id)] = user_data_sport
		with open(file_path, "w") as file:
			json.dump(subscribers_data, file, indent=4)
	else:
		await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_legs"])
		await bot.edit_message_text(yml_loader.sport_data["sport"]["sport_legs_info"], callback_query.from_user.id, callback_query.message.message_id)

async def sport_legs_selected(message: types.Message):
	user_id = message.from_user.id
	file_path = os.path.join("bin", "db", "subscribers.json")
	
	with open(file_path, "r") as file:
		subscribers_data = json.load(file)
	
	user_data = subscribers_data.get(str(user_id), {})
	has_visited_sport = user_data.get("has_visited_sport", False)

	if not has_visited_sport:
		await message.answer(yml_loader.sport_data["sport"]["sport_legs_info"])

		user_data["has_visited_sport"] = True
		subscribers_data[str(user_id)] = user_data
		with open(file_path, "w") as file:
			json.dump(subscribers_data, file, indent=4)
	else:
		await message.answer(yml_loader.sport_data["sport"]["sport_legs_info"])

# Обработчик выбора упражений на руки
@dp.callback_query_handler(lambda c: c.data == 'sport_hand')
async def sport_hand(callback_query: types.CallbackQuery):
	user_id = callback_query.from_user.id
	file_path = os.path.join("bin", "db", "subscribers.json")
	user_data = load_user_data()

	with open(file_path, "r") as file:
		subscribers_data = json.load(file)

	user_data_sport = subscribers_data.get(str(user_id), {})
	has_visited_sport = user_data_sport.get("has_visited_sport", False)

	user_data[str(user_id)]["selected_sport"] = yml_loader.sport_data["sport"]["sport_hand"]
	user_data[str(user_id)]["sport"] = "hand"
	save_user_data(user_data)

	if not has_visited_sport:
		await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_hand"])
		await bot.edit_message_text(yml_loader.sport_data["sport"]["sport_hand_info"], callback_query.from_user.id, callback_query.message.message_id)

		user_data_sport["has_visited_sport"] = True
		subscribers_data[str(user_id)] = user_data_sport
		with open(file_path, "w") as file:
			json.dump(subscribers_data, file, indent=4)
	else:
		await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_hand"])
		await bot.edit_message_text(yml_loader.sport_data["sport"]["sport_hand_info"], callback_query.from_user.id, callback_query.message.message_id)

async def sport_hand_selected(message: types.Message):
	user_id = message.from_user.id
	file_path = os.path.join("bin", "db", "subscribers.json")
	
	with open(file_path, "r") as file:
		subscribers_data = json.load(file)
	
	user_data = subscribers_data.get(str(user_id), {})
	has_visited_sport = user_data.get("has_visited_sport", False)

	if not has_visited_sport:
		await message.answer(yml_loader.sport_data["sport"]["sport_hand_info"])

		user_data["has_visited_sport"] = True
		subscribers_data[str(user_id)] = user_data
		with open(file_path, "w") as file:
			json.dump(subscribers_data, file, indent=4)
	else:
		await message.answer(yml_loader.sport_data["sport"]["sport_hand_info"])

# Обработчик выбора упражений на пресс
@dp.callback_query_handler(lambda c: c.data == 'sport_heart')
async def sport_heart(callback_query: types.CallbackQuery):
	user_id = callback_query.from_user.id
	file_path = os.path.join("bin", "db", "subscribers.json")
	user_data = load_user_data()

	with open(file_path, "r") as file:
		subscribers_data = json.load(file)

	user_data_sport = subscribers_data.get(str(user_id), {})
	has_visited_sport = user_data_sport.get("has_visited_sport", False)

	user_data[str(user_id)]["selected_sport"] = yml_loader.sport_data["sport"]["sport_heart"]
	user_data[str(user_id)]["sport"] = "heart"
	save_user_data(user_data)

	if not has_visited_sport:
		await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_heart"])
		await bot.edit_message_text(yml_loader.sport_data["sport"]["sport_heart_info"], callback_query.from_user.id, callback_query.message.message_id)

		user_data_sport["has_visited_sport"] = True
		subscribers_data[str(user_id)] = user_data_sport
		with open(file_path, "w") as file:
			json.dump(subscribers_data, file, indent=4)
	else:
		await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_heart"])
		await bot.edit_message_text(yml_loader.sport_data["sport"]["sport_heart_info"], callback_query.from_user.id, callback_query.message.message_id)

async def sport_heart_selected(message: types.Message):
	user_id = message.from_user.id
	file_path = os.path.join("bin", "db", "subscribers.json")
	
	with open(file_path, "r") as file:
		subscribers_data = json.load(file)
	
	user_data = subscribers_data.get(str(user_id), {})
	has_visited_sport = user_data.get("has_visited_sport", False)

	if not has_visited_sport:
		await message.answer(yml_loader.sport_data["sport"]["sport_heart_info"])

		user_data["has_visited_sport"] = True
		subscribers_data[str(user_id)] = user_data
		with open(file_path, "w") as file:
			json.dump(subscribers_data, file, indent=4)
	else:
		await message.answer(yml_loader.sport_data["sport"]["sport_heart_info"])