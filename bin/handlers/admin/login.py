from misc.util import types
from misc.loader import dp, bot

from data.config import SECRET_PASSWORD
from data.admin_db import save_admin_data, load_admin_data, is_admin_in_data
from data.start_db import load_user_data, save_user_data

from data import yml_loader

# Обработчик команды /login_admin
@dp.message_handler(commands=['login_admin'])
async def on_admin_command(message: types.Message):
	await message.answer(yml_loader.admin_path["admin"]["password"])
	dp.register_message_handler(process_password_for_admin, content_types=types.ContentType.TEXT)

async def process_password_for_admin(message: types.Message):
	user_password = message.text

	if user_password == SECRET_PASSWORD:
		user_id = message.from_user.id
		username = message.from_user.username
		user_admin = yml_loader.admin_path["admin"]["admin_role"]
		user_smile = yml_loader.start_bot_path["registor"]["smile_admin"]

		user_data = load_user_data()
		admin_data = load_admin_data()

		if not is_admin_in_data(user_id, admin_data):
			admin_data[str(user_id)] = {"username": username}

			save_admin_data(admin_data)

			await bot.send_message(user_id, yml_loader.admin_path["admin"]["add_admin"])

			# Обновляем роль пользователя в user_data.json
			user_data[str(user_id)]["role"] = user_admin
			user_data[str(user_id)]["smile"] = user_smile
			save_user_data(user_data)
		else:
			await bot.send_message(user_id, yml_loader.admin_path["admin"]["has_admin"])
	else:
		await bot.send_message(message.from_user.id, yml_loader.admin_path["admin"]["error_password"])

	dp.message_handlers.unregister(process_password_for_admin)

# Обработчик команды /exit_admin
@dp.message_handler(commands=['exit_admin'])
async def on_delete_admin_command(message: types.Message):
	await message.answer(yml_loader.admin_path["exit_admin"]["password"])
	dp.register_message_handler(process_password_for_delete_admin, content_types=types.ContentType.TEXT)

async def process_password_for_delete_admin(message: types.Message):
	user_password = message.text

	if user_password == SECRET_PASSWORD:
		user_id = message.from_user.id
		user_role = yml_loader.start_bot_path["registor"]["user_role"]
		user_smile = yml_loader.start_bot_path["registor"]["smile_user"]

		user_data = load_user_data()
		admin_data = load_admin_data()

		if is_admin_in_data(user_id, admin_data):
			del admin_data[str(user_id)]
			save_admin_data(admin_data)

			await bot.send_message(user_id, yml_loader.admin_path["exit_admin"]["del_admin"])

			# Возвращаем роль "Пользователь" при выходе из администраторов
			user_data[str(user_id)]["role"] = user_role
			user_data[str(user_id)]["smile"] = user_smile
			save_user_data(user_data)
		else:
			await bot.send_message(user_id, yml_loader.admin_path["exit_admin"]["nope_admin"])
	else:
		await bot.send_message(message.from_user.id, yml_loader.admin_path["exit_admin"]["error_password"])

	dp.message_handlers.unregister(process_password_for_delete_admin)

# Обработчик команды /delete_admin
@dp.message_handler(commands=['delete_admin'])
async def on_delete_admin_command(message: types.Message):
	await message.answer(yml_loader.admin_path["delete_admin"]["user_id"])
	dp.register_message_handler(process_user_id_for_delete_admin, content_types=types.ContentType.TEXT)

async def process_user_id_for_delete_admin(message: types.Message):
	try:
		user_id_to_delete = int(message.text)
	except ValueError:
		await bot.send_message(message.from_user.id, yml_loader.admin_path["delete_admin"]["invalid_user_id"])
		dp.message_handlers.unregister(process_user_id_for_delete_admin)
		return

	if user_id_to_delete == message.from_user.id:
		await bot.send_message(message.from_user.id, yml_loader.admin_path["delete_admin"]["cannot_delete_self"])
		dp.message_handlers.unregister(process_user_id_for_delete_admin)
		return

	user_role = yml_loader.start_bot_path["registor"]["user_role"]
	user_smile = yml_loader.start_bot_path["registor"]["smile_user"]

	user_data = load_user_data()
	admin_data = load_admin_data()

	if is_admin_in_data(user_id_to_delete, admin_data):
		del admin_data[str(user_id_to_delete)]
		save_admin_data(admin_data)
		await bot.send_message(user_id_to_delete, yml_loader.admin_path["delete_admin"]["you_deleted"])
		await bot.send_message(message.from_user.id, yml_loader.admin_path["delete_admin"]["admin_deleted"])

		# Обновляем роль пользователя при удалении администратора
		if str(user_id_to_delete) in user_data:
			user_data[str(user_id_to_delete)]["role"] = user_role
			user_data[str(user_id_to_delete)]["smile"] = user_smile
			save_user_data(user_data)
	else:
		await bot.send_message(message.from_user.id, yml_loader.admin_path["delete_admin"]["user_not_admin"])

	dp.message_handlers.unregister(process_user_id_for_delete_admin)
