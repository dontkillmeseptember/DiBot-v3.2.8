from misc.util import types, logging, State, StatesGroup, FSMContext
from misc.loader import dp, bot

from data.start_db import load_user_data, is_user_in_data
from data.admin_db import load_admin_data

class PhotoState(StatesGroup):
	send_photo_admin = State()

@dp.message_handler(commands=['sd_photo'])
async def send_photo_command(message: types.Message):
	"""Переменные для проверки пользователя на нахождение в базе данных"""
	user_id = message.from_user.id
	user_data = load_user_data()

	"""Проверяем есть ли пользователь в базе данных"""
	if is_user_in_data(user_id, user_data):
		await message.answer("<b>👩🏻‍🦰💬 Пожалуйста, отправьте фотографию или видео для передачи администрации.</b>")
	
		await PhotoState.send_photo_admin.set()
	else:
		print("User not register")

@dp.message_handler(content_types=['photo', 'video'], state=PhotoState.send_photo_admin)
async def send_photo_is_admin(message: types.Message, state: FSMContext):
	try:
		"""Переменные для проверки пользователя на нахождение в базе данных"""
		user_id = message.from_user.id
		user_data = load_user_data()

		"""Проверяем есть ли пользователь в базе данных"""
		if is_user_in_data(user_id, user_data):
			"""Проверяем отправил пользователь фотографию"""
			if message.photo:
				"""Переменные для проверки базы данных на админов"""
				admin_data = load_admin_data()

				"""Создаем цикл для вывода всех user_id админов"""
				for user_admin_id in admin_data:
					"""Переменная для отправки подписи пользователя"""
					user = message.from_user
					userlastname = user.first_name

					user_text = f"<b>👩🏻‍🦰💬 Пользователь {userlastname} прислал фотографию с подписью:</b>\n\n" \
								f"<b>💬 {message.caption}</b>"

					await bot.send_photo(chat_id=user_admin_id, photo=message.photo[-1].file_id, caption=user_text)

				await message.answer("<b>👩🏻‍🦰💬 Фотография успешна отправлена администрации.</b>")

				await state.finish()
			else:
				await message.answer("<b>👩🏻‍🦰💬 Пожалуйста, отправьте фотографию.</b>")
			"""Проверяем отправил пользователь видео"""
			if message.video:
				"""Переменные для проверки базы данных на админов"""
				admin_data = load_admin_data()

				"""Создаем цикл для вывода всех user_id админов"""
				for user_admin_id in admin_data:
					"""Переменная для отправки подписи пользователя"""
					user = message.from_user
					userlastname = user.first_name

					user_text = f"<b>👩🏻‍🦰💬 Пользователь {userlastname} прислал видео с подписью:</b>\n\n" \
								f"<b>💬 {message.caption}</b>"

					await bot.send_video(chat_id=user_admin_id, video=message.video.file_id, caption=user_text)

				await message.answer("<b>👩🏻‍🦰💬 Видео успешна отправлена администрации.</b>")

				await state.finish()
			else:
				await message.answer("<b>👩🏻‍🦰💬 Пожалуйста, отправьте видео.</b>")
		else:
			print("User not register")
	except Exception:
		logging.exception("ERROR: 404 - SEND_PHOTO: FUNC - SEND_PHOTO_IS_ADMIN")