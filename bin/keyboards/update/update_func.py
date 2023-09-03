from misc.util import (
	ReplyKeyboardMarkup,
	KeyboardButton,
	InlineKeyboardMarkup,
	InlineKeyboardButton,
	asyncio,
	types
)

from misc.loader import bot

from data import yml_loader
from data.start_db import load_user_data, is_user_in_data, save_user_data
from data.version_db import get_bot_version

from keyboards.main_menu import create_menu_keyboard
from keyboards.start.start_bot import start_bot

def keyboard_update_bot():
	# Создаем клавиатуру с вкладками
	keyboard_update = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard_update.add(KeyboardButton(yml_loader.update_data["update_bot"]["button_update_bot"]))

	return keyboard_update

# Обработчик вкладки "Обновить бота"
async def update_bot_handler(message, bot: types.Message):
	keyboard = keyboard_update_bot()

	# Проверка у пользователя версии
	user_id = message.from_user.id
	user_data = load_user_data()

	bot_version = get_bot_version()
	user_bot_version = user_data.get(str(user_id), {}).get("version_bot", "")

	if user_bot_version == bot_version:
		await message.answer(yml_loader.update_data["update_bot"]["version_check_info"])
	else:
		await bot.send_message(
				message.chat.id, 
				yml_loader.update_data["update_bot"]["button_update_bot_info"], 
				reply_markup=keyboard
			)

# Функция для отправки сообщения с анимацией загрузки
async def send_loading_message(chat_id):
	message_text = yml_loader.update_data["loading"]["loading_info"]
	loading_symbols = ["🌍", "🌎", "🌏"]  # Unicode-символы загрузки
	loading_animation = "".join(loading_symbols)  # Объединяем символы загрузки

	message = await bot.send_message(chat_id, f"{message_text} {loading_animation}")
	loading_message_id = message.message_id

	# Анимация загрузки
	for _ in range(30):  # Продолжаем цикл 10 раз для около 5 секунд
		for symbol in loading_symbols:
			await asyncio.sleep(0.005)
			await bot.edit_message_text(f"{message_text} {symbol}", chat_id=message.chat.id, message_id=message.message_id)

	# Удаление сообщения с анимацией загрузки
	await bot.delete_message(chat_id, loading_message_id)

	# Отправляем новое сообщение с информацией об обновлении
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.update_data["loading"]["end_update_bot"], callback_data="next_update"))

	await bot.send_message(chat_id, yml_loader.update_data["loading"]["end_update_info"], reply_markup=inline_keyboard)

# Обработчик для кнопки "Обновить бота" чтобы появлялась анимация и т.д
async def update_bot_button_handler(message: types.Message):
	# Отправляем сообщение с анимацией загрузки
	await send_loading_message(message.chat.id)

# Обработчик выбора вкладки "Главное меню"
async def main_menu_update_bot_handler(message: types.Message):
	keyboard = create_menu_keyboard()

	bot_version = get_bot_version()

	await bot.send_message(message.chat.id, f"{yml_loader.version_data['version_0_0_3'][f'button_update_{bot_version}_info']}", reply_markup=keyboard)

# Обработчик для перехожа во вкладку "Главное меню"
async def process_callback_next_update(callback_query: types.CallbackQuery):
	# Проверяем, является ли пользователь регистрирован
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	bot_version = get_bot_version()

	if is_user_in_data(user_id, user_data):
		# Обновляем version_bot в user_data.json
		user_data[str(user_id)]["version_bot"] = bot_version
		save_user_data(user_data)

		await main_menu_update_bot_handler(callback_query.message)
		await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
	else:
		await start_bot(callback_query.message)
		await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)