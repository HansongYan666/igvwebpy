from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('get_bam/', views.get_bam, name='get_bam'),
    path("get_bai/", views.get_bai, name='get_bai'),
    path("test/", views.test, name='test'),
]