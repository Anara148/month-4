from django.urls import path
from . import views
from . import view

urlpatterns = [
    path('quotes/', views.quotes_view),
    path('book_list/', view.book_list_view),
    path('book_list/<int:id>/', view.book_detail_view),
    path('book_list/<int:id>/delete', view.delete_book_view),
    path('book_list/<int:id>/update', view.update_book_view),
    path('create_book_list/', view.create_book_view),
    

]