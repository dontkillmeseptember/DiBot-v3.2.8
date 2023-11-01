from misc.util import types, logging
from misc.loader import dp, bot

from data.admin_db import is_admin_in_data, load_admin_data
from data.basket_db import load_basket_data, save_basket_data

# Функция для обработки команды /add_bs
@dp.message_handler(commands=['add_bs'])
async def add_bs_command(message: types.Message):
	"""Проверяет есть ли пользователь в базе админов"""
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		"""Разбиваем текст на аргументы"""
		args = message.get_args().split()

		if len(args) < 4:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/add_bs</code> [Артикул] [URL Фото] [URL Сайта] [Сообщение]</b>")
			return
		else:
			try:
				"""Переменные для базы данных"""
				bs_data = load_basket_data()

				"""Передаем в переменные аргументы из текста"""
				art = args[0]
				URL_photo = args[1]
				URL_site = args[2]
				price = args[3]
				message_t = args[4]
				message_admin = " ".join(args[5:])

				"""Сохраняем данные в базе данных"""
				bs_data[art] = {
					"URL_PHOTO": URL_photo,
					"URL_SITE": URL_site,
					"PRICE": int(price),
					"NAME": message_t,
					"Message_text": message_admin
				}
				save_basket_data(bs_data)

				"""Форматируем цену"""
				price_int = int(price)
				formatted_price = "{:,}".format(price_int).replace(',', ' ')

				message_text = f"👩🏻‍🦰💬 <b>Товар успешно добавлен в корзину.</b>\n\n" \
							   f"<b>• </b><b>Информация о товаре:</b>\n" \
							   f"<b>↳ </b><b>Артикул: <code>{art}</code></b>\n" \
							   f"<b>↳ </b><b>Сайт товара:</b> <a href='{URL_site}'>Ссылка</a>\n" \
							   f"<b>↳ </b><b>Краткое сообщение: {message_t}</b>\n\n" \
							   f"<b>Цена товара: 💶 {formatted_price} </b>₽\n\n" \
							   f"<b>💬 Текст товара: {message_admin}</b>"
				
				"""Выводим сообщение что все успешно произошло"""
				await bot.send_photo(chat_id=message.chat.id, photo=f"{URL_photo}", caption=message_text)

			except Exception:
				logging.exception("ERROR: 404 - BASKET: FUNC - ADD_BS_COMMAND")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /del_bs
@dp.message_handler(commands=['del_bs'])
async def del_bs_command(message: types.Message):
	"""Проверяет есть ли пользователь в базе админов"""
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		"""Разбиваем текст на аргументы"""
		args = message.get_args().split()

		if len(args) != 1:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/del_bs</code> [Артикул]</b>")
			return
		else:
			try:
				"""Переменные для базы данных"""
				bs_data = load_basket_data()

				"""Передаем в переменные аргументы из текста"""
				art = args[0]

				"""Сравниваем артикул который ввели и в базе данных"""
				if art in bs_data:
					del bs_data[art]

					save_basket_data(bs_data)
					
					await message.answer(f"👩🏻‍🦰💬 <b>Артикул удален из списка • <code>{art}</code></b>")
				else:
					await message.answer(f"👩🏻‍🦰💬 <b>Артикул не найден в списке • <code>{art}</code></b>")

			except Exception:
				logging.exception("ERROR: 404 - BASKET: FUNC - DEL_BS_COMMAND")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /ct_bs
@dp.message_handler(commands=['ct_bs'])
async def ct_bs_command(message: types.Message):
	"""Проверяет есть ли пользователь в базе админов"""
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		"""Загружаем данные о товарах из JSON файла"""
		bs_data = load_basket_data()

		try:
			if not bs_data:
				await message.answer("👩🏻‍🦰💬 <b>Корзина пуста.</b>")

			else:
				result_message = "👩🏻‍🦰💬 <b>Товары в корзине:</b>\n\n"

				"""Делаем цикл который выводит нужную информацию о товарах"""
				for i, (art, item) in enumerate(bs_data.items(), start=1):

					message_text = item["NAME"]
					url_site_text = item["URL_SITE"]

					result_message += f"<b>{i} • [<code>{art}</code>] - {message_text} • </b><a href='{url_site_text}'>Ссылка</a>\n"

				await message.answer(result_message)

		except Exception:
			logging.exception("ERROR: 404 - BASKET: FUNC - CT_BS_COMMAND")
			
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")