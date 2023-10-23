from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)
router.register('likes', LikesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('rating/<id:pk/', RatingViewSet.as_view({'get': 'list'}))
]