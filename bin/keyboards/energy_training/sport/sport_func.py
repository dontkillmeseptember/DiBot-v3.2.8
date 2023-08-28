from misc.util import types, datetime
from misc.loader import bot, moscow_tz

from data import yml_loader
from data.admin_db import is_admin_in_data, load_admin_data

# Обработчик "Упражнения на неделю"
async def sport_handler(message: types.Message):
	# Проверяем, является ли пользователь администратором
	user_id = message.from_user.id
	admin_data = load_admin_data()
	
	if is_admin_in_data(user_id, admin_data):
		await bot.send_message(message.chat.id, yml_loader.sport_data["sport"]["sport_info"])
	else:
		# Получение текущей даты и времени
		current_datetime = datetime.datetime.now(moscow_tz)
		target_datetime = datetime.datetime(current_datetime.year, month=7, day=31, hour=0, minute=0, second=0)  # Целевая дата и время (24 июля, 00:00)
		target_datetime = moscow_tz.localize(target_datetime)
		
		time_diff = target_datetime - current_datetime

		# Рассчитываем оставшееся время до целевой даты и времени
		days = time_diff.days
		hours = time_diff.seconds // 3600
		minutes = (time_diff.seconds % 3600) // 60
		
		if time_diff.total_seconds() > 0:
			await bot.send_message(message.chat.id, f"<b>👩🏻‍🦰💬 Вкладка — <code>{yml_loader.sport_data['sport']['button_sport']}</code> будет доступна через: <code>{days} дней {hours} часов и {minutes} минут.</code></b>")
		else:
			await bot.send_message(message.chat.id, yml_loader.sport_data["sport"]["sport_info"])