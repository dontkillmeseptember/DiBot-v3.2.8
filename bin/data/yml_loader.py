from misc.util import Path, datetime, yaml
from misc.loader import moscow_tz

from data.version_db import get_bot_version
from data.config import (
    # Переменные для версий
    VERSION_17_07,
    VERSION_06_08,
    VERSION_14_08,
    VERSION_19_08,
    VERSION_01_09,
    VERSION_30_08,
    VERSION_03_09,
    # Переменные для ведьмаков
    WITCHER_1,
    WITCHER_2,
    WITCHER_3
)

from keyboards.holidays_contractual.fines.fines_count import (
    igor_fines_account, slava_fines_account, 
    igor_all_fines, slava_all_fines,
    formated_result_one, full_igor_one,
    formated_result_two, full_igor_two,
    formated_result_three, full_igor_three,
    amount_in_eth, usd_equivalent_formatted,
    rub_equivalent_formatted
)

# Получение текущий версии
bot_version = get_bot_version()

# Для всех вкладок
# Получаем текущее время в указанной временной зоне
current_datetime = datetime.datetime.now(moscow_tz)
current_weekday = current_datetime.weekday()
days_until_next_monday = (7 - current_weekday)

# Получаем дату следующего понедельника
next_monday = current_datetime + datetime.timedelta(days=days_until_next_monday)
target_datetime = datetime.datetime(next_monday.year, next_monday.month, next_monday.day, hour=0, minute=0, second=0)
target_datetime = moscow_tz.localize(target_datetime)

time_diff = target_datetime - current_datetime

# Форматируем время до следующего понедельника в удобный формат
formatted_days = f"{time_diff.days}"
formatted_hours = f"{time_diff.seconds // 3600}"

# Для колеса фортуны
# Получаем текущее время в указанной временной зоне
current_datetime_casino = datetime.datetime.now(moscow_tz)
current_weekday_casino = current_datetime_casino.weekday()
days_until_next_monday_casino = (7 - current_weekday_casino)

# Получаем дату следующего понедельника
next_monday_casino = current_datetime_casino + datetime.timedelta(days=days_until_next_monday_casino, weeks=1)
target_datetime_casino = datetime.datetime(next_monday_casino.year, next_monday_casino.month, next_monday_casino.day)
target_datetime_casino = moscow_tz.localize(target_datetime_casino)

time_diff_casino = target_datetime_casino - current_datetime_casino

# Форматируем время до следующего понедельника в удобный формат
formatted_days_casino = f"{time_diff_casino.days}"
formatted_hours_casino = f"{time_diff_casino.seconds // 3600}"

# Русский язык
# Общий путь к файлам
messages_dir = Path(__file__).parent.parent.resolve()

# Путь к файлу main.yml
main_path = messages_dir.joinpath("messages", "ru", "main_string")

# Загрузить start_bot.yml
with open(main_path / "main.yml", "r", encoding="utf-8") as f:
    main_path = yaml.safe_load(f)

# Путь к файлу start_bot.yml
start_bot_path = messages_dir.joinpath("messages", "ru", "handlers_string")

# Загрузить start_bot.yml
with open(start_bot_path / "start_bot.yml", "r", encoding="utf-8") as f:
    start_bot_path = yaml.safe_load(f)
    
# Путь к файлу energy_training.yml
energy_training_path = messages_dir.joinpath("messages", "ru", "keyboards_string", "energy_training.yml")

# Загрузить energy_training.yml
with open(energy_training_path, "r", encoding="utf-8") as f:
    energy_training_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in energy_training_data.items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{days}}", formatted_days).replace("{{hours}}", formatted_hours).strip()
        energy_training_data[key] = value

# Путь к файлу holidays_contractual.yml
holidays_contractual_path = messages_dir.joinpath("messages", "ru", "keyboards_string")

# Загрузить holidays_contractual.yml
with open(holidays_contractual_path / "holidays_contractual.yml", "r", encoding="utf-8") as f:
    holidays_contractual_path = yaml.safe_load(f)

