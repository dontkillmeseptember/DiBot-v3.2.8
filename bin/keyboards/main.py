from misc.util import types
from misc.loader import bot

from keyboards.main_menu import main_menu
from keyboards.main_keyboard import dp as main_keyboard_dp

from keyboards.start.start_bot import start_handler
from keyboards.start.buttons_start import dp as start_buttons_dp

from keyboards.update.update_func import update_bot_handler
from keyboards.update.update_keyboards import dp as update_buttons_dp

from keyboards.version.version_func import version_handler
from keyboards.version.version_keyboards import dp as version_buttons_dp

from keyboards.holidays_contractual.main import holidays_contractual_handler
from keyboards.holidays_contractual.holidays_contractual_keyboards import dp as holidays_contractual_dp

from keyboards.holidays_contractual.contract.contract_func import contract_handler

from keyboards.holidays_contractual.fines.fines_func import fines_handler
from keyboards.holidays_contractual.fines.fines_keyboards import dp as fines_dp

from keyboards.holidays_contractual.calendar.calendar_func import handle_start

from keyboards.quest.quest_func import quest_handler
from keyboards.quest.quest_keyboards import dp as quest_dp

from keyboards.energy_training.main import energy_training_handler
from keyboards.energy_training.energy_training_keyboards import dp as energy_training_dp

from keyboards.energy_training.news.news_func import news_handler
from keyboards.energy_training.news.news_keyboards import dp as news_dp

from keyboards.energy_training.news_igor.news_igor_func import news_igor_handler
from keyboards.energy_training.news_igor.news_igor_keyboards import dp as news_igor_dp

from keyboards.energy_training.cooking.cooking_func import cooking_handler
from keyboards.energy_training.cooking.cooking_keyboards import dp as cooking_dp

from keyboards.energy_training.cooking.ration.ration_func import ration_handler
from keyboards.energy_training.cooking.ration.ration_keyboards import dp as ration_dp

# Обработчик всех функций с кнопками
async def all_keyboards(message: types.Message):
	await start_handler(message, bot)
	await update_bot_handler(message, bot)
	await version_handler(message)
	await main_menu(message)
	await holidays_contractual_handler(message, bot)
	await fines_handler(message)
	await quest_handler(message)
	await energy_training_handler(message)
	await contract_handler(message)
	await ration_handler(message)
	await handle_start(message)
	await cooking_handler(message)