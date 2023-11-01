from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, State, StatesGroup, FSMContext, asyncio, random
from misc.loader import dp, bot

from data import yml_loader

from data.config import PHOTO_PATH_CONTRACT

# Обработчик для контракта
async def contract_handler(message: types.Message):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_igor"], callback_data="contract_igor"))

	await bot.send_photo(message.chat.id, photo=PHOTO_PATH_CONTRACT, caption=yml_loader.contract_path["contract"]["info"], reply_markup=inline_keyboard)

async def contract_igor(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="forward_new10"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new1")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new1(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new1"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new2")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_three"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new2(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new2"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new3")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_four"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new3(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new3"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new4")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_five"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new4(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new4"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new5")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_six"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new5(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new5"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new6")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_seven"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new6(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new6"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new7")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_eight"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new7(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new7"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new8")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_nine"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new8(callback_query: types.CallbackQuery):
	"""Создаем инлайн клавиатуру"""
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new8"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_start"], callback_data="forward_new9")
	)

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_igor"]["contract_ten"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчики для каждой кнопки
handlers = {
	"contract_igor": contract_igor,
	"forward_new": process_callback_forward_new,
	"forward_new1": process_callback_forward_new1,
	"forward_new2": process_callback_forward_new2,
	"forward_new3": process_callback_forward_new3,
	"forward_new4": process_callback_forward_new4,
	"forward_new5": process_callback_forward_new5,
	"forward_new6": process_callback_forward_new6,
	"forward_new7": process_callback_forward_new7,
	"forward_new8": process_callback_forward_new8,
	"forward_new9": contract_igor,
	"forward_new10": process_callback_forward_new8,
	"backward_new": contract_igor,
	"backward_new1": process_callback_forward_new,
	"backward_new2": process_callback_forward_new1,
	"backward_new3": process_callback_forward_new2,
	"backward_new4": process_callback_forward_new3,
	"backward_new5": process_callback_forward_new4,
	"backward_new6": process_callback_forward_new5,
	"backward_new7": process_callback_forward_new6,
	"backward_new8": process_callback_forward_new7
}

# Обработчик для кнопок вкладки "Договор"
@dp.callback_query_handler(lambda query: query.data in handlers)
async def contract_callback_handler(callback_query: types.CallbackQuery):
	handler_func = handlers[callback_query.data]
	await handler_func(callback_query)