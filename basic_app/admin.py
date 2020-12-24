from django.contrib import admin
from .models import Movie, Session

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'date', 'time',)
    list_filter = ('date',)
