from misc.util import BaseMiddleware, logging, os

# Определите путь к файлу логов
log_file_path = os.path.join(os.path.dirname(__file__), 'message_logs.txt')

# Создайте логгер
logger = logging.getLogger("user info")
logger.setLevel(logging.INFO)

# Создайте обработчик для записи логов в файл
file_handler = logging.FileHandler(log_file_path, encoding='utf-8')  # Используем utf-8 кодировку

# Создайте форматтер для указания формата записей в логах
formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавьте обработчик к логгеру
logger.addHandler(file_handler)

# Регистрируем ваш middleware
class LogMiddleware(BaseMiddleware):
	async def on_pre_process_message(self, message, data):
		user_id = message.from_user.id
		user_username = message.from_user.username
		user_first_name = message.from_user.first_name
		text = message.text

		# Выводим информацию в консоль (которая теперь перенаправляется в файл)
		log_message = f"Пользователь с ID {user_id}, никнейм {user_username}, имя пользователя {user_first_name}, отправил сообщение: {text}"
		logger.info(log_message)
