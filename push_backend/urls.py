from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get/(?P<property_id>[0-9]+)/$',views.PropertyGetter.as_view(),name="getproperty"),
    url(r'^get/all/$', views.get_all,name="get_all_properties"),
    url(r'^set/$',views.set_property,name="setproperty")
]