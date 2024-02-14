from django.urls import path,include
from cal import views

app_name = 'cal'


urlpatterns = [
    path('cal/', views.index, name='index')
]
