from django.urls import path
from .views import tour,tour_detail

urlpatterns = [
    path('', tour, name='tour'),
    path('detail/<int:tour_id>/', tour_detail, name='tour_detail'),
]
