from misc.util import types
from misc.loader import dp, bot

from data.start_db import load_user_data, save_user_data
from data.admin_db import is_admin_in_data, load_admin_data
from data.eth_db import load_eth_data, save_eth_data, get_eth_wallet, get_eth_to_rub_rate

# Функция для обработки команды /up_fines
@dp.message_handler(commands=['up_fines'])
async def add_fines_command(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()
		
		if len(args) != 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/up_fines</code> [user_id] [сумма]</b>")
			return
		else:
			user_id = args[0]
			amount = args[1]
			
			# Проверяем, есть ли такой пользователь в данных
			user_data = load_user_data()
			if user_id not in user_data:
				await message.answer(f"👩🏻‍🦰💬 <b>Пользователь • <code>{user_id}</code> не найден.</b>")
				return
			else:	
				# Обновляем сумму штрафов пользователя
				user_data[user_id]["fines"] = int(amount)
				save_user_data(user_data)
				
				# Форматирование переменной fines с пробелами для разделения тысяч
				message_amount = int(amount)

				formatted_amount = "{:,}".format(message_amount).replace(',', ' ')

				# Получаем имя пользователя
				user = user_data[user_id]
				user_name = user.get("userlastname", "Пользователь")

				# Уведомляем пользователя о штрафе
				await bot.send_message(user_id, f"👩🏻‍🦰💬 <b>Здравствуйте, {user_name}! Сумма ваших штрафов была увеличена.</b>\n\n" \
												"<b>• Краткая информация о штрафах:</b>\n" \
												f"<b>↳ </b><b>Сумма штрафов увеличена на • 💷 {formatted_amount} </b>₽\n" \
												f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_amount} </b>₽")

				await message.answer(f"👩🏻‍🦰💬 <b>Сумма штрафов для пользователя {user_name} обновлена.</b>\n\n"
									"<b>• Краткая информация о штрафах:</b>\n" \
									f"<b>↳ </b><b>Сумма штрафов увеличена на • 💷 {formatted_amount} </b>₽\n" \
									f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_amount} </b>₽")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /add_fines
@dp.message_handler(commands=['add_fines'])
async def add_fines(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()
		
		if len(args) < 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/add_fines</code> [user_id] [сумма] [сообщение]</b>")
			return
		else:
			user_id = args[0]
			amount = args[1]
			
			# Проверяем, есть ли такой пользователь в данных
			user_data = load_user_data()
			if user_id not in user_data:
				await message.answer(f"👩🏻‍🦰💬 <b>Пользователь • <code>{user_id}</code> не найден.</b>")
				return
			else:
				# Получаем сообщение из аргументов
				message_text = " ".join(args[2:])

				# Прибавляем сумму к текущему значению штрафов пользователя
				current_fines = int(user_data[user_id].get("fines", 0))
				updated_fines = current_fines + int(amount)
				user_data[user_id]["fines"] = updated_fines
				save_user_data(user_data)

				# Форматирование переменной fines с пробелами для разделения тысяч
				message_amount = int(amount)
				message_updated_fines = int(updated_fines)

				formatted_amount = "{:,}".format(message_amount).replace(',', ' ')
				formatted_updated_fines = "{:,}".format(message_updated_fines).replace(',', ' ')

				# Получаем имя пользователя
				user = user_data[user_id]
				user_name = user.get("userlastname", "Пользователь")

				# Уведомляем пользователя о штрафе
				await bot.send_message(user_id, f"👩🏻‍🦰💬 <b>Здравствуйте, {user_name}! Сумма ваших штрафов была увеличена.</b>\n\n" \
												"<b>• Краткая информация о штрафах:</b>\n" \
												f"<b>↳ </b><b>Сумма штрафов увеличена на • 💷 {formatted_amount} </b>₽\n" \
												f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
												f"💬 <b>Сообщение от администрации: {message_text}.</b>")
				
				await message.answer(f"👩🏻‍🦰💬 <b>Сумма штрафов для пользователя {user_name} обновлена.</b>\n\n"
									"<b>• Краткая информация о штрафах:</b>\n" \
									f"<b>↳ </b><b>Сумма штрафов увеличена на • 💷 {formatted_amount} </b>₽\n" \
									f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
									f"💬 <b>Отправленое сообщение: {message_text}.</b>")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /aw_fines
@dp.message_handler(commands=['aw_fines'])
async def aw_fines(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()
		
		if len(args) < 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/aw_fines</code> [user_id] [сумма] [сообщение]</b>")
			return
		else:
			user_id = args[0]
			amount = args[1]
			
			# Проверяем, есть ли такой пользователь в данных
			user_data = load_user_data()
			eth_data = load_eth_data()

			if user_id not in user_data:
				await message.answer(f"👩🏻‍🦰💬 <b>Пользователь • <code>{user_id}</code> не найден.</b>")
				return
			else:
				# Получаем текущую сумму штрафов пользователя
				current_fines = int(user_data[user_id].get("fines", 0))

				# Получаем имя пользователя
				user = user_data[user_id]
				user_name = user.get("userlastname", "Пользователь")

				# Проверяем, что отнимаемая сумма не больше текущей суммы штрафов
				if int(amount) > current_fines:
					await message.answer(f"👩🏻‍🦰💬 <b>Сумма для уменьшения больше текущей суммы штрафов пользователя {user_name}.</b>")
					return
				else:
					# Получаем сообщение из аргументов
					message_text = " ".join(args[2:])

					# Вычитаем сумму из текущих штрафов пользователя
					updated_fines = current_fines - int(amount)
					user_data[user_id]["fines"] = updated_fines
					save_user_data(user_data)

					# Вычитаем сумму ETH из текущего числа
					eth_to_rub_rate = get_eth_to_rub_rate()
					amount_in_eth = int(amount) / eth_to_rub_rate

					formatted_amount_in_eth = round(amount_in_eth, 3)

					# Обновляем JSON файл с ETH
					eth_wallet = get_eth_wallet()
					eth_wallet += formatted_amount_in_eth
					eth_data["wallet"]["eth"] = eth_wallet
					save_eth_data(eth_data)

					# Форматирование переменной fines с пробелами для разделения тысяч
					message_updated_fines = int(updated_fines)
					message_amount = int(amount)
					
					formatted_amount = "{:,}".format(message_amount).replace(',', ' ')
					formatted_updated_fines = "{:,}".format(message_updated_fines).replace(',', ' ')

					# Уведомляем пользователя о штрафе
					await bot.send_message(user_id, f"👩🏻‍🦰💬 <b>Здравствуйте, {user_name}! Сумма ваших штрафов была уменьшена.</b>\n\n" \
													"<b>• Краткая информация о штрафах:</b>\n" \
													f"<b>↳ </b><b>Сумма штрафов уменьшена на • 💷 {formatted_amount} </b>₽\n" \
													f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
													f"💬 <b>Сообщение от администрации: {message_text}.</b>")
					
					await message.answer(f"👩🏻‍🦰💬 <b>Сумма штрафов для пользователя {user_name} обновлена.</b>\n\n"
										"<b>• Краткая информация о штрафах:</b>\n" \
										f"<b>↳ </b><b>Сумма штрафов уменьшена на • 💷 {formatted_amount} </b>₽\n" \
										f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
										f"💬 <b>Отправленое сообщение: {message_text}.</b>")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /add_eth
@dp.message_handler(commands=['add_eth'])
async def add_eth(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()

		if len(args) != 1:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/add_eth</code> [сумма]</b>")
			return
		else:
			amount = args[0]

			# Проверяем, есть ли такой пользователь в данных
			eth_data = load_eth_data()
		
			# Вычитаем сумму ETH из текущего числа
			eth_to_rub_rate = get_eth_to_rub_rate()
			amount_in_eth = int(amount) / eth_to_rub_rate

			message_eth_to_rub_rate = eth_to_rub_rate			

			formatted_amount_in_eth = round(amount_in_eth, 3)
			formatted_eth_to_rub_rate = "{:,}".format(message_eth_to_rub_rate).replace(',', ' ')

			# Обновляем JSON файл с ETH
			eth_wallet = get_eth_wallet()
			eth_wallet += formatted_amount_in_eth
			eth_data["wallet"]["eth"] = eth_wallet
			save_eth_data(eth_data)

			await message.answer(f"👩🏻‍🦰💬 <b>Сумма ETH обновлена по курсу 1 ETH ~ {formatted_eth_to_rub_rate} </b>₽\n\n"
						 	 	"<b>• Краткая информация о ETH:</b>\n" \
							 	f"<b>↳ </b><b>Сумма ETH увеличена на • 💷 {formatted_amount_in_eth} ETH</b>\n" \
							 	f"<b>↳ </b><b>Текущая сумма ETH • 💷 {eth_wallet} ETH</b>\n")

	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /aw_eth
@dp.message_handler(commands=['aw_eth'])
async def aw_eth(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()

		if len(args) != 1:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/aw_eth</code> [сумма]</b>")
			return
		else:
			amount = args[0]

			# Проверяем, есть ли такой пользователь в данных
			eth_data = load_eth_data()
		
			# Вычитаем сумму ETH из текущего числа
			eth_to_rub_rate = get_eth_to_rub_rate()
			amount_in_eth = int(amount) / eth_to_rub_rate

			message_eth_to_rub_rate = eth_to_rub_rate			

			formatted_amount_in_eth = round(amount_in_eth, 3)
			formatted_eth_to_rub_rate = "{:,}".format(message_eth_to_rub_rate).replace(',', ' ')

			# Обновляем JSON файл с ETH
			eth_wallet = get_eth_wallet()
			eth_wallet -= formatted_amount_in_eth
			eth_data["wallet"]["eth"] = eth_wallet
			save_eth_data(eth_data)

			await message.answer(f"👩🏻‍🦰💬 <b>Сумма ETH обновлена по курсу 1 ETH ~ {formatted_eth_to_rub_rate} </b>₽\n\n"
						 	 	"<b>• Краткая информация о ETH:</b>\n" \
							 	f"<b>↳ </b><b>Сумма ETH уменьшена на • 💷 {formatted_amount_in_eth} ETH</b>\n" \
							 	f"<b>↳ </b><b>Текущая сумма ETH • 💷 {eth_wallet} ETH</b>\n")

	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /add_int
@dp.message_handler(commands=['add_int'])
async def add_int(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()

		if len(args) != 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/add_int</code> [сумма процентов игоря] [сумма процентов динары]</b>")
			return
		else:
			amount_igor = args[0]
			amount_dinara = args[1]

			# Проверяем, есть ли такой пользователь в данных
			eth_data = load_eth_data()
			eth_data["interest_wallet"]["interest_igor"] = int(amount_igor)
			eth_data["interest_wallet"]["interest_dinara"] = int(amount_dinara)
			save_eth_data(eth_data)

			await message.answer(f"<b>👩🏻‍🦰💬 Проценты обновлены • 🧑🏻 {amount_igor}% ~ {amount_dinara}% 👩🏻‍🦰</b>")

	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /aw_fines
@dp.message_handler(commands=['aw_fines'])
async def aw_fines(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()
		
		if len(args) < 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/aw_fines</code> [user_id] [сумма] [сообщение]</b>")
			return
		else:
			user_id = args[0]
			amount = args[1]
			
			# Проверяем, есть ли такой пользователь в данных
			user_data = load_user_data()
			eth_data = load_eth_data()

			if user_id not in user_data:
				await message.answer(f"👩🏻‍🦰💬 <b>Пользователь • <code>{user_id}</code> не найден.</b>")
				return
			else:
				# Получаем текущую сумму штрафов пользователя
				current_fines = int(user_data[user_id].get("fines", 0))

				# Получаем имя пользователя
				user = user_data[user_id]
				user_name = user.get("userlastname", "Пользователь")

				# Проверяем, что отнимаемая сумма не больше текущей суммы штрафов
				if int(amount) > current_fines:
					await message.answer(f"👩🏻‍🦰💬 <b>Сумма для уменьшения больше текущей суммы штрафов пользователя {user_name}.</b>")
					return
				else:
					# Получаем сообщение из аргументов
					message_text = " ".join(args[2:])

					# Вычитаем сумму из текущих штрафов пользователя
					updated_fines = current_fines - int(amount)
					user_data[user_id]["fines"] = updated_fines
					save_user_data(user_data)

					# Вычитаем сумму ETH из текущего числа
					eth_to_rub_rate = get_eth_to_rub_rate()
					amount_in_eth = int(amount) / eth_to_rub_rate

					formatted_amount_in_eth = round(amount_in_eth, 3)

					# Обновляем JSON файл с ETH
					eth_wallet = get_eth_wallet()
					eth_wallet += formatted_amount_in_eth
					eth_data["wallet"]["eth"] = eth_wallet
					save_eth_data(eth_data)

					# Форматирование переменной fines с пробелами для разделения тысяч
					message_updated_fines = int(updated_fines)
					message_amount = int(amount)
					
					formatted_amount = "{:,}".format(message_amount).replace(',', ' ')
					formatted_updated_fines = "{:,}".format(message_updated_fines).replace(',', ' ')

					# Уведомляем пользователя о штрафе
					await bot.send_message(user_id, f"👩🏻‍🦰💬 <b>Здравствуйте, {user_name}! Сумма ваших штрафов была уменьшена.</b>\n\n" \
													"<b>• Краткая информация о штрафах:</b>\n" \
													f"<b>↳ </b><b>Сумма штрафов уменьшена на • 💷 {formatted_amount} </b>₽\n" \
													f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
													f"💬 <b>Сообщение от администрации: {message_text}.</b>")
					
					await message.answer(f"👩🏻‍🦰💬 <b>Сумма штрафов для пользователя {user_name} обновлена.</b>\n\n"
										"<b>• Краткая информация о штрафах:</b>\n" \
										f"<b>↳ </b><b>Сумма штрафов уменьшена на • 💷 {formatted_amount} </b>₽\n" \
										f"<b>↳ </b><b>Текущая сумма штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
										f"💬 <b>Отправленое сообщение: {message_text}.</b>")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /add_fines
@dp.message_handler(commands=['add_fines_s'])
async def add_fines(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()
		
		if len(args) < 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/add_fines_s</code> [user_id] [сумма] [сообщение]</b>")
			return
		else:
			user_id = args[0]
			amount = args[1]
			
			# Проверяем, есть ли такой пользователь в данных
			user_data = load_user_data()
			if user_id not in user_data:
				await message.answer(f"👩🏻‍🦰💬 <b>Пользователь • <code>{user_id}</code> не найден.</b>")
				return
			else:
				# Получаем сообщение из аргументов
				message_text = " ".join(args[2:])

				# Прибавляем сумму к текущему значению штрафов пользователя
				current_fines = int(user_data[user_id].get("fines_slava", 0))
				updated_fines = current_fines + int(amount)
				user_data[user_id]["fines_slava"] = updated_fines
				save_user_data(user_data)

				# Форматирование переменной fines с пробелами для разделения тысяч
				message_amount = int(amount)
				message_updated_fines = int(updated_fines)

				formatted_amount = "{:,}".format(message_amount).replace(',', ' ')
				formatted_updated_fines = "{:,}".format(message_updated_fines).replace(',', ' ')

				# Получаем имя пользователя
				user = user_data[user_id]
				user_name = user.get("userlastname", "Пользователь")

				# Уведомляем пользователя о штрафе
				await bot.send_message(user_id, f"👩🏻‍🦰💬 <b>Здравствуйте, {user_name}! Сумма ваших долгов была увеличена.</b>\n\n" \
												"<b>• Краткая информация о долгах:</b>\n" \
												f"<b>↳ </b><b>Сумма долгов увеличена на • 💷 {formatted_amount} </b>₽\n" \
												f"<b>↳ </b><b>Текущая сумма долгов • 💷 {formatted_updated_fines} </b>₽\n\n" \
												f"💬 <b>Сообщение от администрации: {message_text}.</b>")
				
				await message.answer(f"👩🏻‍🦰💬 <b>Сумма долгов для пользователя {user_name} обновлена.</b>\n\n"
									"<b>• Краткая информация о долгах:</b>\n" \
									f"<b>↳ </b><b>Сумма долгов увеличена на • 💷 {formatted_amount} </b>₽\n" \
									f"<b>↳ </b><b>Текущая долгов штрафов • 💷 {formatted_updated_fines} </b>₽\n\n" \
									f"💬 <b>Отправленое сообщение: {message_text}.</b>")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")

# Функция для обработки команды /aw_fines
@dp.message_handler(commands=['aw_fines_s'])
async def aw_fines(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()

	if is_admin_in_data(user_id, admin_data):
		# Разбиваем текст команды на аргументы
		args = message.get_args().split()
		
		if len(args) < 2:
			await message.answer("<b>👩🏻‍🦰💬 Используйте команду <code>/aw_fines_s</code> [user_id] [сумма] [сообщение]</b>")
			return
		else:
			user_id = args[0]
			amount = args[1]
			
			# Проверяем, есть ли такой пользователь в данных
			user_data = load_user_data()

			if user_id not in user_data:
				await message.answer(f"👩🏻‍🦰💬 <b>Пользователь • <code>{user_id}</code> не найден.</b>")
				return
			else:
				# Получаем текущую сумму штрафов пользователя
				current_fines = int(user_data[user_id].get("fines_slava", 0))

				# Получаем имя пользователя
				user = user_data[user_id]
				user_name = user.get("userlastname", "Пользователь")

				# Проверяем, что отнимаемая сумма не больше текущей суммы штрафов
				if int(amount) > current_fines:
					await message.answer(f"👩🏻‍🦰💬 <b>Сумма для уменьшения больше текущей суммы штрафов пользователя {user_name}.</b>")
					return
				else:
					# Получаем сообщение из аргументов
					message_text = " ".join(args[2:])

					# Вычитаем сумму из текущих штрафов пользователя
					updated_fines = current_fines - int(amount)
					user_data[user_id]["fines_slava"] = updated_fines
					save_user_data(user_data)

					# Форматирование переменной fines с пробелами для разделения тысяч
					message_updated_fines = int(updated_fines)
					message_amount = int(amount)
					
					formatted_amount = "{:,}".format(message_amount).replace(',', ' ')
					formatted_updated_fines = "{:,}".format(message_updated_fines).replace(',', ' ')

					# Уведомляем пользователя о штрафе
					await bot.send_message(user_id, f"👩🏻‍🦰💬 <b>Здравствуйте, {user_name}! Сумма ваших долгов была уменьшена.</b>\n\n" \
													"<b>• Краткая информация о долгах:</b>\n" \
													f"<b>↳ </b><b>Сумма долгов уменьшена на • 💷 {formatted_amount} </b>₽\n" \
													f"<b>↳ </b><b>Текущая сумма долгов • 💷 {formatted_updated_fines} </b>₽\n\n" \
													f"💬 <b>Сообщение от администрации: {message_text}.</b>")
					
					await message.answer(f"👩🏻‍🦰💬 <b>Сумма долгов для пользователя {user_name} обновлена.</b>\n\n"
										"<b>• Краткая информация о долгах:</b>\n" \
										f"<b>↳ </b><b>Сумма долгов уменьшена на • 💷 {formatted_amount} </b>₽\n" \
										f"<b>↳ </b><b>Текущая сумма долгов • 💷 {formatted_updated_fines} </b>₽\n\n" \
										f"💬 <b>Отправленое сообщение: {message_text}.</b>")
	else:
		await message.answer("👩🏻‍🦰💬 <b>У вас нету прав использовать эту команду.</b>")