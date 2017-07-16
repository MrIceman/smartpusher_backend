from django.contrib import admin
from .models import Property,DetailsTitle,Detail,Image
# Register your models here.

@admin.register(Property,Image,DetailsTitle,Detail)
class PropertyAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Property,Image,DetailsTitle,Detail)
