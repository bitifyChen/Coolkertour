from django.urls import path
from .views import *

urlpatterns = [
    path('',member_list, name='member_list'),
    path('detail/<int:tour_id>/', member_detail, name='member_detail'),
]
