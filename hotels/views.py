from rest_framework import viewsets, generics
from .models import Hotels, Category
from rest_framework.response import Response
from .serializers import HotelSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
import logging
logger = logging.getLogger('main')

# class HotelViewSet(viewsets.ModelViewSet):
#     queryset = Hotels.objects.all()
#     serializer_class = HotelSerializer
#     permission_classes = [IsAdminUser]

# class HotelListView(generics.ListAPIView):
#     queryset = Hotels.objects.all()
#     serializer_class = HotelSerializer


class HotelView(generics.CreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]


class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        elif self.request.method == ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


# Category
# id
# title = (VIP, Default)
# slug
#
#
# hotels
# id,
# title
# description
# price
# client_count=2
# user
# is_book=true
# date_in
# date_out
# category_id(Vip)



