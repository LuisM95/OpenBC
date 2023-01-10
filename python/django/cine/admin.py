from django.contrib import admin

from .models import Director, Genre, Film
# Register your models here.

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Film)