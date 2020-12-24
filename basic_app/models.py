from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=120, null=False,
                             unique=True, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              verbose_name='фильм')
    date = models.DateField(verbose_name='дата')
    time = models.TimeField(verbose_name='время')

    def __str__(self):
        return self.movie.title + ' ' + str(self.date) + ' ' + str(self.time)

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
