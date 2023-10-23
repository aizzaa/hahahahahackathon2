from rest_framework import serializers
from .models import *
from review.serializers import CommentsSerializer


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['commented'] = CommentsSerializer(instance.comments.all(), many=True).data
        representation['hotel']=HotelSerializer(instance.hotels.title, many=True).data


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


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'
