from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types
from misc.loader import dp, bot

from data.config import PHOTO_PATH_CONTRACT

from data import yml_loader

# Обработчик выбора вкладки "Договор" если пользователь выбрал интерфейс
async def contract_start_new_interface_select(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="forward_new11"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_PATH_CONTRACT, caption=yml_loader.contract_path["contract_info_new"]["contract_one"], reply_markup=inline_keyboard)

# Обработчик выбора вкладки "Договор"
async def contract_start_new_interface(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup(row_width=2)
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="forward_new11"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

	await bot.send_photo(chat_id=callback_query.message.chat.id, photo=PHOTO_PATH_CONTRACT, caption=yml_loader.contract_path["contract_info_new"]["contract_one"], reply_markup=inline_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'chapters')
async def contract_chapter(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_ago"], callback_data="backward_new"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["chapter_one"], callback_data="backward_new"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["chapter_two"], callback_data="forward_new7"))
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["chapter_three"], callback_data="forward_new8"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["chapter"]["chapter_info"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new2")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_end"], callback_data="forward_new11"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_one"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new2(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new2"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new3")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_three"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new2(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new2")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_two"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new3(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new3"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new4")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_four"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new3(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new2"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new3")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_three"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new4(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new4"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new5")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_five"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new4(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new3"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new4")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_four"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new5(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new5"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new6")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_six"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new5(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new4"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new5")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_five"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new6(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new6"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new7")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_seven"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new6(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new5"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new6")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_six"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new7(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new7"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new8")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_eight"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new7(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new6"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new7")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_seven"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new8(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new8"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new9")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_nine"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new8(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new7"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new8")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_eight"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new9(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new9"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new10")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_ten"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new9(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new8"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new9")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_nine"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new10(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new10"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new11")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_thousand"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new10(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new9"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new10")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_ten"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_forward_new11(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new11"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_start"], callback_data="backward_new")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_hundred"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_new11(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_back"], callback_data="backward_new10"),
		InlineKeyboardButton(yml_loader.contract_path["buttons"]["button_next"], callback_data="forward_new11")
	)
	inline_keyboard.add(InlineKeyboardButton(yml_loader.contract_path["chapter"]["button_chapter"], callback_data="chapters"))

	await bot.edit_message_caption(caption=yml_loader.contract_path["contract_info_new"]["contract_thousand"], chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчики для каждой кнопки
handlers = {
	"forward_new": process_callback_forward_new,
	"forward_new2": process_callback_forward_new2,
	"forward_new3": process_callback_forward_new3,
	"forward_new4": process_callback_forward_new4,
	"forward_new5": process_callback_forward_new5,
	"forward_new6": process_callback_forward_new6,
	"forward_new7": process_callback_forward_new7,
	"forward_new8": process_callback_forward_new8,
	"forward_new9": process_callback_forward_new9,
	"forward_new10": process_callback_forward_new10,
	"forward_new11": process_callback_forward_new11,
	"backward_new": process_callback_backward_new,
	"backward_new2": process_callback_backward_new2,
	"backward_new3": process_callback_backward_new3,
	"backward_new4": process_callback_backward_new4,
	"backward_new5": process_callback_backward_new5,
	"backward_new6": process_callback_backward_new6,
	"backward_new7": process_callback_backward_new7,
	"backward_new8": process_callback_backward_new8,
	"backward_new9": process_callback_backward_new9,
	"backward_new10": process_callback_backward_new10,
	"backward_new11": process_callback_backward_new11
}

# Обработчик для кнопок вкладки "Договор"
@dp.callback_query_handler(lambda query: query.data in handlers)
async def contract_callback_handler(callback_query: types.CallbackQuery):
	handler_func = handlers[callback_query.data]
	await handler_func(callback_query)