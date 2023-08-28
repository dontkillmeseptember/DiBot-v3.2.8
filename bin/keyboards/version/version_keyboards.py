from data import yml_loader

from misc.loader import dp

from keyboards.version.version_func import (
    version_handler,
    update_zero_zero_one_handler,
    update_zero_zero_two_handler,
    update_zero_zero_three_handler
)

# Кнопка "Обновления бота"
dp.register_message_handler(version_handler, lambda message: message.text == yml_loader.version_data["version"]["button_update"])

# Кнопка "Обновление за 01.09.2023"
dp.register_message_handler(update_zero_zero_three_handler, lambda message: message.text == yml_loader.version_data["version_0_0_3"]["button_update_september_zero_zero_three"])

# Кнопка "Обновление за 06.08.2023"
dp.register_message_handler(update_zero_zero_two_handler, lambda message: message.text == yml_loader.version_data["version_0_0_2"]["button_update_jule_zero_zero_two"])

# Кнопка "Обновление за 17.07.2023"
dp.register_message_handler(update_zero_zero_one_handler, lambda message: message.text == yml_loader.version_data["version_0_0_1"]["button_update_jule_zero_zero_one"])