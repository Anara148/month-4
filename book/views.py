from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models, forms



def update_book_view(request, id):
     book_id = get_object_or_404(models.BookList, id=id)
     if request.method == "POST":
          form = forms.BookListForm(request.POST, instance=book_id)
          if form.is_valid():
               form.save()
               return redirect('/book_list/')
     else:
          form = forms.BookListForm(instance=book_id)
     return render(
          request,
          'update_book.html',
          {
               "form": form,
               "book_id": book_id
          }
     )



def delete_book_view(request, id):
     book_id = get_object_or_404(models.BookList, id=id)
     book_id.delete()
     return redirect('/book_list/')




def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/book_list/')
    else:
            form = forms.BookListForm()
    return render(
         request,
         'create_book.html',
         {
              "form": form
         }
    )



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
    





def quotes_view(request):
    if request.method == 'GET':
        return HttpResponse("Ведь сколько раз я говорил вам, что основная ваша ошибка заключается" \
        " в том, что вы недооцениваете значение человеческих глаз. Поймите, что язык может скрыть истину," \
        " а глаза - никогда! " \
        " ('М.А.Булгаков')")

