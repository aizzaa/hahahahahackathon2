from django.urls import path
from .views import HotelView, HotelDetailView, CategoryView

urlpatterns = [
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('post/', HotelView.as_view()),
    path('categories/', CategoryView.as_view())

]