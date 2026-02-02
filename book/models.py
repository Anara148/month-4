from django.db import models

class BookList(models.Model):
    title = models.CharField(max_length=100, verbose_name='напишите названия книги')
    description = models.TextField(verbose_name='напишите аннотацию книги')
    image = models.ImageField(upload_to='booklist/', verbose_name='загрузите фото')
    created_data_lang = models.PositiveBigIntegerField(verbose_name='укажите год создания книги', blank=True)
    chapter_count = models.PositiveIntegerField(verbose_name='сколько глва в книге')
    author = models.CharField(max_length=100, verbose_name='автор книги')
    pages = models.PositiveIntegerField(verbose_name='количество страниц')
    language = models.CharField(max_length=50, verbose_name='язык книги')
    publisher = models.CharField(max_length=100, verbose_name='издательство')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

