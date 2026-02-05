from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Tour)
admin.site.register(models.Registration)
admin.site.register(models.Review)
admin.site.register(models.Category)