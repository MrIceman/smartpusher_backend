from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^upload/(?P<imgid>[0-9]+)/$', csrf_exempt(views.upload_file))
    ]