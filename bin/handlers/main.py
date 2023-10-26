from misc.util import types

from handlers.users.start import start_command
from handlers.users.update import update_bot_command
from handlers.users.mailings import subscribe_command
from handlers.users.profile import profile_command

from handlers.admin.login import on_admin_command, on_delete_admin_command
from handlers.admin.notices import send_nt_message_command
from handlers.admin.fines import add_fines_command

# Функция для команд пользователей
async def all_users(message: types.Message):
	await start_command(message)
	await update_bot_command(message)
	await subscribe_command(message)
	await profile_command(message)

# Функция для команд админов
async def all_admin(message: types.Message):
	await on_admin_command(message)
	await on_delete_admin_command(message)
	await send_nt_message_command(message)
	await add_fines_command(message)