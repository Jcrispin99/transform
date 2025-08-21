from django.urls import path
from . import views

app_name = 'transformer'

urlpatterns = [
    path('', views.index, name='index'),
    path('transform/', views.transform_text, name='transform_text'),
]