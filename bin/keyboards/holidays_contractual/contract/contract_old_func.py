from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types
from misc.loader import dp, bot

from data import yml_loader

# Обработчик выбора вкладки "Договор" если пользотватель уже выбрал интерфейс
async def contract_start_old_interface_select(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="end"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward")
	)

	await bot.send_message(message.chat.id, yml_loader.contract_path["contract_info"]["contract_one"], reply_markup=inline_keyboard)

# Обработчик выбора вкладки "Договор"
async def contract_start_old_interface(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="end"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward")
	)

	await bot.edit_message_text(yml_loader.contract_path["contract_info"]["contract_one"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для кнопки "Далее" на первой странице вкладки "Договор"
async def process_callback_forward(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward2")
	)

	await bot.edit_message_text(yml_loader.contract_path["contract_info"]["contract_two"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для кнопки "Назад" на второй странице вкладки "Договор"
async def process_callback_backward(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="end"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward")
	)

	await bot.edit_message_text(yml_loader.contract_path["contract_info"]["contract_one"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для кнопки "Далее" на второй странице вкладки "Договор"
async def process_callback_forward2(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward2"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_start"], callback_data="start")
	)

	await bot.edit_message_text(yml_loader.contract_path["contract_info"]["contract_three"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для кнопки "В начало" на третьей странице вкладки "Договор"
async def process_callback_start(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="end"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward")
	)

	await bot.edit_message_text(yml_loader.contract_path["contract_info"]["contract_one"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик для кнопки "В конец" на третьей странице вкладки "Договор"
async def process_callback_end(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward2"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_start"], callback_data="start")
	)

	await bot.edit_message_text(yml_loader.contract_path["contract_info"]["contract_three"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчики для каждой кнопки
handlers = {
	"forward": process_callback_forward,
	"backward": process_callback_backward,
	"backward2": process_callback_forward,
	"forward2": process_callback_forward2,
	"start": process_callback_start,
	"end": process_callback_end,
}

# Обработчик для кнопок вкладки "Договор"
@dp.callback_query_handler(lambda query: query.data in handlers)
async def contract_callback_handler(callback_query: types.CallbackQuery):
	handler_func = handlers[callback_query.data]
	await handler_func(callback_query)