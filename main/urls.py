from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from main.apps import MainConfig
from main.views import index, FrameworkModelViewSet, FrameworkListByLanguageView
from django.conf import settings
from django.conf.urls.static import static

app_name = MainConfig.name
# роуетр для вьюсета ViewSet
router = DefaultRouter()
router.register(r'frameworks', FrameworkModelViewSet, basename='frameworks')

urlpatterns = [
    path('', index),
    path('frameworks/<str:language>/', FrameworkListByLanguageView.as_view(), name='framework-list-by-language'),
    path('single.html', views.single_page, name='single_page'),
] + router.urls

