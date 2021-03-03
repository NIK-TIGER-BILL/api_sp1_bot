import os
import time
import requests
import telegram
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
        level=logging.DEBUG,
        filename='main.log',
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s')
logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_logger.log', maxBytes=50000000,
                              backupCount=5)
logger.addHandler(handler)

API_YANDEX_URL = 'https://praktikum.yandex.ru/api/user_api/homework_statuses/'
PRAKTIKUM_TOKEN = os.getenv("PRAKTIKUM_TOKEN")
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def parse_homework_status(homework):
    homework_name = homework.get('homework_name')
    homework_status = homework.get('status')
    if homework_name is None or homework_status is None:
        return 'Пришли пустые данные, ошибка API'
    if homework_status == 'rejected':
        verdict = 'К сожалению в работе нашлись ошибки.'
    elif homework_status == 'approved':
        verdict = ('Ревьюеру всё понравилось, '
                   'можно приступать к следующему уроку.')
    else:
        return f'Работа {homework_name} взята на проверку'
    return f'У вас проверили работу "{homework_name}"!\n\n{verdict}'


def get_homework_statuses(current_timestamp):
    homework_statuses = requests.get(
        API_YANDEX_URL,
        headers={'Authorization': f'OAuth {PRAKTIKUM_TOKEN}'},
        params={'from_date': current_timestamp})
    return homework_statuses.json()


def send_message(message, bot_client):
    return bot_client.send_message(CHAT_ID, message)


def main():
    current_timestamp = int(time.time())
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    logging.debug('Бот запущен')
    while True:
        try:
            new_homework = get_homework_statuses(current_timestamp)
            if new_homework.get('homeworks'):
                logger.info(new_homework.get('homeworks')[0])
                send_message(
                    parse_homework_status(new_homework.get('homeworks')[0]),
                    bot)
            current_timestamp = new_homework.get('current_date',
                                                 current_timestamp)
            time.sleep(300)
        except Exception as e:
            logger.exception('')
            send_message(f'Бот столкнулся с ошибкой: {e}', bot)
            time.sleep(5)


if __name__ == '__main__':
    main()
