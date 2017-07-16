from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=200)
    short_descr = models.CharField(max_length=350)
    description = models.TextField(blank=True)
    amount_of_photos = models.IntegerField(default=0)
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class DetailsTitle(models.Model):
    property = models.ForeignKey(Property, on_delete= models.CASCADE, related_name="details")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Detail(models.Model):
    first_value = models.CharField(max_length=200)
    second_value = models.CharField(max_length=300)
    detailsTitle = models.ForeignKey(DetailsTitle, on_delete=models.CASCADE, related_name='detail_values')

    def __str__(self):
        return self.detailsTitle.title


class Image(models.Model):
    from push_backend.values import img_upload_path
    path = models.CharField(max_length=350)
    description = models.CharField(max_length=350, default="No Description")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to=img_upload_path(id), blank=True)

    def __str__(self):
        return self.property.title + " / " + str(id)
