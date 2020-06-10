import os

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
import csv
from django.http import HttpResponse
from .models import *


class CSVPageView(TemplateView):
    template_name = "csv_home.html"


def csv_simple_write(request):
    # Tạo đối tượng HttpResponse với tiêu đề CSV .
    response = HttpResponse(content_type='text/csv')
    # config file trả về
    response['Content-Disposition'] = 'attachment;filename="csv_simple_write.csv"'
    writer = csv.writer(response)
    writer.writerow(['first_name', 'last_name', 'phone_number', 'country'])
    writer.writerow(['Tung', 'Nguyen Son', '123456', 'Hanoi'])
    return response


def csv_dictionary_write(request):
    # Tạo đối tượng HttpResponse với tiêu đề CSV .
    response = HttpResponse(content_type='text/csv')
    # config file trả về
    response['Content-Disposition'] = 'attachment;filename="csv_dictionary_write.csv"'
    filenames = ['first_name', 'last_name', 'phone_number', 'country']
    writer = csv.DictWriter(response, fieldnames=filenames)
    writer.writeheader()
    writer.writerow({'first_name': 'tung', 'last_name': 'Nguyen Son', 'phone_number': '1234556', 'country': 'HCM'})
    return response


def csv_database_write(request):
    users = MyUser.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="csv_database_write.csv"'
    writer = csv.writer(response)
    writer.writerow(['code', 'name'])
    for user in users:
        writer.writerow([user.code, user.name])
    return response


def csv_simple_read(request):
    path = os.path.dirname(__file__)
    file = os.path.join(path, 'csv_readfile.csv')
    with open(file) as fi:
        csv_render = csv.reader(fi,delimiter=',')
        line_count = 0
        for row in csv_render:
            if line_count ==0:
                print(f'Header :{row}')
                line_count += 1
            else:
                print(f'Content :{row}')
                line_count += 1
        return redirect('/')

