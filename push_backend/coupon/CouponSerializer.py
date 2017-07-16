from rest_framework import serializers

from push_backend.coupon.models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('id', 'what', 'when', 'offer', 'picture', 'created_on')

    def create(self, validated_data):
        couponObj = Coupon.objects.create(**validated_data)
        return couponObj
