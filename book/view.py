from django.shortcuts import render, get_object_or_404
from . import models





def book_detail_view(request, id):
    if request.method == 'GET':
        book_detail_id = get_object_or_404(models.BookList, id=id)
        return render(
            request,
            'book_detail.html',
            {
                "book_id": book_detail_id
            }
        )





def book_list_view(request):
    if request.method == 'GET':
        book_list = models.BookList.objects.all()
        return render(
            request,
            'book_list.html',
            {
                    "book_list": book_list
            }
        )
    


    