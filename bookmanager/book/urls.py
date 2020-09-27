from django.urls import path
from book.views import create_book,shop,register,json,method,response

from django.urls import converters
from django.urls.converters import register_converter

class MobileConverter:
    regex = '1[3-9]\d{9}'
    def to_python(self,value):
        return value

register_converter(MobileConverter,'phone')

urlpatterns = [
    path('create/',create_book),
    path('<int:city_id>/<phone:mobile>/',shop),
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('res/',response)
]

