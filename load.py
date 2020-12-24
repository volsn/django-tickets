from bs4 import BeautifulSoup

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tickets.settings')

import django
django.setup()

from basic_app.models import Movie, Session


def load(filename='Cinema.xml'):
    with open('Cinema.xml', 'r') as file:
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')

    for movie_soup in soup.find_all('movie'):
        if not Movie.objects.filter(pk=movie_soup['id']).exists():
            movie = Movie()
            movie.pk = movie_soup['id']
            movie.title = movie_soup['name']
            movie.save()
            
    for date_soup in soup.find_all('date'):
        date = date_soup['value']
        for movie_soup in date_soup.find_all('movie'):
            movie = movie_soup['name']
            for session_soup in movie_soup.find_all('session'):
                time = session_soup['time']

                session = Session()
                movie = Movie.objects.get(title=movie)
                session.movie = movie
                session.date = date
                session.time = time
                session.save()


if __name__ == '__main__':
    load()
