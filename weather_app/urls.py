from django.urls import path

# Views
from .views import home_page, get_city_name_api

urlpatterns = [
    path('', home_page, name='home_page'),
    path('get_city_name/', get_city_name_api, name='get_city_name'),
]
