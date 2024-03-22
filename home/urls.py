from django.urls import path#, include
from .views import Homepage, detalhe_sala, VerificarDisponibilidadeView, AgendarEventoView, EventoDeleteView, AprovarEventoView, FaqListView

app_name = 'home'

urlpatterns = [
    # path('', views.index, name='home'),
    path('', Homepage.as_view(), name='homepage'),
    path('salas/<int:pk>/', detalhe_sala.as_view(),name='popup'),
    path('verificar-disponibilidade/<int:sala_id>/<str:data>/', VerificarDisponibilidadeView.as_view(), name='verificar-disponibilidade'),
    path('agendar-evento/', AgendarEventoView.as_view(), name='agendar_evento'),
    path('evento/<int:pk>/delete/', EventoDeleteView.as_view(), name='delete_evento'),
    path('evento/<int:pk>/aprovar/', AprovarEventoView.as_view(), name='aprovar_evento'),
    path('faq/', FaqListView.as_view(), name='faq'),
]
