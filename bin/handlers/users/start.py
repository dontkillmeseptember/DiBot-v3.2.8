from misc.loader import dp, bot
from misc.util import types

from keyboards.main import start_handler

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await start_handler(message, bot)
