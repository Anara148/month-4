from django.shortcuts import render
from django.http import HttpResponse


def quotes_view(request):
    if request.method == 'GET':
        return HttpResponse("Ведь сколько раз я говорил вам, что основная ваша ошибка заключается" \
        " в том, что вы недооцениваете значение человеческих глаз. Поймите, что язык может скрыть истину," \
        " а глаза - никогда! " \
        " 'М.А.Булгаков' ")

