from django.contrib import admin
from review.models import *

admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Rating)
admin.site.register(Favorite)