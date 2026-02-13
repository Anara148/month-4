from django.urls import path
from . import views


urlpatterns = [
    path('quotes/', views.quotes_view),
    path('book_list/', views.book_list_view),
    path('book_list/<int:id>/', views.book_detail_view),
    path('book_list/<int:id>/delete', views.delete_book_view),
    path('book_list/<int:id>/update', views.update_book_view),
    path('create_book_list/', views.create_book_view)
    

]