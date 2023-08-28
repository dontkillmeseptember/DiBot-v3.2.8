from handlers.main import all_users, all_admin
from keyboards.main import all_keyboards

# Функция для импорта всех функций из отдельных папок
async def functions_all(message, bot):
    await all_users(message)
    await all_admin(message)
    await all_keyboards(message, bot)