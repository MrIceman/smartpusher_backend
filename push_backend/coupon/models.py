from django.db import models
from push_backend.values import img_upload_path



class Coupon(models.Model):
    what = models.CharField(max_length=200)
    when = models.CharField(max_length=200)
    offer = models.CharField(max_length=200)
    picture = models.ImageField(img_upload_path(id), blank=True)
    created_on = models.TimeField(auto_now=True)

    def __str__(self):
        return self.what


class Location(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    created_on = models.TimeField(auto_now=True)
