from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, datetime, WebAppInfo
from misc.loader import bot, moscow_tz

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data

from data.config import PHOTO_PATH

def create_quest_keyboard():
	web = WebAppInfo(url="https://ru.warface.com/seasons/treasurehunting")

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row(
		KeyboardButton(yml_loader.quest_data["quest_buttons"]["info"]),
		KeyboardButton(yml_loader.quest_data["quest_buttons"]["quest"], web_app=web)
	)
	keyboard.add(KeyboardButton(yml_loader.main_path["main_menu"]["button_main_menu"]))

	return keyboard

# Обработчик вкладки "Задания"
async def quest_handler(message: types.Message):
	# Переменная для кнопок
	keyboard = create_quest_keyboard()

	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()
	
	if is_admin_in_data(user_id, admin_data):
		await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info"], reply_markup=keyboard)
	else:
		# Получение текущей даты и времени
		current_datetime = datetime.datetime.now(moscow_tz)
		target_datetime = datetime.datetime(current_datetime.year, month=9, day=31, hour=0, minute=0, second=0)
		target_datetime = moscow_tz.localize(target_datetime)
		
		time_diff = target_datetime - current_datetime
		
		# Рассчитываем оставшееся время до целевой даты и времени
		days = time_diff.days
		hours = time_diff.seconds // 3600
		minutes = (time_diff.seconds % 3600) // 60

		if time_diff.total_seconds() > 0:
			await bot.send_message(message.chat.id, f"<b>👩🏻‍🦰💬 Вкладка — <code>{yml_loader.quest_data['quest']['button_quest']}</code> будет доступна через: <code>{days} дней {hours} часов и {minutes} минут.</code></b>")
		else: 
			await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info"], reply_markup=keyboard)

async def info_handler(message: types.Message):
	await bot.send_photo(message.chat.id, photo=PHOTO_PATH, caption=yml_loader.quest_data["quest"]["quest_info"])