# Путь к файлу quest.yml
quest_path = messages_dir.joinpath("messages", "ru", "quest_string", "quest.yml")

# Загрузить quest.yml
with open(quest_path, "r", encoding="utf-8") as f:
    quest_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in quest_data["quest"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{witcherone}}", str(WITCHER_1)).replace("{{witchertwo}}", str(WITCHER_2)).replace("{{witcherthree}}", str(WITCHER_3)).strip()
        quest_data["quest"][key] = value

# Путь к файлу update.yml
update_path = messages_dir.joinpath("messages", "ru", "update_string", "update.yml")

# Загрузить update.yml
with open(update_path, "r", encoding="utf-8") as f:
    update_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in update_data["update_bot"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{version}}", str(bot_version)).strip()
        update_data["update_bot"][key] = value

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in update_data["loading"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{version}}", str(bot_version)).strip()
        update_data["loading"][key] = value

# Путь к файлу version.yml
version_path = messages_dir.joinpath("messages", "ru", "version_string", "version.yml")

# Загрузить version.yml
with open(version_path, "r", encoding="utf-8") as f:
    version_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in version_data["version"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{version}}", str(bot_version)).strip()
        version_data["version"][key] = value

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in version_data["version_0_0_1"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{version_one}}", str(VERSION_17_07)).strip()
        version_data["version_0_0_1"][key] = value

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in version_data["version_0_0_2"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{version_two}}", str(VERSION_06_08)).replace("{{version_three}}", str(VERSION_14_08)).replace("{{version_four}}", str(VERSION_19_08)).strip()
        version_data["version_0_0_2"][key] = value

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in version_data["version_0_0_3"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{version_five}}", str(VERSION_01_09)).replace("{{version_six}}", str(VERSION_30_08)).replace("{{version_seven}}", str(VERSION_03_09)).strip()
        version_data["version_0_0_3"][key] = value

# Путь к файлу language.yml
language_path = messages_dir.joinpath("messages", "ru", "language.yml")

# Загрузить language.yml
with open(language_path, "r", encoding="utf-8") as f:
    language_path = yaml.safe_load(f)

# Путь к файлу mailings.yml
mailings_path = messages_dir.joinpath("messages", "ru", "handlers_string")

# Загрузить mailings.yml
with open(mailings_path / "mailings.yml", "r", encoding="utf-8") as f:
    mailings_path = yaml.safe_load(f)

# Путь к файлу calendar.yml
calendar_path = messages_dir.joinpath("messages", "ru", "calendar_string")

# Загрузить calendar.yml
with open(calendar_path / "calendar.yml", "r", encoding="utf-8") as f:
    calendar_path = yaml.safe_load(f)

# Путь к файлу fines.yml
fines_path = messages_dir.joinpath("messages", "ru", "fines_string", "fines.yml")

# Замена переменных для Игоря
fines_igor = f"{igor_fines_account}"
fines_all_igor = f"{igor_all_fines}"

# Замена переменных для Славы
fines_slava = f"{slava_fines_account}"
fines_all_slava = f"{slava_all_fines}"

# Загрузить fines.yml
with open(fines_path, "r", encoding="utf-8") as f:
    fines_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in fines_data["fines_igor"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{igor}}", str(fines_igor)).replace("{{igorfull}}", str(igor_all_fines)).replace("{{resultone}}", str(formated_result_one)).replace("{{rate_one}}", str(full_igor_one)).replace("{{resulttwo}}", str(formated_result_two)).replace("{{rate_two}}", str(full_igor_two)).replace("{{resultthree}}", str(formated_result_three)).replace("{{rate_three}}", str(full_igor_three)).replace("{{eth}}", str(amount_in_eth)).replace("{{usd}}", str(usd_equivalent_formatted)).replace("{{rub}}", str(rub_equivalent_formatted)).strip()
        fines_data["fines_igor"][key] = value

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in fines_data["fines_slava"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{slava}}", fines_slava).replace("{{slavafull}}", fines_all_slava).strip()
        fines_data["fines_slava"][key] = value

