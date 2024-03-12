from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from cal.views import AllEventsView, IndexView
# from home.views import Homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('cal/', IndexView.as_view(), name='index'),
    path('all_events/', AllEventsView.as_view(), name='all_events'),
    path('accounts/', include('allauth.urls')),
    # path('perfil/', Paginaperfil.as_view(), name='editarperfil'),
]
    # path('add_event/', views.add_event, name='add_event'),
    # path('update/', views.update, name='update'),
    # path('remove/', views.remove, name='remove'),
    # path('cal/', views.index, name='index'),
    # path('all_events/', views.all_events, name='all_events'),

    # ... the rest of your URLconf goes here ...

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
