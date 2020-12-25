from django.urls import path
from basic_app.views import index, user_login, user_logout, register


app_name = 'basic_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
]
