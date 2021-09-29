from django.urls import path
from .views import work

urlpatterns = [
    path('<int:work_album_id>/', work, name='work'),
]
