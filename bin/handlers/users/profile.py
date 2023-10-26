from misc.loader import dp, bot
from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, FSMContext, State, StatesGroup, logging, Text, asyncio

from data.start_db import check_user_data, load_user_data, save_user_data
from data.config import PASSWORD_IGOR, PASSWORD_DINARA, SECRET_PASSWORD 

from data import yml_loader

class LanguageStateTwo(StatesGroup):
	waiting_for_language_two = State()

class RegistrationState(StatesGroup):
	waiting_for_password_role = State()

# Обработчик функции для inline_keyboards
def profile_menu():
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["contraft_interface"]["button_interface"], callback_data="interface_menu"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.role_path["role"]["shift_role"], callback_data="role_menu"))
	# inline_keyboard.add(InlineKeyboardButton(yml_loader.mailings_path["mailings"]["button_mailings"], callback_data="mailings_menu"))
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.language_path["language"]["button_language"], callback_data="language_menu"),
		InlineKeyboardButton(yml_loader.sport_data["sport"]["selected_sport"], callback_data="sport_menu")
	)

	return inline_keyboard

# Обработка профиля
async def profile_command(message: types.Message):
	inline_keyboard = profile_menu()

	user = message.from_user
	userlastname = user.first_name
	user_id = user.id
	username = f"@{user.username}" if user.username else None
	
	# Получаем фотографию пользователя
	photo = await bot.get_user_profile_photos(user_id)
	
	# Получаем информацию о пользователе
	user_data = check_user_data(user_id)
	role = user_data.get("role", "Uxknow")
	bot_id = user_data.get("bot_id", "Uxknow")
	language = user_data.get("language", "Uxknow")
	smile = user_data.get("smile", "Uxknow")
	battlepass = user_data.get("battlepass", "Uxknow")
	

	caption = f"<b>👩🏻‍🦰💬 Ваша текущая информация о профиле.</b>\n\n" \
				f"<b> • Ваше имя на текущий момент: {userlastname}</b>\n" \
				f"<b> • Ваше имя пользователя: {username}</b>\n" \
				f"<b> • Ваш user_id: </b><code>{user_id}</code>\n\n" \
				f"<b> • Ваш bot_id: </b><code>{bot_id}</code>\n" \
				f"<b> • Ваша роль на данный момент: {smile} {role}</b>\n\n" \
				f"<b> • Ваш прогресс в боевом пропуске: {battlepass}</b>\n\n" \
				f"<b> • Выбранный язык приложения: {language}</b>\n\n"

	if photo.photos:
		# Берем текущую фотографию пользователя (первая в списке)
		photo_file_id = photo.photos[0][-1].file_id
		await bot.send_photo(chat_id=message.chat.id, photo=photo_file_id, caption=caption, reply_markup=inline_keyboard)
	else:
		await bot.send_message(message.chat.id, caption)

