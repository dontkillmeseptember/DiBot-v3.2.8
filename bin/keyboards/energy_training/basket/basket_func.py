from misc.util import types, InlineKeyboardMarkup, InlineKeyboardButton, State, StatesGroup, FSMContext, logging
from misc.loader import dp, bot

from data.basket_db import load_basket_data, check_basket_data

class SearchState(StatesGroup):
	waiting_search_bs = State()

# Обработчик функции для корзины товаров
async def basket_handler(message: types.Message, state: FSMContext):
	"""Создаем инлайкн клавиатуру для поиска"""
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton("🔍 Начать поиск товаров", callback_data="search"))

	"""Загружаем данные о товарах из JSON файла"""
	bs_data = load_basket_data()

	"""Текст для вкладки"""
	message_basket = f"<b>👩🏻‍🦰💬 Добро пожаловать во вкладку • 📁🥼 Корзина Товаров</b>\n\n" \
					 f"<b>В данный момент в корзине находится: 👜 {len(bs_data)} ШТ</b>\n\n" \
					 f"<b>Для поиска товаров, нажмите кнопку • 🔍 Начать поиск товаров</b>\n\n" \
					 f"<b>Мы готовы помочь вам с вашими покупками!</b>"

	await message.answer(message_basket, reply_markup=inline_keyboard)

	await state.finish()

# Обработчик кнопки "Начать поиск товаров"
@dp.callback_query_handler(lambda c: c.data == 'search')
async def search_handler(callback_query: types.CallbackQuery):
	"""Загружаем данные о товарах из JSON файла"""
	bs_data = load_basket_data()

	try:
		if not bs_data:
			await bot.edit_message_text("👩🏻‍🦰💬 <b>Ваша корзина товаров пуста.</b>", callback_query.from_user.id, callback_query.message.message_id)
		else:
			"""Переменная для кнопки"""
			inline_keyboard = InlineKeyboardMarkup()
			inline_keyboard.add(InlineKeyboardButton("❌ Отменить поиск товаров", callback_data="off_search"))

			result_message = "👩🏻‍🦰💬 <b>Ваша корзина товаров.</b>\n\n" \
							 "<b>Список товаров на данный момент:</b>\n\n"

			"""Делаем цикл который выводит нужную информацию о товарах"""
			for i, (art, item) in enumerate(bs_data.items(), start=1):

				message_text = item["NAME"]

				result_message += f"<b>{i} • [<code>{art}</code>] — {message_text}</b>\n"

			result_message += "\n<b>Для поиска товара из списка, введите артикул товара в поле поиска ниже.</b>"

			await bot.edit_message_text(result_message, callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

			await SearchState.waiting_search_bs.set()

	except Exception:
		logging.exception("ERROR: 404 - BASKET_FUNC: FUNC - SEARCH_HANDLER")

@dp.message_handler(state=SearchState.waiting_search_bs)
async def commodity(message: types.Message):
	"""Пользователь вводит артикул"""
	user_message_art = message.text

	"""Выводится из базы данных артикул"""
	bs_data = check_basket_data(user_message_art)
	bs_data_load = load_basket_data()

	if user_message_art in bs_data_load:
		"""Выводим данные из введеного артикула"""
		URL_ph = bs_data.get("URL_PHOTO")
		name_product = bs_data.get("NAME", "ERROR")
		message_product = bs_data.get("Message_text", "ERROR")
		url_site = bs_data.get("URL_SITE")
		price_product = bs_data.get("PRICE", "ERROR")

		"""Форматируем цену"""
		price_int = int(price_product)
		formatted_price = "{:,}".format(price_int).replace(',', ' ')

		"""Переменная для кнопки"""
		inline_keyboard = InlineKeyboardMarkup()
		inline_keyboard.add(InlineKeyboardButton("❌ Отменить поиск товаров", callback_data="off_search_two"))

		"""Информация о товаре"""
		message_text = f"<b>👩🏻‍🦰💬 Товар из корзины.</b>\n\n" \
					   f"<b><a href='{url_site}'>{name_product}</a> • {user_message_art}</b>\n\n" \
					   f"<b>💬 {message_product}</b>\n\n" \
					   f"<b>Цена товара: 💶 {formatted_price} </b>₽\n\n" \
					   f"<b>Если вам нужно найти еще один товар, вы можете ввести новый артикул и продолжить поиск.</b>"

		await bot.send_photo(chat_id=message.chat.id, photo=f"{URL_ph}", caption=message_text, reply_markup=inline_keyboard)
	else:
		await message.answer(f"👩🏻‍🦰💬 <b>Извините, но введенный вами артикул не соответствует нашей системе. Пожалуйста, убедитесь, что вы ввели правильный артикул, и попробуйте снова.</b>")

async def basket_handler_call(callback_query: types.CallbackQuery, state: FSMContext):
	"""Создаем инлайкн клавиатуру для поиска"""
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton("🔍 Начать поиск товаров", callback_data="search"))

	"""Загружаем данные о товарах из JSON файла"""
	bs_data = load_basket_data()

	"""Текст для вкладки"""
	message_basket = f"<b>👩🏻‍🦰💬 Добро пожаловать во вкладку • 📁🥼 Корзина Товаров</b>\n\n" \
					 f"<b>В данный момент в корзине находится: 👜 {len(bs_data)} ШТ</b>\n\n" \
					 f"<b>Для поиска товаров, нажмите кнопку • 🔍 Начать поиск товаров</b>\n\n" \
					 f"<b>Мы готовы помочь вам с вашими покупками!</b>"

	await bot.edit_message_text(message_basket, callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

	await state.finish()

async def basket_handler_message(callback_query: types.CallbackQuery, state: FSMContext):
	"""Создаем инлайкн клавиатуру для поиска"""
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton("🔍 Начать поиск товаров", callback_data="search"))

	"""Загружаем данные о товарах из JSON файла"""
	bs_data = load_basket_data()

	"""Текст для вкладки"""
	message_basket = f"<b>👩🏻‍🦰💬 Добро пожаловать во вкладку • 📁🥼 Корзина Товаров</b>\n\n" \
					 f"<b>В данный момент в корзине находится: 👜 {len(bs_data)} ШТ</b>\n\n" \
					 f"<b>Для поиска товаров, нажмите кнопку • 🔍 Начать поиск товаров</b>\n\n" \
					 f"<b>Мы готовы помочь вам с вашими покупками!</b>"

	await bot.send_message(callback_query.from_user.id, message_basket, reply_markup=inline_keyboard)

	await state.finish()

# Обработчик кнопки "Отменить поиск"
@dp.callback_query_handler(lambda c: c.data == 'off_search_two', state=SearchState.waiting_search_bs)
async def back_p_bs(callback_query: types.CallbackQuery, state: FSMContext):
	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

	await basket_handler_message(callback_query, state)

# Обработчик кнопки "Отменить поиск"
@dp.callback_query_handler(lambda c: c.data == 'off_search', state=SearchState.waiting_search_bs)
async def back_p_bs(callback_query: types.CallbackQuery, state: FSMContext):
	await basket_handler_call(callback_query, state)