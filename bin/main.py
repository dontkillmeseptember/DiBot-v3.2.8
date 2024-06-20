from data.functions import functions_all
from data.mailings_db import daily_reset_has_visited_sport
from data.scheduled import job_settings_ration, settings_calendar, settings_sport

from misc.util import logging
from misc.loader import dp, bot, scheduler

from keyboards.energy_training.cooking.ration.ration_func import daily_reset_has_visited_ration

# Установка логгера для отображения информации об ошибках
logging.basicConfig(level=logging.INFO)

# Функция для запуска бота
async def on_startup(dp, message):
	await functions_all(dp, message, bot)

# Функция для запуска ежедневного сброса флага has_visited_ration в полночь
async def daily_reset_job():
	await daily_reset_has_visited_ration()
	await daily_reset_has_visited_sport()

# Добавляем задачи в планировщик
for job_setting in job_settings_ration:
	scheduler.add_job(**job_setting)

# Добавляем задачи в планировщик
for calendar in settings_calendar:
	scheduler.add_job(**calendar)

for sport_mallings in settings_sport:
	 scheduler.add_job(**sport_mallings)

# Устанавливаем задачу для ежедневного сброса флага в полночь
scheduler.add_job(daily_reset_job, "cron", hour=0)

scheduler.start()

if __name__ == '__main__':
	from aiogram import executor
	executor.start_polling(dp, skip_updates=True)