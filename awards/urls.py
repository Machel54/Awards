from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/',views.search_project,name='search_project'),
    url(r'^project/(\d+)',views.project,name='project'),
    url(r'^profile/',views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)