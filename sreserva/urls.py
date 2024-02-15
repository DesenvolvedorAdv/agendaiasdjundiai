from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from cal import views
# from home.views import Homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('cal/', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    # path('perfil/', Paginaperfil.as_view(), name='editarperfil'),
]


    # ... the rest of your URLconf goes here ...

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
