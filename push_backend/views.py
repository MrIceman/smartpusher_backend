from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from .serializer.PropertySerializer import PropertySerializer
from rest_framework import mixins
# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to the Gates of the Pusher-Backend.</h1>")


class PropertyGetter(APIView):

    def get(self, request, property_id):
        pId = property_id
        property = Property.objects.get(pk=pId)
        serializer = PropertySerializer(property)
        return Response(serializer.data)

def get_all(request):
    serializer = PropertySerializer(Property.objects.all())
    return Response(serializer.data)

@api_view(['POST'])
def set_property(request):
    if request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertySetter(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, param, param1):
        pass
