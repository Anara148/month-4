from django import forms
from book.models import BookList

class BookListForm(forms.ModelForm):
    class Meta:
        model = BookList
        fields = "__all__"