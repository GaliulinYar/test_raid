import json
from django.core.management import BaseCommand
from main.models import FrameworkModel


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Функция для заполнения БД"""
        # открываем файл, где лежит список словарей с нужными значениями
        with open('fw_list.json', 'r') as json_file:
            data = json.load(json_file)
        for a in data:

            frame_work = FrameworkModel.objects.create(
                name=a["name"],
                language=a["language"],

            )

            frame_work.save()
