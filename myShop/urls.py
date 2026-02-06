from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.all_categories),
    path('products/', views.all_products),
    path('category/<int:id>/', views.category_products)
]
    