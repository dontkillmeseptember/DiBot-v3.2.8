from misc.util import ReplyKeyboardMarkup, KeyboardButton, types, datetime
from misc.loader import bot, moscow_tz

from data import yml_loader
from data.start_db import check_user_data

# Создание клавитуры для меню
def create_menu_keyboard(message: types.Message):
	# Выводим информацию о пользователе для кнопки "Ваш профиль"
	user = message.from_user
	user_id = user.id
	user_data = check_user_data(user_id)
	smile = user_data.get("smile", "Uxknow")
	battlepass = user_data.get("battlepass", "Uxknow")

	# Отсчет времени до остановки батлпасса
	current_datetime = datetime.datetime.now(moscow_tz)
	target_datetime = datetime.datetime(year=2024, month=1, day=15, hour=0, minute=0, second=0)
	target_datetime = moscow_tz.localize(target_datetime)

	time_diff = target_datetime - current_datetime

	# Рассчитываем оставшееся время до целевой даты и времени
	days = time_diff.days
	hours = time_diff.seconds // 3600

	# Создаем клавиатуру с вкладками
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	keyboard.row(
		KeyboardButton(yml_loader.energy_training_data["button_energy_training"]), 
		KeyboardButton(yml_loader.holidays_contractual_data["button_holidays_contractual"])
	)
	keyboard.add(KeyboardButton(f"🐺 Белый Волк • Летопись Ведьмака • {days}Д {hours}Ч 🗡️"))
	keyboard.row(
		KeyboardButton(yml_loader.version_data["version"]["button_update"]), 
		KeyboardButton(f"{smile} Ваш Профиль — {battlepass}")
	)

	return keyboard

async def info_bot(message: types.Message):
	await bot.send_message(message.chat.id, yml_loader.start_bot_path["start"]["base_info"])

# Обработчик "Главное меню"
async def main_menu(message: types.Message):
	keyboard = create_menu_keyboard(message)
	
	await bot.send_message(message.chat.id, yml_loader.main_path["main_menu"]["main_menu_info"], reply_markup=keyboard)