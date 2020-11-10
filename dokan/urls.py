from django.urls import path
from .views import *
urlpatterns = [
    path('dokan',my_product),
    path('product-detail/<id>',product_detail,name='product-details'),
    
]