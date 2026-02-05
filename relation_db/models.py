from django.db import models


# many:many
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Person(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    category = models.ManyToManyField(Category, null=True)

    def __str__(self):
        return f'{self.full_name}------{', '.join(i.name for i in self.category.all() )}'
    
# 1:1
class Tour(models.Model):
    title = models.CharField(max_length=100, default='Тур по горам')
    location = models.TextField(max_length=100, default='Неизвестно')
    


    def __str__(self):
        return self.title


class Registration(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='registrations')
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.person} зарегистрирован на {self.tour}'



# 1:many
class Review(models.Model):
    MARKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='review')
    marks = models.CharField(max_length=100, choices=MARKS, default='5')
    text = models.CharField(max_length=100, default='Очень ответственный человек')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Человек: {self.person} - Оценка: {self.marks} - Коммент: {self.text}'


