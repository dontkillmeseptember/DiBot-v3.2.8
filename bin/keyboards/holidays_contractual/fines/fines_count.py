from misc.util import requests, reduce

# Всего штрафов у Игоря
# Входные данные
fines_igor_one = 30000
fines_igor_two = 4700
fines_igor_three = 0
full_igor_one = 20
full_igor_two = 22
full_igor_three = 0

# Проверка значения full_one
if full_igor_one > 15:
    full_igor_one += 7

# Проверка значения full_two
if full_igor_two > 15:
    full_igor_two += 7
    
# Проверка значения full_igor_three
if full_igor_three > 15:
    full_igor_three += 7

# Вычисление суммы с учетом процентов для fines_one
interest_one = 1 + full_igor_one / 100
result_one = fines_igor_one * interest_one

# Вычисление суммы с учетом процентов для fines_two
interest_two = 1 + full_igor_two / 100
result_two = fines_igor_two * interest_two

# Вычисление суммы с учетом процентов для fines_igor_three
interest_three = 1 + fines_igor_three / 100
result_three = fines_igor_three * interest_two

# Сложение результатов
result = reduce(
    lambda x, y: x + y,
    map(int, (result_one, result_two, result_three))
)

# Преобразование результата в целое число
result, int_result_one, int_result_two, int_result_three = map(int, (result, result_one, result_two, result_three))

# Форматирование числа с пробелами
formatted_result = "{:,}".format(result).replace(",", " ")
formated_result_one = "{:,}".format(int_result_one).replace(",", " ")
formated_result_two = "{:,}".format(int_result_two).replace(",", " ")
formated_result_three = "{:,}".format(int_result_three).replace(",", " ")

igor_fines_account = f"💷 {formatted_result}"

# Сумма всех штрафов
# Входные данные
fines_igor = [8200, 6790, 10300, 36000, 1120, 840, 11750]

# Сложение результатов
all_fines = reduce(
	lambda c, b: c + b,
	fines_igor
)

# Преобразование результата в целое число
all_fines = int(all_fines)

# Форматирование числа с пробелами
formatted_all_fines = "{:,}".format(all_fines).replace(",", " ")

igor_all_fines = f"💷 {formatted_all_fines}"

# Всегош штрафов у Вячеслава
# Входные данные
fines_slava_one = 0
fines_slava_two = 0
full_slava_one = 0
full_slava_two = 0

# Проверка значения full_one
if full_slava_one > 15:
    full_slava_one += 7

# Проверка значения full_two
if full_slava_two > 15:
    full_slava_two += 7

# Вычисление суммы с учетом процентов для fines_one
interest_one_slava = 1 + full_slava_one / 100
result_one_slava = fines_slava_one * interest_one_slava

# Вычисление суммы с учетом процентов для fines_two
interest_two_slava = 1 + full_slava_two / 100
result_two_slava = fines_slava_two * interest_two_slava

# Сложение результатов
result_slava = result_one_slava + result_two_slava

# Преобразование результата в целое число
result_slava = int(result_slava)

# Форматирование числа с пробелами
formatted_result_slava = "{:,}".format(result_slava).replace(",", " ")

slava_fines_account = f"💷 {formatted_result_slava}"

# Сумма всех штрафов
# Входные данные
fines_slava = [0, 0]

# Сложение результатов
all_fines_slava = reduce(
    lambda h, d: h + d,
    fines_slava
)

# Преобразование результата в целое число
all_fines_slava = int(all_fines_slava)

# Форматирование числа с пробелами
formatted_all_fines_slava = "{:,}".format(all_fines_slava).replace(",", " ")

slava_all_fines = f"💷 {formatted_all_fines_slava}"

# Рассчет ETH в рубль и доллар
def get_eth_to_usd_rate():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    eth_to_usd_rate = data.get("ethereum", {}).get("usd")
    return eth_to_usd_rate

def get_eth_to_rub_rate():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=rub"
    response = requests.get(url)
    data = response.json()
    eth_to_rub_rate = data.get("ethereum", {}).get("rub")
    return eth_to_rub_rate

def eth_to_usd(eth_amount, eth_to_usd_rate):
    usd_amount = eth_amount * eth_to_usd_rate
    return usd_amount


def eth_to_rub(eth_amount, eth_to_rub_rate):
    rub_amount = eth_amount * eth_to_rub_rate
    return rub_amount

# Получение актуального курса ETH/USD с CoinGecko
current_eth_to_usd_rate = get_eth_to_usd_rate()
current_eth_to_rub_rate = get_eth_to_rub_rate()

# Замените эту сумму на нужное количество ETH
amount_in_eth = 1.709

# Расчет эквивалента в USD
usd_equivalent = eth_to_usd(amount_in_eth, current_eth_to_usd_rate)
rub_equivalent = eth_to_rub(amount_in_eth, current_eth_to_rub_rate)

# Переводим в целое число рубль
int_rub_equivalent = int(rub_equivalent)

# Округление до двух знаков после запятой с использованием форматирования
usd_equivalent_formatted = "{:.2f}".format(usd_equivalent)
rub_equivalent_formatted = "{:,}".format(int_rub_equivalent).replace(",", " ")