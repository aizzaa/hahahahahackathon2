from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('')
    path('likes/', LikesDetailView.as_view()),
    # path('rating/<id:pk/', RatingViewSet.as_view({'get': 'list'}))
]