from data import yml_loader
from misc.loader import dp

from keyboards.main_menu import main_menu

from handlers.users.profile import profile_command

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Главное меню"
dp.register_message_handler(main_menu, lambda message: message.text == yml_loader.main_path["main_menu"]["button_main_menu"])

# Кнопка "Ваш профиль"
dp.register_message_handler(profile_command, lambda message: message.text == "💀 Ваш профиль — 0/60")

# Кнопка "Ваш профиль с прогрессом"
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 0/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 1/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 2/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 3/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 4/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 5/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 6/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 7/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 8/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 9/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 10/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 11/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 12/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 13/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 14/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 15/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 16/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 17/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 18/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 19/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 20/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 20/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 21/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 22/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🤵🏻 Ваш профиль — 23/60")


dp.register_message_handler(profile_command, lambda message: message.text == "🐋 Ваш профиль — 0/60")
dp.register_message_handler(profile_command, lambda message: message.text == "🐈 Ваш профиль — 0/60")