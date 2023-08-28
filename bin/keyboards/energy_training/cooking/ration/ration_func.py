from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, datetime, json, os
from misc.loader import bot

from data import yml_loader

# Обновляем функцию get_current_weekday() для правильного определения текущего дня недели.
def get_current_weekday():
	# Здесь используется модуль datetime для получения текущего дня недели.
	# Возвращаемое значение: 0 (понедельник) до 6 (воскресенье).
	# Мы будем использовать значение 0 (понедельник) до 6 (воскресенье) в качестве индекса дня недели.
	return datetime.datetime.now().weekday()

# Изменим функцию ration_handler.
async def ration_handler(message: types.Message):
    # Создаем клавиатуру с вкладками
    inline_keyboard = InlineKeyboardMarkup()

    current_weekday = get_current_weekday()

    # В понедельник не создаем кнопку вообще
    if current_weekday != 0:
        days = [
            {"button": None, "text": "monday"},
            {"button": "monday", "text": "tuesday"},
            {"button": "tuesday", "text": "wednesday"},
            {"button": "wednesday", "text": "thursday"},
            {"button": "thursday", "text": "friday"},
            {"button": "friday", "text": "saturday"},
            {"button": "saturday", "text": "sunday"}
        ]

        # Добавляем кнопки для каждого дня недели, кроме понедельника
        for i, day in enumerate(days):
            if i == current_weekday:
                # Если это текущий день, добавляем текст рациона для этого дня
                await message.answer(yml_loader.ration_data["ration_info"]["ration_" + day["text"]], reply_markup=inline_keyboard)
            elif i == (current_weekday - 1) % 7:
                    inline_keyboard.row(
                        InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_" + day["text"]], callback_data=f"backward_{day['text']}")
                    )
    else:
        # В понедельник отправляем текст рациона без кнопок
        await message.answer(yml_loader.ration_data["ration_info"]["ration_monday"])

# Асинхронная функция для обработки недельного запроса о рационе
async def ration_weekly_callback(message: types.Message):
    user_id = message.from_user.id
    file_path = os.path.join("bin", "db", "subscribers.json")
    
    with open(file_path, "r") as file:
        subscribers_data = json.load(file)
    
    user_data = subscribers_data.get(str(user_id), {})
    has_visited_ration = user_data.get("has_visited_ration", False)
    
    if not has_visited_ration:
        # Если пользователь еще не посещал вкладку, отправляем текст с кнопками для рациона на текущий день.
        await ration_handler(message)
        # После отправки рациона на текущий день устанавливаем флаг has_visited_ration в JSON файле в True.
        user_data["has_visited_ration"] = True
        subscribers_data[str(user_id)] = user_data
        with open(file_path, "w") as file:
            json.dump(subscribers_data, file, indent=4)
    else:
        # Если пользователь уже посещал вкладку, отправляем только текст с текущим рационом.
        await ration_handler(message)

# Функция для установки ежедневного сброса флага has_visited_ration
async def daily_reset_has_visited_ration():
    file_path = os.path.join("bin", "db", "subscribers.json")
    
    with open(file_path, "r") as file:
        subscribers_data = json.load(file)
    
    for user_id, user_data in subscribers_data.items():
        user_data["has_visited_ration"] = False
    
    with open(file_path, "w") as file:
        json.dump(subscribers_data, file, indent=4)

# Обработчик кнопки "Следующий день: Вторник"
async def process_callback_forward_tuesday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_monday"], callback_data="backward_monday"))

	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_tuesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)
	
# Обработчик кнопки "Предыщищий день: Понедельник"
async def process_callback_backward_monday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_tuesday"], callback_data="forward_tuesday"))
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_monday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Следующий день: Среда"
async def process_callback_forward_wednesday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_tuesday"], callback_data="backward_tuesday"))

	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_wednesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Предыщищий день: Вторник"
async def process_callback_backward_tuesday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_monday"], callback_data="backward_monday_two"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_wednesday"], callback_data="forward_wednesday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_tuesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_monday_two(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_tuesday"], callback_data="backward_tuesday"))
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_monday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Следующий день: Четверг"
async def process_callback_forward_thursday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_wednesday"], callback_data="backward_wednesday"))

	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_thursday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Предыщищий день: Среда"
async def process_callback_backward_wednesday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_tuesday"], callback_data="backward_tuesday_two"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_thursday"], callback_data="forward_thursday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_wednesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_tuesday_two(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_monday"], callback_data="backward_monday_three"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_wednesday"], callback_data="backward_wednesday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_tuesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_monday_three(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_tuesday"], callback_data="backward_tuesday_two"))
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_monday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Следующий день: Пятница"
async def process_callback_forward_friday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_thursday"], callback_data="backward_thursday"))

	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_friday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Предыщищий день: Четверг"
async def process_callback_backward_thursday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_wednesday"], callback_data="backward_wednesday_two"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_friday"], callback_data="forward_friday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_thursday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_wednesday_two(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_tuesday"], callback_data="backward_tuesday_three"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_thursday"], callback_data="backward_thursday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_wednesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_tuesday_three(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_monday"], callback_data="backward_monday_four"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_wednesday"], callback_data="backward_wednesday_two")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_tuesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_monday_four(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_tuesday"], callback_data="backward_tuesday_three"))
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_monday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Следующий день: Суббота"
async def process_callback_forward_saturday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_friday"], callback_data="backward_friday"))

	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_saturday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Предыщищий день: Пятница"
async def process_callback_backward_friday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_thursday"], callback_data="backward_thursday_two"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_saturday"], callback_data="forward_saturday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_friday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_thursday_two(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_wednesday"], callback_data="backward_wednesday_three"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_friday"], callback_data="backward_friday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_thursday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_wednesday_three(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_tuesday"], callback_data="backward_tuesday_four"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_thursday"], callback_data="backward_thursday_two")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_wednesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_tuesday_four(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_monday"], callback_data="backward_monday_five"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_wednesday"], callback_data="backward_wednesday_three")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_tuesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_monday_five(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_tuesday"], callback_data="backward_tuesday_four"))
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_monday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

# Обработчик кнопки "Следующий день: Воскресенье"
async def process_callback_forward_sunday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_saturday"], callback_data="backward_saturday"))

	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_sunday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)
		
# Обработчик кнопки "Предыщищий день: Суббота"
async def process_callback_backward_saturday(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_friday"], callback_data="backward_friday_two"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_sunday"], callback_data="forward_sunday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_saturday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_friday_two(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_thursday"], callback_data="backward_thursday_three"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_saturday"], callback_data="backward_saturday")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_friday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_thursday_three(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_wednesday"], callback_data="backward_wednesday_four"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_friday"], callback_data="backward_friday_two")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_thursday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_wednesday_four(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_tuesday"], callback_data="backward_tuesday_five"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_thursday"], callback_data="backward_thursday_three")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_wednesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_tuesday_five(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_backward_monday"], callback_data="backward_monday_six"),
		InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_wednesday"], callback_data="backward_wednesday_four")
	)
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_tuesday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)

async def process_callback_backward_monday_six(callback_query: types.CallbackQuery):
	# Создаем клавиатуру с вкладками
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.add(InlineKeyboardButton(yml_loader.ration_data["buttons"]["button_forward_tuesday"], callback_data="backward_tuesday_five"))
	
	await bot.edit_message_text(yml_loader.ration_data["ration_info"]["ration_monday"], callback_query.from_user.id, callback_query.message.message_id, reply_markup=inline_keyboard)