# Обработчик вкладки "Сменить упражнение"
@dp.callback_query_handler(lambda c: c.data == 'sport_menu')
async def change_sport(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.language_path["language"]["button_back"], callback_data="back_profile"))
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.sport_data["sport"]["sport_legs"], callback_data="sport_legs_change"),
		InlineKeyboardButton(yml_loader.sport_data["sport"]["sport_hand"], callback_data="sport_hand_change")
	)

	inline_keyboard.add(InlineKeyboardButton(yml_loader.sport_data["sport"]["sport_heart"], callback_data="sport_heart_change"))

	await bot.edit_message_caption(caption=yml_loader.sport_data["sport"]["sport_changes"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик выбора упражнения для ноги
@dp.callback_query_handler(Text(startswith="sport_legs_change"), state="*")
async def change_sport_legs(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора упражнения в user_data
	user_data[str(user_id)]["selected_sport"] = yml_loader.sport_data["sport"]["sport_legs"]
	user_data[str(user_id)]["sport"] = "legs"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_legs"])

	await profile_end(callback_query, state)

# Обработчик выбора упражнения для руки
@dp.callback_query_handler(Text(startswith="sport_hand_change"), state="*")
async def change_sport_hand(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора упражнения в user_data
	user_data[str(user_id)]["selected_sport"] = yml_loader.sport_data["sport"]["sport_hand"]
	user_data[str(user_id)]["sport"] = "hand"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_hand"])

	await profile_end(callback_query, state)

# Обработчик выбора упражнения для пресс
@dp.callback_query_handler(Text(startswith="sport_heart_change"), state="*")
async def change_sport_heart(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора упражнения в user_data
	user_data[str(user_id)]["selected_sport"] = yml_loader.sport_data["sport"]["sport_heart"]
	user_data[str(user_id)]["sport"] = "heart"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.sport_data["sport"]["text_sport_changes_heart"])

	await profile_end(callback_query, state)

# Обработчик вкладки "Идентифицировать новую роль"
@dp.callback_query_handler(lambda c: c.data == 'role_menu')
async def role_handler(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.language_path["language"]["button_back"], callback_data="back_profile"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.role_path["role"]["id_role"], callback_data="next_role"))

	await bot.edit_message_caption(caption=yml_loader.role_path["role"]["role_menu_info"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'next_role')
async def role_start(callback_query: types.CallbackQuery):
	await bot.edit_message_caption(caption=yml_loader.role_path["role"]["password_role"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)

	await RegistrationState.waiting_for_password_role.set()

@dp.message_handler(state=RegistrationState.waiting_for_password_role)
async def process_password_role(callback_query: types.CallbackQuery, state: FSMContext):
	user_role = callback_query.text

	if user_role == PASSWORD_IGOR:
			user_id = callback_query.from_user.id
			user_data = load_user_data()

			text_select_none = f"<b>🧑🏻‍🦱💬 Вы успешно идентифицированы!</b>\n" \
									"<b>     						↳ </b><b>Ваша уникальный роль: </b>" + f"<b>{yml_loader.start_bot_path['registor']['smile_igor']} {yml_loader.role_path['roles']['role_igor']}</b>"

			# Сохранение роли в user_data
			user_data[str(user_id)]["role"] = yml_loader.role_path["roles"]["role_igor"]
			user_data[str(user_id)]["smile"] = yml_loader.start_bot_path["registor"]["smile_igor"]
			save_user_data(user_data)

			await bot.send_message(callback_query.from_user.id, text_select_none)

			await asyncio.sleep(5)

			await profile_end_two(callback_query, state)

	elif user_role == PASSWORD_DINARA:
			user_id = callback_query.from_user.id
			user_data = load_user_data()

			text_select_none = f"<b>🧑🏻‍🦱💬 Вы успешно идентифицированы!</b>\n" \
									"<b>     						↳ </b><b>Ваша уникальный роль: </b>" + f"<b>{yml_loader.start_bot_path['registor']['smile_dinara']} {yml_loader.role_path['roles']['role_dinara']}</b>"

			# Сохранение роли в user_data
			user_data[str(user_id)]["role"] = yml_loader.role_path["roles"]["role_dinara"]
			user_data[str(user_id)]["smile"] = yml_loader.start_bot_path["registor"]["smile_dinara"]
			save_user_data(user_data)

			await bot.send_message(callback_query.from_user.id, text_select_none)

			await asyncio.sleep(5)

			await profile_end_two(callback_query, state)
	
	elif user_role == SECRET_PASSWORD:
			user_id = callback_query.from_user.id
			user_data = load_user_data()

			text_select_none = f"<b>🧑🏻‍🦱💬 Вы успешно идентифицированы!</b>\n" \
									"<b>     						↳ </b><b>Ваша уникальный роль: </b>" + f"<b>{yml_loader.start_bot_path['registor']['smile_admin']} {yml_loader.admin_path['admin']['admin_role']}</b>"

			# Сохранение роли в user_data
			user_data[str(user_id)]["role"] = yml_loader.admin_path["admin"]["admin_role"]
			user_data[str(user_id)]["smile"] = yml_loader.start_bot_path["registor"]["smile_admin"]
			save_user_data(user_data)

			await bot.send_message(callback_query.from_user.id, text_select_none)

			await asyncio.sleep(5)

			await profile_end_two(callback_query, state)

	else:
		await bot.send_message(callback_query.from_user.id, yml_loader.admin_path["admin"]["error_password"])

# Обработчик вкладки "Сменить интерфейс договора"
@dp.callback_query_handler(lambda c: c.data == 'interface_menu')
async def interface_handler(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.language_path["language"]["button_back"], callback_data="back_profile"))
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["contraft_interface"]["old_interface"], callback_data="interface_profile_old"),
		InlineKeyboardButton(yml_loader.contract_path["contraft_interface"]["new_interface"], callback_data="interface_profile_new")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contraft_interface"]["interface_info"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для выбора старого интерфейса
@dp.callback_query_handler(Text(startswith="interface_profile_old"), state="*")
async def save_old_interface(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора интерфейса в user_data
	user_data[str(user_id)]["interface_contract"] = "old_interface"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.contract_path["contraft_interface"]["text_old_interface"])

	await profile_end(callback_query, state)

# Обработчик для выбора нового интерфейса
@dp.callback_query_handler(Text(startswith="interface_profile_new"), state="*")
async def save_new_interface(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора интерфейса в user_data
	user_data[str(user_id)]["interface_contract"] = "new_interface"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.contract_path["contraft_interface"]["text_new_interface"])

	await profile_end(callback_query, state)

# Обработчик вкладки "Смена языка"
@dp.callback_query_handler(lambda c: c.data == 'language_menu')
async def language_handler(callback_query: types.CallbackQuery, state: FSMContext):
	# Создаем inline клавиатуру с кнопкой выбора языка
	languages_keyboard = InlineKeyboardMarkup(row_width=2)
	languages_keyboard.add(InlineKeyboardButton(yml_loader.language_path["language"]["button_back"], callback_data="back_language"))
	languages = [yml_loader.language_path["buttons_language"]["button_russian"], yml_loader.language_path["buttons_language"]["button_english"], 
		   			yml_loader.language_path["buttons_language"]["button_georgian"], yml_loader.language_path["buttons_language"]["button_ukranian"], 
					yml_loader.language_path["buttons_language"]["button_spanish"], yml_loader.language_path["buttons_language"]["button_french"], 
					yml_loader.language_path["buttons_language"]["button_german"], yml_loader.language_path["buttons_language"]["button_polish"]]

	# Размещаем кнопки в рядах по две
	for i in range(0, len(languages), 2):
		row_buttons = [InlineKeyboardButton(text=languages[i], callback_data=languages[i])]

		if i + 1 < len(languages):
			row_buttons.append(InlineKeyboardButton(text=languages[i + 1], callback_data=languages[i + 1]))
		languages_keyboard.row(*row_buttons)

	await bot.edit_message_caption(caption=yml_loader.language_path["select_language"]["language_info"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=languages_keyboard)

	await LanguageStateTwo.waiting_for_language_two.set()

@dp.callback_query_handler(state=LanguageStateTwo.waiting_for_language_two)
async def select_language(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	languages = [yml_loader.language_path["buttons_language"]["button_russian"], yml_loader.language_path["buttons_language"]["button_english"], 
		   		 yml_loader.language_path["buttons_language"]["button_georgian"], yml_loader.language_path["buttons_language"]["button_ukranian"], 
				 yml_loader.language_path["buttons_language"]["button_spanish"], yml_loader.language_path["buttons_language"]["button_french"], 
				 yml_loader.language_path["buttons_language"]["button_german"], yml_loader.language_path["buttons_language"]["button_polish"]]

	try:
		chosen_language = callback_query.data
		back_to_language = "back_language"

		if chosen_language in languages:
			# Обновляем язык пользователя в user_data.json
			user_data[str(user_id)]["language"] = chosen_language
			save_user_data(user_data)

			await profile_end(callback_query, state)

		elif callback_query.data == back_to_language:
			await profile_end(callback_query, state)

	except Exception:
		logging.exception("Ошибочка")

# Обработчик вкладки "Профиль после функций"
async def profile_end_two(callback_query: types.CallbackQuery, state: FSMContext):
	user = callback_query.from_user
	userlastname = user.first_name
	user_id = user.id
	username = f"@{user.username}" if user.username else None

	# Получаем фотографию пользователя
	photo = await bot.get_user_profile_photos(user_id)

	inline_keyboard = profile_menu()

	# Получаем информацию о пользователе
	user_data = check_user_data(user_id)
	role = user_data.get("role", "Uxknow")
	bot_id = user_data.get("bot_id", "Uxknow")
	language = user_data.get("language", "Uxknow")
	smile = user_data.get("smile", "Uxknow")
	battlepass = user_data.get("battlepass", "Uxknow")

	caption = f"<b>👩🏻‍🦰💬 Ваша текущая информация о профиле.</b>\n\n" \
				f"<b> • Ваше имя на текущий момент: {userlastname}</b>\n" \
				f"<b> • Ваше имя пользователя: {username}</b>\n" \
				f"<b> • Ваш user_id: </b><code>{user_id}</code>\n\n" \
				f"<b> • Ваш bot_id: </b><code>{bot_id}</code>\n" \
				f"<b> • Ваша роль на данный момент: {smile} {role}</b>\n\n" \
				f"<b> • Ваш прогресс в боевом пропуске: {battlepass}</b>\n\n" \
				f"<b> • Выбранный язык приложения: {language}</b>\n\n"
				
	if photo.photos:
		# Берем текущую фотографию пользователя (первая в списке)
		photo_file_id = photo.photos[0][-1].file_id
		await bot.send_photo(chat_id=callback_query.chat.id, photo=photo_file_id, caption=caption, reply_markup=inline_keyboard)
	else:
		await bot.send_message(callback_query.chat.id, caption)

	await state.finish()

# Обработчик вкладки "Профиль после функций"
async def profile_end(callback_query: types.CallbackQuery, state: FSMContext):
	user = callback_query.from_user
	userlastname = user.first_name
	user_id = user.id
	username = f"@{user.username}" if user.username else None

	inline_keyboard = profile_menu()

	# Получаем информацию о пользователе
	user_data = check_user_data(user_id)
	role = user_data.get("role", "Uxknow")
	bot_id = user_data.get("bot_id", "Uxknow")
	language = user_data.get("language", "Uxknow")
	smile = user_data.get("smile", "Uxknow")
	battlepass = user_data.get("battlepass", "Uxknow")

	caption = f"<b>👩🏻‍🦰💬 Ваша текущая информация о профиле.</b>\n\n" \
				f"<b> • Ваше имя на текущий момент: {userlastname}</b>\n" \
				f"<b> • Ваше имя пользователя: {username}</b>\n" \
				f"<b> • Ваш user_id: </b><code>{user_id}</code>\n\n" \
				f"<b> • Ваш bot_id: </b><code>{bot_id}</code>\n" \
				f"<b> • Ваша роль на данный момент: {smile} {role}</b>\n\n" \
				f"<b> • Ваш прогресс в боевом пропуске: {battlepass}</b>\n\n" \
				f"<b> • Выбранный язык приложения: {language}</b>\n\n"
				
	await bot.edit_message_caption(caption=caption, chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)
				
	await state.finish()

# Обработчик кнопки "Вернуться назад"
@dp.callback_query_handler(lambda c: c.data == 'back_profile')
async def back_p(callback_query: types.CallbackQuery, state: FSMContext):
	await profile_end(callback_query, state)