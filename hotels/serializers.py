from rest_framework import serializers
from .models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=30, source=Category.title)
    owner = serializers.ReadOnlyField(source=User.email)
#    slug = serializers.SlugField(required=False)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