# Путь к файлу contract.yml
contract_path = messages_dir.joinpath("messages", "ru", "contract_string")

# Загрузить contract.yml
with open(contract_path / "contract.yml", "r", encoding="utf-8") as f:
    contract_path = yaml.safe_load(f)

# Путь к файлу contract_slava.yml
contract_slava_path = messages_dir.joinpath("messages", "ru", "contract_string")

# Загрузить contract_slava.yml
with open(contract_slava_path / "contract_slava.yml", "r", encoding="utf-8") as f:
    contract_slava_path = yaml.safe_load(f)

# Путь к файлу news.yml
news_path = messages_dir.joinpath("messages", "ru", "news_string")

# Загрузить news.yml
with open(news_path / "news.yml", "r", encoding="utf-8") as f:
    news_path = yaml.safe_load(f)

# Путь к файлу news.yml
news_life_path = messages_dir.joinpath("messages", "ru", "news_string")

# Загрузить news.yml
with open(news_life_path / "news_life.yml", "r", encoding="utf-8") as f:
    news_life_path = yaml.safe_load(f)

# Путь к файлу news.yml
news_igor_path = messages_dir.joinpath("messages", "ru", "news_string")

# Загрузить news.yml
with open(news_igor_path / "news_igor.yml", "r", encoding="utf-8") as f:
    news_igor_path = yaml.safe_load(f)

# Путь к файлу sport.yml
sport_path = messages_dir.joinpath("messages", "ru", "sport_string", "sport.yml")

# Загрузить sport.yml
with open(sport_path, "r", encoding="utf-8") as f:
    sport_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in sport_data["sport"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{days}}", formatted_days).replace("{{hours}}", formatted_hours).strip()
        sport_data["sport"][key] = value

# Путь к файлу ration.yml
ration_path = messages_dir.joinpath("messages", "ru", "ration_string", "ration.yml")

# Загрузить содержимое ration.yml
with open(ration_path, "r", encoding="utf-8") as f:
    ration_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in ration_data["ration_info"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{days}}", formatted_days).replace("{{hours}}", formatted_hours).strip()
        ration_data["ration_info"][key] = value

# Путь к файлу admin.yml
admin_path = messages_dir.joinpath("messages", "ru", "handlers_string")

# Загрузить admin.yml
with open(admin_path / "admin.yml", "r", encoding="utf-8") as f:
    admin_path = yaml.safe_load(f)

# Путь к файлу casino.yml
casino_path = messages_dir.joinpath("messages", "ru", "casino_string")

# Загрузить casino.yml
with open(casino_path / "casino.yml", "r", encoding="utf-8") as f:
    casino_path = yaml.safe_load(f)

# Путь к файлу cooking.yml
cooking_path = messages_dir.joinpath("messages", "ru", "keyboards_string", "cooking.yml")

# Загрузить cooking.yml
with open(cooking_path, "r", encoding="utf-8") as f:
    cooking_data = yaml.safe_load(f)

# Заменяем переменные в YAML-файле с помощью метода safe_load
for key, value in cooking_data["cooking"].items():
    if isinstance(value, str) and "{{" in value and "}}" in value:
        # Заменяем ключевые слова "{{days}}" и "{{hours}}" на соответствующие значения
        value = value.replace("{{days_casino}}", formatted_days_casino).replace("{{hours_casino}}", formatted_hours_casino).strip()
        cooking_data["cooking"][key] = value

# Путь к файлу notices.yml
notices_path = messages_dir.joinpath("messages", "ru", "handlers_string")

# Загрузить notices.yml
with open(notices_path / "notices.yml", "r", encoding="utf-8") as f:
    notices_path = yaml.safe_load(f)

# Путь к файлу notices.yml
role_path = messages_dir.joinpath("messages", "ru", "role_string")

# Загрузить notices.yml
with open(role_path / "role.yml", "r", encoding="utf-8") as f:
    role_path = yaml.safe_load(f)