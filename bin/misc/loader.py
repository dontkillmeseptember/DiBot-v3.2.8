from misc.util import Bot, MemoryStorage, Dispatcher, pytz, AsyncIOScheduler, LoggingMiddleware

from data.config import BOT_TOKEN

# Переменная для бота где bot(token = "Ваш токен бота")
bot = Bot(token=BOT_TOKEN, parse_mode="HTML", disable_web_page_preview=True)

# Переменная для хранилища данных
storage = MemoryStorage()

# Создание планировщика задач
scheduler = AsyncIOScheduler()

# Переменная для диспетчера
dp = Dispatcher(bot, storage=storage)

# Отправляет в консоль user_id польвазетей которые отправили сообщения в чат
dp.middleware.setup(LoggingMiddleware())

# Создание ожидание времени для всех пользователей
moscow_tz = pytz.timezone('Europe/Moscow')