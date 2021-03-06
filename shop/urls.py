from django.urls import path
from .views import *

urlpatterns = [
    path('', shop_index, name='shop'),
    path('detail/', shop_detail, name='shop_detail'),
    path('detail/list', shop_list, name='shop_list'),
    path('detail/submit', shop_submit, name='shop_submit'),

    path('cms/', shop_cms, name='shop_cms'),
    path('cms/add', shop_cms_add, name='shop_cms_add'),

]
