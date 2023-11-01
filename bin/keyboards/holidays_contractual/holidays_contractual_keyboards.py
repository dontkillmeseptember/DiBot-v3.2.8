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

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Праздники и договор"
dp.register_message_handler(holidays_contractual_handler, lambda message: message.text == yml_loader.holidays_contractual_data["button_holidays_contractual"])

# Кнопка "RedSlavBank"
def button_fines(message: types.Message):
	# Проверяем, является ли пользователь регистрирован
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Получаем сумму платежа
		interest_summ = calculate_interest(message)

		formatted_interest_summ = "{:,.0f}".format(interest_summ).replace(',', ' ')

		return formatted_interest_summ
	else:
		return 0

dp.register_message_handler(check_user_rsb, lambda message: message.text == f"📁💳 RedSlavBank • {button_fines(message)} ₽")

# Кнопка "Договор"
dp.register_message_handler(contract_handler, lambda message: message.text == yml_loader.contract_path["contract"]["button_contract"])

# Кнопка "Календарь"
# Получаем текущую дату и форматируем её
current_date = datetime.datetime.now()
russian_month = get_russian_month(current_date.month)

formatted_date = f"{current_date.day} {russian_month}"

dp.register_message_handler(handle_start, lambda message: message.text == f"📁📅 Календарь • {formatted_date}")