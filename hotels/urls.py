from django.urls import path
from .views import HotelView, HotelDetailView, CategoryView, RoomView, RoomDetailView

urlpatterns = [
    path('hotel/<int:pk>/', HotelDetailView.as_view()),
    path('post/', HotelView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('rooms/<int:pk>/', RoomDetailView.as_view()),
    path('rooms/', RoomView.as_view()),

]