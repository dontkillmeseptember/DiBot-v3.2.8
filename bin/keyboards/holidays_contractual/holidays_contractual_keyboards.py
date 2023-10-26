from data import yml_loader
from misc.loader import dp

from keyboards.holidays_contractual.main import holidays_contractual_handler
from keyboards.holidays_contractual.redslavbank.rsb_func import check_user_rsb

from keyboards.holidays_contractual.contract.contract_func import contract_handler
from keyboards.holidays_contractual.calendar.calendar_func import handle_start

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Праздники и договор"
dp.register_message_handler(holidays_contractual_handler, lambda message: message.text == yml_loader.holidays_contractual_path["button_holidays_contractual"])

# Кнопка "Штрафы"
dp.register_message_handler(check_user_rsb, lambda message: message.text == yml_loader.fines_data["fines"]["button_fines"])

# Кнопка "Договор"
dp.register_message_handler(contract_handler, lambda message: message.text == yml_loader.contract_path["contract"]["button_contract"])

# Кнопка "Календарь"
dp.register_message_handler(handle_start, lambda message: message.text == yml_loader.calendar_path["calendar"]["button_calendar"])