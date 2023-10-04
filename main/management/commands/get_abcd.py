import requests
import json
from django.core.management import BaseCommand
from main.models import FrameworkModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Ссылка на данные
        url = "https://api.npoint.io/ab1d335a31210c153bd1"

        # Отправка GET-запроса и получение ответа
        response = requests.get(url)

        # Проверка успешности запроса
        if response.status_code == 200:
            # Декодирование JSON-данных из ответа
            data = json.loads(response.text)

            # Вывод данных
            print(data)
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
