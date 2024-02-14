from django.urls import path#, include
from .views import Homepage, detalhe_sala

app_name = 'home'

urlpatterns = [
    # path('', views.index, name='home'),
    path('', Homepage.as_view(), name='homepage'),
    path('salas/<int:pk>/', detalhe_sala.as_view(),name='popup'),
]