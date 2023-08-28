from misc.util import InlineKeyboardMarkup, InlineKeyboardButton, types, FSMContext, Text
from misc.loader import dp, bot

from data.start_db import load_user_data, is_user_in_data, save_user_data
from data import yml_loader

from keyboards.holidays_contractual.contract.contract_old_func import contract_start_old_interface, contract_start_old_interface_select
from keyboards.holidays_contractual.contract.contract_new_func import contract_start_new_interface, contract_start_new_interface_select

# Обработчик для кнопок вкладки "Договор"
async def contract_handler(message: types.Message):
	user_id = message.from_user.id
	user_data = load_user_data()

	if is_user_in_data(user_id, user_data):
		# Проверяем, есть ли уже выбранный интерфейс у пользователя
		if str(user_id) in user_data and "interface_contract" in user_data[str(user_id)]:
			selected_interface = user_data[str(user_id)]["interface_contract"]
			
			if selected_interface == "old_interface":
				await contract_start_old_interface_select(message)
			elif selected_interface == "new_interface":
				await contract_start_new_interface_select(message)
			elif selected_interface is None:
				await contract_start_no_interface(message)

	else:
		print("User not registor.")

# Обработчик если пользователь не выбрал интерфейс
async def contract_start_no_interface(message: types.Message):
	inline_keyboard = InlineKeyboardMarkup()
	inline_keyboard.row(
		InlineKeyboardButton(yml_loader.contract_path["contraft_interface"]["old_interface"], callback_data="old_interface"),
		InlineKeyboardButton(yml_loader.contract_path["contraft_interface"]["new_interface"], callback_data="new_interface")
	)

	await message.answer(yml_loader.contract_path["contraft_interface"]["interface_info"], reply_markup=inline_keyboard)

# Обработчик для выбора старого интерфейса
@dp.callback_query_handler(Text(startswith="old_interface"), state="*")
async def save_old_interface(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора интерфейса в user_data
	user_data[str(user_id)]["interface_contract"] = "old_interface"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.contract_path["contraft_interface"]["text_old_interface"])
	
	await contract_start_old_interface(callback_query)

# Обработчик для выбора нового интерфейса
@dp.callback_query_handler(Text(startswith="new_interface"), state="*")
async def save_new_interface(callback_query: types.CallbackQuery, state: FSMContext):
	user_id = callback_query.from_user.id
	user_data = load_user_data()

	# Сохранение выбора интерфейса в user_data
	user_data[str(user_id)]["interface_contract"] = "new_interface"
	save_user_data(user_data)

	await bot.answer_callback_query(callback_query.id, text=yml_loader.contract_path["contraft_interface"]["text_new_interface"])

	await contract_start_new_interface(callback_query)