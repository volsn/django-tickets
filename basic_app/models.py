from django.db import models
from django.contrib.auth.models import User

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


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='пользователь')
    session = models.ForeignKey(Session, on_delete=models.CASCADE,
                                verbose_name='сеанс')
    bought_at = models.DateTimeField(auto_now_add=True,
                                     verbose_name='Дата и время покупки')

    def __str__(self):
        return self.user.username + ' ' + str(self.session)

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
