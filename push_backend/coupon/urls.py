from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns=[
    url(r'^get/(?P<coupon_id>[0-9]+)/$', views.CouponGetter.as_view(), name="get_coupon"),
    url(r'^set/', views.set_coupon, name="set_coupon")
]