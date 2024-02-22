from django.urls import path#, include
from .views import Homepage, detalhe_sala, VerificarDisponibilidadeView

app_name = 'home'

urlpatterns = [
    # path('', views.index, name='home'),
    path('', Homepage.as_view(), name='homepage'),
    path('salas/<int:pk>/', detalhe_sala.as_view(),name='popup'),
    path('verificar-disponibilidade/<int:sala_id>/<str:data>/', VerificarDisponibilidadeView.as_view(), name='verificar-disponibilidade'),
]