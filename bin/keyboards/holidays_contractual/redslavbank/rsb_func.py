from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, State, StatesGroup, FSMContext, asyncio, random
from misc.loader import dp, bot

from data.rsb_db import load_rsb_data, is_rsb_in_data, save_rsb_data, check_rsb_data

from data.eth_db import (
	get_eth_wallet, 
	usd_formatted, 
	rub_formatted, 
	get_rub_to_usd_rate, 
	get_usd_to_rub_rate, 
	get_eth_to_rub_rate, 
	get_interest_walltet_igor, 
	get_interest_walltet_dinara, 
	calculate_interest, 
	calculate_interest_call, 
	interest_fines,
	interest_fines_call
)

from data.start_db import check_user_data

from datetime import datetime, timedelta

from data import yml_loader

class RegistrationState(StatesGroup):
	waiting_for_password_rsb = State()
	waiting_for_username_rsb = State()
	waiting_for_user_password_rsb = State()
	recovery_for_user_password_rsb = State()
	waiting_for_user_new_password_rsb = State()

class ChangeState(StatesGroup):
	change_for_username_rsb = State()
	change_for_password_rsb = State()
	waiting_remember_password_rsb = State()

# Обработчик функции для inline_keyboards
def office_menu():
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_settings"], callback_data="settings_rsb"))

	return inline_keyboard

# Обработчик личного кабинета пользователя
async def private_office(message: types.Message, state: FSMContext):
	user_id = message.from_user.id

	"""Выводим из базы данные пользователя"""
	rsb_data = check_rsb_data(user_id)
	user_data = check_user_data(user_id)
	eth = get_eth_wallet()
	eth_to_usd = usd_formatted()
	eth_to_rub = rub_formatted()
	rub = get_rub_to_usd_rate()
	usd = get_usd_to_rub_rate()
	eth_to_rub_rate = get_eth_to_rub_rate()
	interest_igor = get_interest_walltet_igor()
	interest_dinara = get_interest_walltet_dinara()
	interest_summ = calculate_interest(message)
	interest = interest_fines(message)
	fines = user_data.get("fines", "ERROR")
	fines_slava = user_data.get("fines_slava", "ERROR")

	"""Выводим из базы данных имя пользователя"""
	user_name_rsb = rsb_data.get("username_rsb", "Пользователь")
	number_card_rsb = rsb_data.get("usercard_rsb", "ERROR")

	"""Форматирование переменной fines с пробелами для разделения тысяч"""
	message_eth_to_rub_rate = eth_to_rub_rate

	formatted_usd = round(usd, 3)
	formatted_fines = "{:,}".format(fines).replace(',', ' ')
	formatted_fines_slava = "{:,}".format(fines_slava).replace(',', ' ')
	formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')
	formatted_eth_to_rub_rate = "{:,}".format(message_eth_to_rub_rate).replace(',', ' ')

	"""Отображения даты, месяца и года для платежа"""
	current_date = datetime.now()

	if current_date.day >= 26:
		current_date += timedelta(days=30)  # Добавляем 5 дней (для следующего месяца)
		if current_date.month == 13:  # Если текущий месяц стал 13, обновляем и год
			current_date = current_date.replace(month=1, year=current_date.year + 1)
	
	formatted_date = current_date.strftime("%d.%m.%y")

	inline_keyboard = office_menu()

	message_text = f"<b>👩🏻‍🦰💬 Добро пожаловать в вашу учетную запись, {user_name_rsb}.</b>\n\n" \
				   f"<b> • Ваш номер карты: 💳 <code>{number_card_rsb}</code></b>\n\n" \
				   f"<b> • Ваша общая сумма штрафов/долгов: 💷 {formatted_fines} </b>₽<b> ~ {formatted_fines_slava} </b>₽\n" \
				   f"<b> • Ваш общий бюджет: 💷 {eth} ETH — {eth_to_usd} $ ~ {eth_to_rub} </b>₽\n\n" \
				   f"<b> • Ваш вклад в %: 🧑🏻 {interest_igor}% ~ {interest_dinara}% 👩🏻‍🦰</b>\n\n" \
				   f"<b> • Текущий курс рубля: 💴 1 </b>₽<b> ~ {formatted_usd} $</b>\n" \
				   f"<b> • Текущий курс доллара: 💵 1 $ ~ {rub} </b>₽\n\n" \
				   f"<b> • Текущий курс ETH: 💶 1 ETH ~ {formatted_eth_to_rub_rate} </b>₽\n\n" \
				   f"<b> • Ваш минимальный платеж: 〽️ {interest}% ~ {formatted_interest_summ} </b>₽\n\n" \
				   f"<b>✠ Оплатить штраф до • {formatted_date}.</b>"

	await message.answer(message_text, reply_markup=inline_keyboard)

	await state.finish()

