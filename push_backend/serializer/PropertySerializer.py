from rest_framework import serializers
from push_backend.models import Property, DetailsTitle, Detail, Image
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


class DetailValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ("first_value", "second_value")
        depth = 1

    def create(self, validated_data):
        return Detail.objects.create(detailsTitle=self.context['detailsTitle'], **validated_data)


class DetailTitleSerializer(serializers.ModelSerializer):
    detail_values = DetailValuesSerializer(many=True)

    class Meta:
        model = DetailsTitle
        fields = ('title', 'detail_values')

    def create(self, validated_data):
        detail_values = validated_data.pop('detail_values')
        detailTitleObj = DetailsTitle.objects.create(property=self.context['property'], **validated_data)
        detailsSerializer = DetailValuesSerializer(data=detail_values, many=True,
                                                   context={'detailsTitle': detailTitleObj})
        if detailsSerializer.is_valid():
            detailsSerializer.save()
        return detailTitleObj


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "path", "description","file")
        depth = 1


class PropertySerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    details = DetailTitleSerializer(many=True)

    class Meta:
        model = Property
        fields = ('id', "title", "short_descr", "description", "amount_of_photos", "created_on", "details", "images")

    def create(self, validated_data):
        image_data = validated_data.pop('images')
        detail_titles_data = validated_data.pop('details')
        propertyObj = Property.objects.create(**validated_data)
        for image in image_data:
            Image.objects.create(property=propertyObj, **image)
        # since its a level 2 nested object we're trying to deserialize
        # we need to pass the parent object as context
        detailsSerializer = DetailTitleSerializer(data=detail_titles_data, many=True, context={'property': propertyObj})
        if detailsSerializer.is_valid():
            detailsSerializer.save()

        return propertyObj
