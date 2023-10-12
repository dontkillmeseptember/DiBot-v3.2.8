from misc.util import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, types, State, StatesGroup, FSMContext, logging, asyncio, random
from misc.loader import dp, bot

from data.config import PASSWORD, PHOTO_START
from data.start_db import load_user_data, is_user_in_data, save_user_data
from data.version_db import get_bot_version

from data import yml_loader

from keyboards.main_menu import create_menu_keyboard

class RegistrationState(StatesGroup):
	waiting_for_password = State()
	waiting_for_language = State()

class LanguageState(StatesGroup):
	waiting_for_language = State()

# Обработчик /start
async def start_handler(message, bot: types.Message):
	# Создаем клавиатуру с кнопкой "Запустить бота"
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
	keyboard.add(KeyboardButton(yml_loader.start_bot_path["start"]["button_bot_run"]))
	
	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_START, caption=yml_loader.start_bot_path["start"]["bot_run_info"], reply_markup=keyboard)

# Обработчик "Запустить бота"
async def start_bot(message: types.Message):
	# Проверяем, является ли пользователь регистрирован
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Переменная для клавиатуры
		keyboard = create_menu_keyboard(message)
		await message.answer(yml_loader.start_bot_path["start"]["base_info"], reply_markup=keyboard)	
	else:
		await message.answer(yml_loader.start_bot_path["registor"]["registor_info"])

		await RegistrationState.waiting_for_password.set()

@dp.message_handler(state=RegistrationState.waiting_for_password)
async def process_password(message: types.Message, state: FSMContext):
	user = message.text

	if user == PASSWORD:
		user_id = message.from_user.id
		username = message.from_user.username

		user_role = yml_loader.start_bot_path["registor"]["user_role"]
		user_smile = yml_loader.start_bot_path["registor"]["smile_user"]

		user_data = load_user_data()

		version = get_bot_version()

		if not is_user_in_data(user_id, user_data):
			user_data[str(user_id)] = {"username": username, 
				  					   "role": user_role,
									   "smile": user_smile,
				  					   "fines": "0", 
				  					   "language": None,
									   "bot_id": None,
									   "interface_contract": None,
									   "version_bot": version,
									   "battlepass": "0/60",
									   "active_chapter": None}
			save_user_data(user_data)

			await message.answer(yml_loader.language_path["select_language"]["try_language"])

			# Ожидание ответа "да" или "нет" от пользователя
			await RegistrationState.waiting_for_language.set()
	else:
		await message.answer(yml_loader.admin_path["admin"]["error_password"])

# Добавляем новый обработчик для ожидания ответа "да" или "нет"
@dp.message_handler(lambda message: message.text.lower() in ["да", "нет"], state=RegistrationState.waiting_for_language)
async def language_decision(message: types.Message, state: FSMContext):
	user_answer = message.text.lower()

	# Проверяем, является ли пользователь регистрирован
	user_id = message.from_user.id
	user_data = load_user_data()

	version = get_bot_version()

	if user_answer == "нет":
		keyboard = create_menu_keyboard(message)
		
		# Генерация случайного 9-значного ID
		bot_id = ''.join(str(random.randint(0, 9)) for _ in range(9))

		text_select_none = f"<b>🧑🏻‍🦱💬 Вы успешно зарегистрированы!</b>\n" \
								"<b>     						↳ </b><b>Ваш уникальный bot_id: </b>" + f"<code>{bot_id}</code>\n" \
								"<b>     						↳ </b><b>Версия бота: </b>" + f"<code>{version}</code>"

		# Обновляем язык пользователя в user_data.json
		user_data[str(user_id)]["language"] = yml_loader.language_path["buttons_language"]["button_russian"]
		save_user_data(user_data)

		# Обновляем bot_id в user_data.json
		user_data[str(user_id)]["bot_id"] = bot_id
		save_user_data(user_data)
	
		await message.answer(text_select_none)
		
		await asyncio.sleep(5)

		await message.answer(yml_loader.start_bot_path["start"]["base_info"], reply_markup=keyboard)

		await state.finish()

	elif user_answer == "да":
		# Создаем inline клавиатуру с кнопкой выбора языка
		languages_keyboard = InlineKeyboardMarkup(row_width=2)
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

		await message.answer(yml_loader.language_path["select_language"]["language_info"], reply_markup=languages_keyboard)

		await LanguageState.waiting_for_language.set()

@dp.callback_query_handler(state=LanguageState.waiting_for_language)
async def select_language(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	languages = [yml_loader.language_path["buttons_language"]["button_russian"], yml_loader.language_path["buttons_language"]["button_english"], 
		   		 yml_loader.language_path["buttons_language"]["button_georgian"], yml_loader.language_path["buttons_language"]["button_ukranian"], 
				 yml_loader.language_path["buttons_language"]["button_spanish"], yml_loader.language_path["buttons_language"]["button_french"], 
				 yml_loader.language_path["buttons_language"]["button_german"], yml_loader.language_path["buttons_language"]["button_polish"]]

	try:
		chosen_language = callback_query.data

		if chosen_language in languages:
			keyboard = create_menu_keyboard()

			# Генерация случайного 9-значного ID
			bot_id = ''.join(str(random.randint(0, 9)) for _ in range(9))

			version = get_bot_version()

			text_select_language = f"<b>🧑🏻‍🦱💬 Вы успешно зарегистрированы!</b>\n" \
									"<b>     						↳ </b><b>Вы выбрали язык: </b>" + f"<b>{chosen_language}</b>\n" \
									"<b>     						↳ </b><b>Ваш уникальный bot_id: </b>" + f"<code>{bot_id}</code>\n" \
									"<b>     						↳ </b><b>Версия бота: </b>" + f"<code>{version}</code>"

			# Обновляем язык пользователя в user_data.json
			user_data[str(user_id)]["language"] = chosen_language
			save_user_data(user_data)

			# Обновляем bot_id в user_data.json
			user_data[str(user_id)]["bot_id"] = bot_id
			save_user_data(user_data)

			await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

			await bot.send_message(user_id, text_select_language)
		
			await asyncio.sleep(5)

			await bot.send_message(user_id, yml_loader.start_bot_path["start"]["base_info"], reply_markup=keyboard)

			await state.finish()

	except Exception:
		logging.exception("Ошибочка")
