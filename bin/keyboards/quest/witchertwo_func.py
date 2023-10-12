from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types
from misc.loader import dp, bot

from data.config import PHOTO_THE_WITCHER_THREE

from data import yml_loader

# Обработчик второй части ведьмака
async def start_the_witcher_two(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.quest_data["quest_buttons"]["start"], callback_data="start_two"))

	await bot.send_photo(chat_id=message.chat.id, photo=PHOTO_THE_WITCHER_THREE, caption=yml_loader.quest_data["quest"]["thewitchertwo_info"], reply_markup=inline_keyboard)
