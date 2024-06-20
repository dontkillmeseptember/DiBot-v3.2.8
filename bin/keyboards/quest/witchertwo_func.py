from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types
from misc.loader import dp, bot

from data.config import PHOTO_THE_WITCHER_TWO

from data import yml_loader

# Обработчик второй части ведьмака
async def start_the_witcher_two(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["start"], callback_data="start_two_two"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_TWO, caption=yml_loader.quest_data["quest"]["thewitchertwo_info"], reply_markup=inline_keyboard)

# Обработчик второй части ведьмака
async def start_the_witcher_two_call(callback_query: types.CallbackQuery):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["start"], callback_data="start_two_two"))

	await bot.send_photo(chat_id=callback_query.message.chat.id, photo=PHOTO_THE_WITCHER_TWO, caption=yml_loader.quest_data["quest"]["thewitchertwo_info"], reply_markup=inline_keyboard)