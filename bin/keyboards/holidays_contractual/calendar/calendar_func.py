from misc.util import types, calendar, FSMContext, logging
from misc.loader import dp

from datetime import datetime

from data.base_glossary import MONTH_NAMES_RU, SPECIAL_DATES
from data import yml_loader

async def generate_calendar_markup(year, month, user_day=None):
    inline_keyboard = types.InlineKeyboardMarkup()

    prev_month = month - 1 if month > 1 else 12
    next_month = month + 1 if month < 12 else 1

    inline_keyboard.row(
        types.InlineKeyboardButton("⬅️", callback_data=f"month-{prev_month}"),
        types.InlineKeyboardButton(f"{MONTH_NAMES_RU[month - 1]}", callback_data="current"),
        types.InlineKeyboardButton("➡️", callback_data=f"month-{next_month}")
    )

    days_in_month = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month != 2 else 29 if calendar.isleap(year) else 28
    day = 1
    while day <= days_in_month:
        row = []
        for _ in range(7):
            if day > days_in_month:
                break
            callback_data = f"{year}-{month:02d}-{day:02d}"
            emoji_data = SPECIAL_DATES.get(callback_data, None)  # Получаем данные для эмодзи из словаря

            # Получаем текущую дату и проверяем, является ли текущий день равным дате в календаре
            now = datetime.now()
            current_day = now.day
            current_month = now.month
            current_year = now.year

            if day == current_day and month == current_month and year == current_year:
                # Если день совпадает с текущей датой пользователя, добавляем звездочку перед числом дня
                if emoji_data:
                    row.append(types.InlineKeyboardButton(f"•{emoji_data['emoji']}•", callback_data=f"text-{callback_data}"))
                else:
                    row.append(types.InlineKeyboardButton(f"•{day}•", callback_data=f"date-{callback_data}"))
            else:
                if emoji_data:
                    row.append(types.InlineKeyboardButton(emoji_data['emoji'], callback_data=f"text-{callback_data}"))
                else:
                    row.append(types.InlineKeyboardButton(str(day), callback_data=f"date-{callback_data}"))
            day += 1
        inline_keyboard.row(*row)

    return inline_keyboard

async def handle_start(message: types.Message, state: FSMContext):
    # Получаем текущую дату
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    await message.answer(yml_loader.calendar_path["calendar"]["calendar_info"], reply_markup=await generate_calendar_markup(current_year, current_month))
    await state.set_data({"year": current_year, "month": current_month})

async def generate_selected_calendar_markup(year, month, day):
    # Генерируем календарь с соответствующей пометкой
    inline_keyboard = await generate_calendar_markup(year, month, user_day=datetime(year, month, day))

    return inline_keyboard

@dp.callback_query_handler(lambda call: call.data.startswith('text-'))
async def handle_text_selection(call: types.CallbackQuery, state: FSMContext):
    try:
        callback_data = call.data[len('text-'):]
        emoji_data = SPECIAL_DATES.get(callback_data, None)
        if emoji_data:
            year, month, day = map(int, callback_data.split('-'))
            inline_keyboard = await generate_selected_calendar_markup(year, month, day)
            await call.message.edit_text(emoji_data['text'], reply_markup=inline_keyboard)
        else:
            year, month, day = map(int, callback_data.split('-'))
            selected_date = f"{day:02d}.{month:02d}.{year}"
            await call.message.answer(f"Вы выбрали: {selected_date}")
        await call.answer()
    except Exception:
        logging.exception("Ошибочка")

@dp.callback_query_handler(lambda call: call.data.startswith('month-'))
async def handle_month_selection(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    year = data.get('year', 2023)
    month = int(call.data.split('-')[1])
    user_day = data.get('user_day', None)  # Получаем выбранную пользователем дату из состояния

    # Обновляем состояние с текущим годом и месяцем
    await state.update_data(year=year, month=month)

    # Вызываем обработчик выбора даты снова, чтобы обновить выбранную пользователем дату в состоянии
    if user_day:
        # Форматируем день пользователя для соответствия формату callback_data в handle_date_selection
        formatted_user_day = f"{year}-{month:02d}-{int(user_day.split('.')[0]):02d}"
        await handle_date_selection(types.CallbackQuery(data=f"date-{formatted_user_day}"), state)

    # Генерируем календарь с соответствующей пометкой
    await call.message.edit_text(yml_loader.calendar_path["calendar"]["calendar_info"], reply_markup=await generate_calendar_markup(year, month, user_day=user_day))
    await call.answer()

@dp.callback_query_handler(lambda call: call.data.startswith('date-'))
async def handle_date_selection(call: types.CallbackQuery, state: FSMContext):
    try:
        year, month, day = map(int, call.data.split('-')[1:])
        selected_date = f"{day:02d}.{month:02d}.{year}"
        await call.message.answer(f"Вы выбрали: {selected_date}")
        await call.answer()
        await state.finish()  # Завершаем состояние после выбора даты
    except Exception:
        logging.exception("Ошибочка")