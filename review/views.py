from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import generics


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = []
        return super().get_permissions()


class LikesViewSet(ModelViewSet): #попробовать написать через apiview
    queryset = Likes.objects.all
    serializer_class = LikesSerializer
