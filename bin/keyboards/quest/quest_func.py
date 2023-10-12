from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, datetime
from misc.loader import bot, moscow_tz

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data
from data.start_db import check_user_data, load_user_data, save_user_data, is_user_in_data

from data.config import PHOTO_PATH, PHOTO_PATH_PREVIEW, PHOTO_REWARD

from keyboards.quest.witcherone_func import start_the_witcher_one
from keyboards.quest.witchertwo_func import start_the_witcher_two
# from keyboards.quest.witcherthree_func import start_the_witcher_three

def create_quest_keyboard(message):
	# Выводим информацию о пользователе для кнопки "Ваш прогресс"
	user = message.from_user
	user_id = user.id
	user_data = check_user_data(user_id)
	battlepass = user_data.get("battlepass", "Uxknow")

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.quest_data["quest_buttons"]["awards"]),
		KeyboardButton(yml_loader.quest_data["quest_buttons"]["info"])
	)
	keyboard.add(KeyboardButton(yml_loader.quest_data["quest_buttons"]["quest"]))
	keyboard.row(
		KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]),
		KeyboardButton(f"📈 Ваш прогресс — {battlepass}")
	)

	return keyboard

# Обработчик вкладки "Задания"
async def quest_handler(message: types.Message):
	# Переменная для кнопок
	keyboard = create_quest_keyboard(message)

	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()
	
	if is_admin_in_data(user_id, admin_data):
		await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info"], reply_markup=keyboard)
	else:
		# Получение текущей даты и времени
		current_datetime = datetime.datetime.now(moscow_tz)
		target_datetime = datetime.datetime(current_datetime.year, month=10, day=31, hour=0, minute=0, second=0)
		target_datetime = moscow_tz.localize(target_datetime)
		
		time_diff = target_datetime - current_datetime
		
		# Рассчитываем оставшееся время до целевой даты и времени
		days = time_diff.days
		hours = time_diff.seconds // 3600
		minutes = (time_diff.seconds % 3600) // 60

		if time_diff.total_seconds() > 0:
			await bot.send_photo(message.chat.id, photo=PHOTO_PATH_PREVIEW, caption=f"<b>• Боевой пропуск — {yml_loader.quest_data['quest']['button_quest']};\n 	↳ будет доступна через: <code>⌛️ {days}Д {hours}Ч и {minutes}М</code></b>")
		else:
			await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info"], reply_markup=keyboard)

# Обработчик вкладки "В путь!"
async def start_battlepass(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже выбранная часть у пользователя
		if str(user_id) in user_data and "active_chapter" in user_data[str(user_id)]:
			selected_chapters = user_data[str(user_id)]["active_chapter"]

			if selected_chapters is None:
				await start_the_witcher_one(message)
			elif selected_chapters == "the_witcher_two":
				await start_the_witcher_two(message)
			elif selected_chapters == "the_witcher_three":
				await start_the_witcher_three(message)
	else:
		print("User not registor.")

# Обработчик вкладки "Награды боевого пропуска"
async def info_rewards(message: types.Message):
	await bot.send_photo(message.chat.id, photo=PHOTO_REWARD, caption=yml_loader.quest_data["quest"]["reward_info"])

# Обработчик вкладки "Информация о боевом пропуске"
async def info_handler(message: types.Message):
	await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info"])
