from data import yml_loader
from misc.loader import dp

from keyboards.main_menu import main_menu

from handlers.users.profile import profile_command

# Свяжите функции обработки сообщений с диспетчером
# Кнопка "Главное меню"
dp.register_message_handler(main_menu, lambda message: message.text == yml_loader.main_path["main_menu"]["button_main_menu"])

# Кнопка "Ваш профиль"
text_options = ["🤵🏻 Ваш профиль —", 
                "🐈 Ваш профиль —", 
                "💀 Ваш профиль —", 
                "🐋 Ваш профиль —"]

for text in text_options:
    for progress in range(61):
        full_text = f"{text} {progress}/60"
        dp.register_message_handler(profile_command, lambda message, text=full_text: message.text == text)

