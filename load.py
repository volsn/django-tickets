from bs4 import BeautifulSoup

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tickets.settings')

import django
django.setup()

from basic_app.models import Movie, Session

import argparse

parser = argparse.ArgumentParser(description='Data loading script.')
parser.add_argument('-f', '--file', type=str, default='Cinema.xml',
                    help='XML file to read from.')
parser.add_argument('-d', '--drop_data', type=bool, default=True,   # TODO : Change the default value
                    help='Drop the existing data from SQL before loading new.')


def load(filename='Cinema.xml', drop_data=False):

    if drop_data:
        print('[INFO] Dropping existing info from the database')
        Movie.objects.all().delete()
        Session.objects.all().delete()

    with open(filename, 'r') as file:
        print(f'[INFO] Loading data from { filename }')
        contents = file.read()
        soup = BeautifulSoup(contents, 'lxml')

        for movie_soup in soup.find_all('movie'):
            if not Movie.objects.filter(pk=movie_soup['id']).exists():
                movie = Movie()
                movie.pk = movie_soup['id']
                movie.title = movie_soup['name']
                movie.save()

        print('[INFO] Successfully loaded movies')

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

        print('[INFO] Successfully loaded sessions')


if __name__ == '__main__':
    args = vars(parser.parse_args())
    load(args['file'], drop_data=args['drop_data'])
