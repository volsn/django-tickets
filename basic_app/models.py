from django.db import models

# Create your models here.


class Movie(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=120, null=False, unique=True)

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.movie.title + ' ' + str(self.date) + ' ' + str(self.time)
