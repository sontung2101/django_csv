from django.urls import path
from .views import *

urlpatterns = [
    path('', CSVPageView.as_view(), name='csv_home_page'),
    path('export/csv_simple_write/', csv_simple_write, name='csv_simple_write'),
    path('export/csv_dictionary_write/', csv_dictionary_write,name='csv_dictionary_write'),
    path('export/csv_database_write/', csv_database_write,name='csv_database_write'),
    path('export/csv_simple_read/', csv_simple_read,name ='csv_readfile'),
]