# Обработчик проверки зарегался пользователь в банк или нет
async def check_user_rsb(message: types.Message, state: FSMContext):
	"""Проверяем, является ли пользователь регистрирован"""
	user_id = message.from_user.id
	rsb_data = load_rsb_data()

	"""Получаем имя пользователя из сообщения отправленое им"""
	user = message.from_user
	userlastname = user.first_name

	"""
	Проверяется зарегистрирован пользователь через функцию is_rsb_in_data  
	Если пользователь не найден в базе данных, то он переводится на стадию регистрации
	"""
	if is_rsb_in_data(user_id, rsb_data):
		"""Выводит из базы данных информацию о пользователе, запомнил он пароль или нет"""
		user_data = check_rsb_data(user_id)
		user_remember_password_rsb = user_data.get("remember_password")

		try:
			if user_remember_password_rsb == True:
				await private_office(message, state)
			elif user_remember_password_rsb == False:
				user_data = check_rsb_data(user_id)
				user_name_rsb = user_data.get("username_rsb", "Пользователь")

				"""Определяем время суток в данный момент у пользователя"""
				import datetime
				now = datetime.datetime.now()
				current_hour = now.hour

				if 6 <= current_hour < 12:
					greeting = "Доброе утро"
					greeting_smile = "🌄"
				elif 12 <= current_hour < 18:
					greeting = "Добрый день"
					greeting_smile = "🏞"
				elif 18 <= current_hour < 24:
					greeting = "Добрый вечер"
					greeting_smile = "🌅"
				else:
					greeting = "Доброй ночи"
					greeting_smile = "🌌"

				await message.answer(f"<b>👩🏻‍🦰💬 {greeting}, {user_name_rsb} • {greeting_smile}\n\n</b>"
									"<b>Пожалуйста, введите ваш пароль для доступа к вашей учетной записи банка.</b>")

				"""Запрос на подтвеждение пароля пользователя когда он уже зарегистрировался в банке."""
				await RegistrationState.waiting_for_user_password_rsb.set()
		except Exception:
			await message.answer("<b>👩🏻‍🦰💬 Извините, но кажется, что приложение банка временно недоступно. Пожалуйста, подождите немного, мы работаем над устранением неполадок.\n\nМы приносим извинения за временные неудобства и постараемся восстановить доступ к сервису как можно скорее.\n\nСпасибо за ваше терпение. 🤍</b>")
	else:
		await message.answer(f"<b>👩🏻‍🦰💬 {userlastname} Добро пожаловать во вкладку • 📁💳 RedSlavBank\n\n</b>"
					   		 "<b>RedSlavBank — это ваш надежный партнер в мире финансов. Мы готовы предоставить вам широкий спектр банковских услуг и возможностей для достижения ваших финансовых целей.\n\n</b>"
							 "<b>Чтобы персонализировать наше обслуживание, пожалуйста, укажите ваше имя ниже, чтобы мы могли лучше удовлетворить ваши потребности.</b>")

		"""Запрос на ввода имени пользователя чтобы оно отображлось в информации."""
		await RegistrationState.waiting_for_username_rsb.set()

