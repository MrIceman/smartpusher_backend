from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Coupon
from .CouponSerializer import CouponSerializer


class CouponGetter(APIView):
    def get(self, request, coupon_id):
        coupon = Coupon.objects.get(pk=coupon_id)
        serializer = CouponSerializer(coupon)
        return Response(serializer.data)

    def post(self, request):
        if request.method == 'POST':
            jsonVal = request.data
            coupon = CouponSerializer(data=jsonVal)
            if coupon.is_valid():
                coupon.save()
                return HttpResponse(coupon.data, status.HTTP_201_CREATED)
            return HttpResponse(coupon.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def set_coupon(request):
    if request.method == 'POST':
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
