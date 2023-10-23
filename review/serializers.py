from rest_framework.serializers import ModelSerializer, ReadOnlyField, ValidationError
from .models import *
from rest_framework import serializers


class CommentsSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    hotels = serializers.ReadOnlyField(source='hotels.title')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comments = self.Meta.model.objects.create(author=user, **validated_data)
        return comments

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['commented'] = CommentsSerializer(instance.comments.all(), many=True).data


class RatingSerializer(ModelSerializer):
    customer = ReadOnlyField(source='author.name')

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):  # удалить у Аизы так как это кажется не нужно т.к мы импортировали валидаторы в модельке
        if rating > 5:
            raise ValidationError(
                'Рейтинг не должен быть больше 5'
            )
        return rating

    def create(self, validated_data):
        user = self.context.get('request').user
        rating = self.Meta.model.objects.create(author=user, **validated_data)
        return rating


class LikesSerializer(ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        like = self.Meta.model.objects.create(author=user, **validated_data)
        return like

    def to_representation(self, instance):  # проверить что тут получится у Аизы
        representation = super().to_representation(instance)
        representation['likes'] = LikesSerializer(instance.likes.all(), many=True).data

    def validate(self, attrs):
        hotel = attrs.get('hotels')
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(hotel=hotel, author=user).exists():
            raise ValidationError('Вы уже оставляли лайк')
        return attrs
