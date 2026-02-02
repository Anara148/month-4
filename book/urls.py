from django.urls import path
from . import views
from . import view

urlpatterns = [
    path('quotes/', views.quotes_view),
    path('book_list/', view.book_list_view),
    path('book_list/<int:id>/', view.book_detail_view,),
]