# Обаботчик ввода информации о пользователе
@dp.message_handler(state=RegistrationState.waiting_for_username_rsb)
async def create_user_name_rsb(message: types.Message):
	"""Пользователь вводит свое имя и как к нему обращаться"""
	user = message.text

	"""Переменные для сохранения данных"""
	user_id = message.from_user.id

	rsb_data = load_rsb_data()

	"""Проверка нету ли пользователя уже в базе данных"""
	if not is_rsb_in_data(user_id, rsb_data):
		"""Сохраняем имя пользователь в базу данных"""
		rsb_data[str(user_id)] = {
			"username_rsb": user,
			"userpassword_rsb": None,
			"usercard_rsb": None,
			"remember_password": False,
			"userchangepassword_rsb": False
		}
		save_rsb_data(rsb_data)

		await message.answer(f"<b>👩🏻‍🦰💬 Отлично, теперь введите пароль для доступа к вашему аккаунту в RedSlavBank.</b>\n\n" 
					   		  "<b>Пароль должен содержать не менее 8 символов и включать буквы и цифры для обеспечения безопасности вашей учетной записи.</b>")

		await RegistrationState.waiting_for_password_rsb.set()
	else:
		print("ERROR: 404 - RSB: FUNC - CREATE_USER_NAME_RSB")

