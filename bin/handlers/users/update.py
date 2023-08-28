from misc.loader import dp, bot
from misc.util import types

from keyboards.main import update_bot_handler

# Обработчик команды /update
@dp.message_handler(commands=["update"])
async def update_bot_command(message: types.Message):
    await update_bot_handler(message, bot)