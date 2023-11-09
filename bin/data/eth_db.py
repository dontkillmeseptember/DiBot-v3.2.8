from misc.util import os, json, requests, types, logging

from data.rsb_db import load_rsb_data, is_rsb_in_data, save_rsb_data, check_rsb_data
from data.start_db import check_user_data

# Функции для получения текущего курса ETH
def get_eth_to_usd_rate():
	url = "https://api.coingecko.com/api/v3/simple/price"
	params = {
		"ids": "ethereum",
		"vs_currencies": "usd"
	}

	response = requests.get(url, params=params)
	data = response.json()
	eth_to_usd_rate = data.get("ethereum", {}).get("usd", 0)
	return eth_to_usd_rate

def get_eth_to_rub_rate():
	url = "https://api.coingecko.com/api/v3/simple/price"
	params = {
		"ids": "ethereum",
		"vs_currencies": "rub"
	}

	response = requests.get(url, params=params)
	data = response.json()
	eth_to_rub_rate = data.get("ethereum", {}).get("rub", 0)
	return eth_to_rub_rate

def get_rub_to_usd_rate():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "usd",
        "vs_currencies": "rub"
    }

    response = requests.get(url, params=params)
    data = response.json()
    rub_to_usd_rate = data.get("usd", {}).get("rub", 0)
    return rub_to_usd_rate

def get_usd_to_rub_rate():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "usd",
        "vs_currencies": "rub"
    }

    response = requests.get(url, params=params)
    data = response.json()
    usd_to_rub_rate = 1 / data.get("usd", {}).get("rub", 0)  # Обратный курс
    return usd_to_rub_rate

# Рассчет ETH в рубль и доллар
def get_eth_to_usd():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    eth_to_usd_rate = data.get("ethereum", {}).get("usd")
    return eth_to_usd_rate

def get_eth_to_rub():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=rub"
    response = requests.get(url)
    data = response.json()
    eth_to_rub_rate = data.get("ethereum", {}).get("rub")
    return eth_to_rub_rate

# Функции для перевода текущего ETH в Рубль и Доллар
def eth_to_usd(eth_amount, eth_to_usd_rate):
    usd_amount = eth_amount * eth_to_usd_rate
    return usd_amount


def eth_to_rub(eth_amount, eth_to_rub_rate):
    rub_amount = eth_amount * eth_to_rub_rate
    return rub_amount

# Функция для загрузки данных из JSON файла
def load_eth_data():
	version_path = os.path.join("bin", "db", "eth_data.json")

	if os.path.exists(version_path):
		with open(version_path, "r", encoding="utf-8") as file:
			return json.load(file)
	return {}

def get_eth_wallet():
	version_data = load_eth_data()
	version_bot = version_data.get("wallet", {}).get("eth", "")
	return version_bot

def get_interest_walltet_igor():
	interest_data = load_eth_data()
	interest_wallet = interest_data.get("interest_wallet", {}).get("interest_igor", "")
	return interest_wallet

def get_interest_walltet_dinara():
	interest_data = load_eth_data()
	interest_wallet = interest_data.get("interest_wallet", {}).get("interest_dinara", "")
	return interest_wallet

# Функция для сохранения данных в JSON файл
def save_eth_data(data):
	user_path = os.path.join("bin", "db", "eth_data.json")

	with open(user_path, "w", encoding="utf-8") as file:
		json.dump(data, file, ensure_ascii=False, indent=4)

def usd_formatted():
	# Получение ETH из JSON
	eth = get_eth_wallet()

	# Получение курса по рублю и доллару для ETH
	current_eth_to_usd_rate = get_eth_to_usd()

	# Расчет эквивалента в USD
	usd_equivalent = eth_to_usd(eth, current_eth_to_usd_rate)

	# Округление до двух знаков после запятой с использованием форматирования
	usd_equivalent_formatted = "{:.2f}".format(usd_equivalent)

	usd_formatted = usd_equivalent_formatted
	return usd_formatted

def rub_formatted():
	# Получение ETH из JSON
	eth = get_eth_wallet()

	# Получение курса по рублю и доллару для ETH
	current_eth_to_rub_rate = get_eth_to_rub()

	# Расчет эквивалента в RUB
	rub_equivalent = eth_to_rub(eth, current_eth_to_rub_rate)

	# Переводим в целое число рубль
	int_rub_equivalent = int(rub_equivalent)

	# Округление до двух знаков после запятой с использованием форматирования
	rub_equivalent_formatted = "{:,}".format(int_rub_equivalent).replace(",", " ")

	rub_formatted = rub_equivalent_formatted

	return rub_formatted

def rub_formatted_calculate():
	# Получение ETH из JSON
	eth = get_eth_wallet()

	# Получение курса по рублю и доллару для ETH
	current_eth_to_rub_rate = get_eth_to_rub()

	# Расчет эквивалента в RUB
	rub_equivalent = eth_to_rub(eth, current_eth_to_rub_rate)

	# Переводим в целое число рубль
	int_rub_equivalent = int(rub_equivalent)

	return int_rub_equivalent

def calculate_interest(message: types.Message):
	# Получаем % из JSON
	user_id = message.from_user.id
	user_data = check_user_data(user_id)
	interest = user_data.get("user_interest")

	# Получаем штрафы пользователя из JSON
	fines = user_data.get("fines")

	# Получаем общий бюджет из функции
	budget = rub_formatted_calculate()

	try:
		interest = int(interest)

		if fines > 0:
			result = fines * interest / 100

			return result
		else:
			budget_int = int(budget)

			interest_budget = interest / 2
			result_budget = budget_int * interest_budget / 100

			return result_budget
	except Exception:
		logging.exception("ERROR: 404 - ETH_DB: FUNC - CALCULATE_INTEREST")

def calculate_interest_call(callback_query: types.CallbackQuery):
	# Получаем % из JSON
	user = callback_query.from_user
	user_id = user.id
	user_data = check_user_data(user_id)
	interest = user_data.get("user_interest")

	# Получаем штрафы пользователя из JSON
	fines = user_data.get("fines")

	# Получаем общий бюджет из функции
	budget = rub_formatted_calculate()

	try:
		interest = float(interest)

		if fines > 0:
			result = fines * interest / 100

			return result
		else:
			budget_int = float(budget)

			interest_budget = interest / 2
			result_budget = budget_int * interest_budget / 100

			return result_budget
	except Exception:
		logging.exception("ERROR: 404 - ETH_DB: FUNC - CALCULATE_INTEREST_CALL")

def interest_fines(message: types.Message):
	# Получаем % из JSON
	user_id = message.from_user.id
	user_data = check_user_data(user_id)
	interest = user_data.get("user_interest")

	# Получаем штрафы пользователя из JSON
	fines = user_data.get("fines")

	try:
		if fines > 0:
			return interest
		else:
			interest_fines = interest / 2

			return interest_fines
	except Exception:
		logging.exception("ERROR: 404 - ETH_DB: FUNC - INTEREST_FINES")

def interest_fines_call(callback_query: types.CallbackQuery):
	# Получаем % из JSON
	user = callback_query.from_user
	user_id = user.id
	user_data = check_user_data(user_id)
	interest = user_data.get("user_interest")

	# Получаем штрафы пользователя из JSON
	fines = user_data.get("fines")

	try:
		if fines > 0:
			return interest
		else:
			interest_fines = interest / 2

			return interest_fines
	except Exception:
		logging.exception("ERROR: 404 - ETH_DB: FUNC - INTEREST_FINES_CALL")