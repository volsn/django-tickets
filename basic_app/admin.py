from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.models import Group

from .models import Movie, Session


class TimeFilter(SimpleListFilter):
    title = 'время'
    parameter_name = 'время'

    def lookups(self, request, model_admin):
        return [('morning', 'Утро'), ('daytime', 'День'), ('evening', 'Вечер')]

    def queryset(self, request, queryset):
        if self.value() == 'morning':
            return queryset.filter(time__gte='06:01', time__lte='12:00')
        elif self.value() == 'daytime':
            return queryset.filter(time__gte='12:01', time__lte='20:00')
        elif self.value() == 'evening':
            return queryset.filter(time__gte='20:01', time__lte='06:00')
        else:
            return queryset

# Register your models here.


admin.site.unregister(Group)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'date', 'time',)
    list_filter = ('date', TimeFilter)
