from django.urls import path
from . import views

app_name = 'app_searcher'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('output/', views.output, name='output')
]
