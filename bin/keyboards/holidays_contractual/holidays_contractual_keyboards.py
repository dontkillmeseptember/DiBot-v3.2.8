from data import yml_loader

from data.eth_db import calculate_interest
from data.start_db import load_user_data, is_user_in_data, save_user_data

from misc.util import datetime, types
from misc.loader import dp

from data.base_glossary import get_russian_month

from keyboards.holidays_contractual.main import holidays_contractual_handler
from keyboards.holidays_contractual.redslavbank.rsb_func import check_user_rsb

from keyboards.holidays_contractual.contract.contract_func import contract_handler
from keyboards.holidays_contractual.calendar.calendar_func import handle_start

def now_date():
	# Получаем текущую дату и форматируем её
	current_date = datetime.datetime.now()
	russian_month = get_russian_month(current_date.month)

	formatted_date = f"{current_date.day} {russian_month}"

	return formatted_date

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Праздники и договор"
dp.register_message_handler(holidays_contractual_handler, lambda message: message.text == yml_loader.holidays_contractual_data["button_holidays_contractual"])

# Кнопка "RedSlavBank"
dp.register_message_handler(check_user_rsb, lambda message: message.text == f"📁💳 RedSlavBank")

# Кнопка "Договор"
dp.register_message_handler(contract_handler, lambda message: message.text == yml_loader.contract_path["contract"]["button_contract"])

# Кнопка "Календарь"
dp.register_message_handler(handle_start, lambda message: message.text == f"📁📅 Календарь • {now_date()}")