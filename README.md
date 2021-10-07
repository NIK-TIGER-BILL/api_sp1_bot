# Telegram-bot
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/-Telegram-464646?style=flat-square&logo=Telegram)](https://pypi.org/project/python-telegram-bot/)
[![Heroku](https://img.shields.io/badge/-Heroku-464646?style=flat-square&logo=Heroku)](https://www.heroku.com/)

Данный бот оповещает пользователя о проверенной работе. В случаи ошибки, пришлет исключение сообщением в чат.
Его я располагал на бесплатном сервисе [Heroku](https://www.heroku.com/). Для этого, в репозитории уже лежит Procfile. Вы можете выбрать любой другой удобный для вас.

## Переменные окружения:  
* `API_YANDEX_URL`  url адрес сервера api яндекс практикума
* `PRAKTIKUM_TOKEN` токен аутентификации Яндекс.Практикума
* `TELEGRAM_TOKEN`  телеграмм токен созданного вами бота
* `CHAT_ID`         id чата с вами

*Токен можно получить по адресу: https://oauth.yandex.ru/authorize?response_type=token&client_id=<client_id>, где client_id, id пользователя*


