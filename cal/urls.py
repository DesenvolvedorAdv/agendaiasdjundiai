from django.urls import path #,include
# from cal import views
from .views import AllEventsView, IndexView

app_name = 'cal'


urlpatterns = [
    path('cal/', IndexView.as_view(), name='index'),
    path('all_events/', AllEventsView.as_view(), name='all_events'),
]
# path('cal/', views.index, name='index'),

