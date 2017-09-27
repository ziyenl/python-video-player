from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^player/$', views.player, name='player'),
    url(r'^player/(?P<id>[\w{}.-]{1,40})/$', views.player, name='player'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)