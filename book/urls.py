from django.urls import path
from . import views


app_name='book'

urlpatterns = [
    path('quotes/', views.quotes_view),
    path('book_list/', views.book_list_view, name='knizhnyi_pir'),
    path('book_list/<int:id>/', views.book_detail_view, name='knizhnoe_menu'),
    path('book_list/<int:id>/delete', views.delete_book_view, name='kniga_terminator'),
    path('book_list/<int:id>/update', views.update_book_view, name='peresolit_knigu'),
    path('create_book_list/', views.create_book_view, name='sozdat_blog'),
    path('search/', views.search_view, name='iskat_recepty'),
    

]