from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from push_backend.models import Image,Property
from push_backend import values


@ensure_csrf_cookie
def upload_file(request, imgid):
    if request.method == 'POST':
        img = Image.objects.get(id=imgid)
        img.file = request.FILES['file']
        img.save()
        return HttpResponse(str(status.HTTP_200_OK))
    return HttpResponse(str(status.HTTP_400_BAD_REQUEST))