# Обработчик ввода пароля пользователя
@dp.message_handler(state=RegistrationState.waiting_for_password_rsb)
async def create_user_password_rsb(message: types.Message, state: FSMContext):
	"""Пользователь вводит свой пароль для входа в банк"""
	user_password = message.text

	"""Пременные для сохранения данных"""
	user_id = message.from_user.id

	rsb_data = load_rsb_data()

	"""Проверяется есть ли пользователь уже в базе данных или нет"""
	if is_rsb_in_data(user_id, rsb_data):
		"""Пользователь должен ввести пароль не менее из 8 символов, иначе он получит оповещение, что пароль должен содержать не менее 8 симлов"""
		if len(user_password) < 8 or not any(char.isalpha() for char in user_password) or not any(char.isdigit() for char in user_password):
			await message.answer(f"<b>👩🏻‍🦰💬 Пароль должен содержать не менее 8 символов и включать буквы и цифры. Попробуйте еще раз.</b>")
		else:
			"""Генерируем номер каточки для пользователя"""
			card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])

			formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])

			"""Сохраняем пароль и номер карточки пользователя"""
			rsb_data[str(user_id)]["userpassword_rsb"] = user_password
			rsb_data[str(user_id)]["usercard_rsb"] = formatted_card_number
			save_rsb_data(rsb_data)

			"""Выводим из базы данных имя пользователя"""
			user_data = check_rsb_data(user_id)
			user_name_rsb = user_data.get("username_rsb", "Пользователь")

			"""Создаем инлайн клавиатуру для входа в учетную запись"""
			inline_keyboard = InlineKeyboardMarkup()
			inline_keyboard.add(InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_input_profille"], callback_data="back_profile_rsb"))

			await message.answer(f"<b>👩🏻‍🦰💬 {user_name_rsb}, Прекрасно! Ваш аккаунт успешно создан. Теперь вы можете воспользоваться всеми услугами RedSlavBank и следить за своими финансами.</b>\n\n"
								  "<b>❕ Не забудьте сохранить свой пароль в надежном месте и обращаться к нему осторожно, чтобы обеспечить безопасность вашей учетной записи. Добро пожаловать в RedSlavBank!</b>", reply_markup=inline_keyboard)

			await state.finish()

	else:
		print("ERROR: 404 - RSB: FUNC - CREATE_USER_PASSWORD_RSB")

# Обработчик для входа в банк
@dp.message_handler(state=RegistrationState.waiting_for_user_password_rsb)
async def create_user_password_rsb(message: types.Message, state: FSMContext):
	"""Выводим из базы данных пароль пользователя"""
	user_id = message.from_user.id
	user_data = check_rsb_data(user_id)
	user_password_rsb = user_data.get("userpassword_rsb")

	"""Пользователь вводит свой пароль для входа в банк"""
	user_password = message.text

	"""Сравниваем пароли"""
	if user_password == user_password_rsb:
		await private_office(message, state)

		await state.finish()
	else:
		"""Создаем инлайн клавиатуру с кнопкой запроса для восстановления пароля"""
		inline_keyboard = InlineKeyboardMarkup()
		inline_keyboard.add(InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_recovery_password"], callback_data="recovery_password"))

		await message.answer("<b>👩🏻‍🦰💬 Извините, но введенный вами пароль неверен. Пожалуйста, попробуйте снова.</b>\n\n" 
					   		 "<b>❕ Если вы забыли свой пароль, вы можете воспользоваться функцией восстановления пароля.</b>", reply_markup=inline_keyboard)

		await state.finish()

# Обаботчик для восстановления пароля
@dp.callback_query_handler(lambda c: c.data == 'recovery_password')
async def start_recovery_user_password(callback_query: types.CallbackQuery):
	await bot.edit_message_text("<b>👩🏻‍🦰💬 Для восстановления пароля, введите ваш user_id.</b>", callback_query.from_user.id, callback_query.message.message_id)

	await RegistrationState.recovery_for_user_password_rsb.set()

@dp.message_handler(state=RegistrationState.recovery_for_user_password_rsb)
async def recovery_user_password(message: types.Message):
	"""Берем user_id из базы данных и сраниваем его с введенем user_id пользователем"""
	user_id = message.text
	rsb_data = load_rsb_data()

	if user_id in rsb_data:
		await message.answer("<b>👩🏻‍🦰💬 Пожалуйста, введите новый пароль.\n\n❕ Новый пароль должен содержать не менее 8 символов и включать буквы и цифры для обеспечения безопасности вашей учетной записи.</b>")

		await RegistrationState.waiting_for_user_new_password_rsb.set()
	else:
		await message.answer("<b>👩🏻‍🦰💬 Извините, но введенный вами user_id не соответствует нашей системе. Пожалуйста, убедитесь, что вы ввели правильный идентификатор пользователя, и попробуйте снова.</b>")

@dp.message_handler(state=RegistrationState.waiting_for_user_new_password_rsb)
async def recovery_user_new_password(message: types.Message, state: FSMContext):
	"""Пользователь вводит новый пароль для входа в банк"""
	user_new_password = message.text

	"""Пременные для сохранения данных"""
	user_id = message.from_user.id

	rsb_data = load_rsb_data()

	"""Пользователь должен ввести пароль не менее из 8 символов, иначе он получит оповещение, что пароль должен содержать не менее 8 симлов"""
	if len(user_new_password) < 8 or not any(char.isalpha() for char in user_new_password) or not any(char.isdigit() for char in user_new_password):
		await message.answer(f"<b>👩🏻‍🦰💬 Пароль должен содержать не менее 8 символов и включать буквы и цифры. Попробуйте еще раз.</b>")
	else:
		"""Сохраняем пароль и номер карточки пользователя"""
		rsb_data[str(user_id)]["userpassword_rsb"] = user_new_password
		save_rsb_data(rsb_data)

		"""Выводим из базы данных имя пользователя"""
		user_data = check_rsb_data(user_id)
		user_name_rsb = user_data.get("username_rsb", "Пользователь")

		"""Выводим из базы данных фазу пользователя"""
		phase_change_password = user_data.get("userchangepassword_rsb")

		await message.answer(f"<b>👩🏻‍🦰💬 {user_name_rsb}, Отлично! Ваш пароль успешно изменен.</b>\n\n"
					   		  "<b>Теперь вы можете использовать новый пароль для входа в свою учетную запись. Пожалуйста, сохраните его в надежном месте и обращайтесь к нему осторожно, чтобы обеспечить безопасность вашего аккаунта.</b>")
		
		await asyncio.sleep(2)

		"""Проверка какая фаза у пользователя в данный момент"""
		if phase_change_password == True:
			rsb_data[str(user_id)]["userchangepassword_rsb"] = False
			rsb_data[str(user_id)]["remember_password"] = False
			save_rsb_data(rsb_data)

			await private_office(message, state)
		elif phase_change_password == False:
			rsb_data[str(user_id)]["remember_password"] = False
			save_rsb_data(rsb_data)

			await check_user_rsb(message)

# Обработчик меню настроик банка
@dp.callback_query_handler(lambda c: c.data == 'settings_rsb')
async def menu_settings_rsb(callback_query: types.CallbackQuery):
	"""Выводит из базы данных информацию о пользователе, запомнил он пароль или нет"""
	user = callback_query.from_user
	user_id = user.id

	user_data = check_rsb_data(user_id)
	user_remember_password_rsb = user_data.get("remember_password")

	if user_remember_password_rsb == True:
		"""Создаем инлайн клавиатуру с кнопками выбора для пользователя"""
		inline_keyboard = InlineKeyboardMarkup()
		inline_keyboard.row(
			InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_password"], callback_data="change_password_rsb"),
			InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_off_remember_password"], callback_data="off_remember_password_rsb")
		)
		inline_keyboard.add(InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_name"], callback_data="change_name_rsb"))
		inline_keyboard.add(InlineKeyboardButton(yml_loader.language_path["language"]["button_back"], callback_data="back_profile_rsb"))

		await bot.edit_message_text(yml_loader.fines_data["rsb"]["settings_info"], callback_query.message.chat.id, callback_query.message.message_id, reply_markup=inline_keyboard)

	elif user_remember_password_rsb == False:
		"""Создаем инлайн клавиатуру с кнопками выбора для пользователя"""
		inline_keyboard = InlineKeyboardMarkup()
		inline_keyboard.row(
			InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_password"], callback_data="change_password_rsb"),
			InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_remember_password"], callback_data="remember_password_rsb")
		)
		inline_keyboard.add(InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_name"], callback_data="change_name_rsb"))
		inline_keyboard.add(InlineKeyboardButton(yml_loader.language_path["language"]["button_back"], callback_data="back_profile_rsb"))

		await bot.edit_message_text(yml_loader.fines_data["rsb"]["settings_info"], callback_query.message.chat.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для забывания пароля
@dp.callback_query_handler(lambda c: c.data == 'off_remember_password_rsb')
async def remember_password_rsb(callback_query: types.CallbackQuery):
	await bot.edit_message_text("<b>👩🏻‍🦰💬 Для отключения функции запоминания пароля и возврата к вводу пароля при каждом входе, вам необходимо подтвердить свою личность.\n\nПожалуйста, введите ваш текущий пароль, чтобы выполнить это действие и вернуться к вводу пароля при входе.</b>", callback_query.from_user.id, callback_query.message.message_id)

	await ChangeState.waiting_remember_password_rsb.set()

# Обработчик для запоминания пароля
@dp.callback_query_handler(lambda c: c.data == 'remember_password_rsb')
async def remember_password_rsb(callback_query: types.CallbackQuery):
	await bot.edit_message_text("<b>👩🏻‍🦰💬 Для удобства входа, пожалуйста, введите ваш текущий пароль.</b>", callback_query.from_user.id, callback_query.message.message_id)

	await ChangeState.waiting_remember_password_rsb.set()

@dp.message_handler(state=ChangeState.waiting_remember_password_rsb)
async def remember_uses_password(message: types.Message, state: FSMContext):
	"""Пользователь вводит свой текущий пароль"""
	user_message_password = message.text
	user_id = message.from_user.id

	"""Выводим пароль из базы данных для проверки пароля"""
	user_data = check_rsb_data(user_id)
	user_password_rsb = user_data.get("userpassword_rsb")

	if user_message_password in user_password_rsb:
		"""Выводит из базы данных информацию о пользователе, запомнил он пароль или нет"""
		user_data = check_rsb_data(user_id)
		user_remember_password_rsb = user_data.get("remember_password")

		if user_remember_password_rsb == True:
			"""Сохраняем что пользователь включил эту фукнцию"""
			rsb_data = load_rsb_data()

			rsb_data[str(user_id)]["remember_password"] = False
			save_rsb_data(rsb_data)

			await message.answer("<b>👩🏻‍🦰💬 Функция запоминания пароля успешно отключена. Теперь при входе в аккаунт вам будет необходимо вводить пароль каждый раз.\n\nЕсли вы в будущем захотите снова воспользоваться этой функцией, вы сможете активировать её в настройках вашей учетной записи.</b>")

			await asyncio.sleep(2)

			await private_office(message, state)

		elif user_remember_password_rsb == False:
			"""Сохраняем что пользователь включил эту фукнцию"""
			rsb_data = load_rsb_data()

			rsb_data[str(user_id)]["remember_password"] = True
			save_rsb_data(rsb_data)

			await message.answer("<b>👩🏻‍🦰💬 Отлично! Ваш пароль успешно запомнен, и вам больше не придется вводить его при входе в аккаунт.</b>")

			await asyncio.sleep(2)

			await private_office(message, state)
	else:
		await message.answer("<b>👩🏻‍🦰💬 Извините, но введенный вами пароль не соответствует нашей системе. Пожалуйста, убедитесь, что вы ввели правильный пароль, и попробуйте снова.</b>")

# Обработчик смена имени для пользователя
@dp.callback_query_handler(lambda c: c.data == 'change_name_rsb')
async def change_name_rsb(callback_query: types.CallbackQuery):
	await bot.edit_message_text("<b>👩🏻‍🦰💬 Пожалуйста, введите новое имя пользователя, которое вы хотели бы использовать.</b>", callback_query.from_user.id, callback_query.message.message_id)

	await ChangeState.change_for_username_rsb.set()

@dp.message_handler(state=ChangeState.change_for_username_rsb)
async def change_uses_name(message: types.Message, state: FSMContext):
	"""Пользователь вводит свое новое имя пользователя"""
	user_message_name = message.text
	user_id = message.from_user.id

	"""Сохраняем в базу данных новое имя пользователя"""
	rsb_data = load_rsb_data()

	rsb_data[str(user_id)]["username_rsb"] = user_message_name
	save_rsb_data(rsb_data)

	await message.answer(f"<b>👩🏻‍🦰💬 Ваше имя успешно изменено. Теперь ваш аккаунт будет отображаться • {user_message_name}.</b>")

	await asyncio.sleep(2)

	await private_office(message, state)

# Обработчик смена пароля для пользователя
@dp.callback_query_handler(lambda c: c.data == 'change_password_rsb')
async def change_password_rsb(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру для восстановления пароля"""
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.fines_data["rsb"]["button_recovery_password"], callback_data="recovery_password"))

	await bot.edit_message_text("<b>👩🏻‍🦰💬 Для смена пароля, введите ваш старый пароль.</b>\n\n"
							 	"<b>❕ Если вы забыли свой пароль, вы можете воспользоваться функцией восстановления пароля.</b>", callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

	await ChangeState.change_for_password_rsb.set()

@dp.message_handler(state=ChangeState.change_for_password_rsb)
async def change_user_password(message: types.Message):
	"""Пользователь вводит старый пароль и идет сравнение"""
	user_message_password = message.text
	user_id = message.from_user.id

	rsb_data = check_rsb_data(user_id)
	old_user_password = rsb_data.get("userpassword_rsb")

	if user_message_password in old_user_password:
		"""Вводит триггер для следующей функции, чтобы та проверяла в какой фазе пользователь находится"""
		rsb_data = load_rsb_data()

		rsb_data[str(user_id)]["userchangepassword_rsb"] = True
		save_rsb_data(rsb_data)

		await message.answer("<b>👩🏻‍🦰💬 Пожалуйста, введите новый пароль.\n\n❕ Новый пароль должен содержать не менее 8 символов и включать буквы и цифры для обеспечения безопасности вашей учетной записи.</b>")

		await RegistrationState.waiting_for_user_new_password_rsb.set()
	else:
		await message.answer("<b>👩🏻‍🦰💬 Извините, но введенный вами пароль не соответствует нашей системе. Пожалуйста, убедитесь, что вы ввели правильный пароль, и попробуйте снова.</b>")

# Обработчик личного кабинета пользователя
async def profile_rsb(callback_query: types.CallbackQuery, state: FSMContext):
	user = callback_query.from_user
	user_id = user.id

	"""Выводим из базы данные пользователя"""
	rsb_data = check_rsb_data(user_id)
	user_data = check_user_data(user_id)
	eth = get_eth_wallet()
	eth_to_usd = usd_formatted()
	eth_to_rub = rub_formatted()
	rub = get_rub_to_usd_rate()
	usd = get_usd_to_rub_rate()
	eth_to_rub_rate = get_eth_to_rub_rate()
	interest_igor = get_interest_walltet_igor()
	interest_dinara = get_interest_walltet_dinara()
	interest_summ = calculate_interest_call(callback_query)
	interest = interest_fines_call(callback_query)
	fines = user_data.get("fines", "ERROR")
	fines_slava = user_data.get("fines_slava", "ERROR")

	"""Выводим из базы данных имя пользователя"""
	user_name_rsb = rsb_data.get("username_rsb", "Пользователь")
	number_card_rsb = rsb_data.get("usercard_rsb", "ERROR")

	"""Форматирование переменной fines с пробелами для разделения тысяч"""
	message_eth_to_rub_rate = eth_to_rub_rate

	formatted_usd = round(usd, 3)
	formatted_fines = "{:,}".format(fines).replace(',', ' ')
	formatted_fines_slava = "{:,}".format(fines_slava).replace(',', ' ')
	formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')
	formatted_eth_to_rub_rate = "{:,}".format(message_eth_to_rub_rate).replace(',', ' ')

	"""Отображения даты, месяца и года для платежа"""
	current_date = datetime.now()

	if current_date.day >= 26:
		current_date += timedelta(days=30)  # Добавляем 5 дней (для следующего месяца)
		if current_date.month == 13:  # Если текущий месяц стал 13, обновляем и год
			current_date = current_date.replace(month=1, year=current_date.year + 1)
	
	formatted_date = current_date.strftime("%d.%m.%y")

	inline_keyboard = office_menu()

	message_text = f"<b>👩🏻‍🦰💬 Добро пожаловать в вашу учетную запись, {user_name_rsb}.</b>\n\n" \
				   f"<b> • Ваш номер карты: 💳 <code>{number_card_rsb}</code></b>\n\n" \
				   f"<b> • Ваша общая сумма штрафов/долгов: 💷 {formatted_fines} </b>₽<b> ~ {formatted_fines_slava} </b>₽\n" \
				   f"<b> • Ваш общий бюджет: 💷 {eth} ETH — {eth_to_usd} $ ~ {eth_to_rub} </b>₽\n\n" \
				   f"<b> • Ваш вклад в %: 🧑🏻 {interest_igor}% ~ {interest_dinara}% 👩🏻‍🦰</b>\n\n" \
				   f"<b> • Текущий курс рубля: 💴 1 </b>₽<b> ~ {formatted_usd} $</b>\n" \
				   f"<b> • Текущий курс доллара: 💵 1 $ ~ {rub} </b>₽\n\n" \
				   f"<b> • Текущий курс ETH: 💶 1 ETH ~ {formatted_eth_to_rub_rate} </b>₽\n\n" \
				   f"<b> • Ваш минимальный платеж: 〽️ {interest}% ~ {formatted_interest_summ} </b>₽\n\n" \
				   f"<b>✠ Оплатить штраф до • {formatted_date}.</b>"

	await bot.edit_message_text(message_text, chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

	await state.finish()

# Обработчик кнопки "Вернуться назад"
@dp.callback_query_handler(lambda c: c.data == 'back_profile_rsb')
async def back_p_rsb(callback_query: types.CallbackQuery, state: FSMContext):
	await profile_rsb(callback_query, state)