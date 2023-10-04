import requests
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from main.models import FrameworkModel
from main.templates.serializers import FrameworkModelSerializer
import json


# Create your views here.
def index(request):
    url = "https://api.npoint.io/ab1d335a31210c153bd1"

    # Отправка GET-запроса и получение ответа
    response = requests.get(url)

    # Проверка успешности запроса
    if response.status_code == 200:
        # Декодирование JSON-данных из ответа
        data_list = json.loads(response.text)

    return render(request, 'main/index.html', {'data_list': data_list})


def single_page(request):
    s = request.GET.get('s', '')  # Получаем параметр 's' из запроса
    text = f'This is page for {s}'  # Создаем текст на основе параметра
    return HttpResponse(text)


class FrameworkModelViewSet(viewsets.ModelViewSet):
    """ ViewSet-класс для вывода списка FrameworkModel  """

    serializer_class = FrameworkModelSerializer
    queryset = FrameworkModel.objects.all()
    filter_backends = [DjangoFilterBackend]


class FrameworkListByLanguageView(generics.ListAPIView):
    """Класс с выводам по языкам при запросе формата GET /frameworks/<language>"""
    serializer_class = FrameworkModelSerializer

    def get_queryset(self):
        language = self.kwargs['language']
        return FrameworkModel.objects.filter(language=language)
