from django.contrib import admin

# Register your models here.

from .models import Noticias
admin.site.register(Noticias)

from .models import ImagensNoticia
admin.site.register(ImagensNoticia)
