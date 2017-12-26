import csv
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def teapot(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def drinks(request):
    drinks = []
    with open('drinks.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header

        for row in reader:
            drink = [
                row[0], # name
                row[1], # price
                row[2], # cold
                row[3], # emoney
                row[4], # floor
                row[5], # location
                row[6]  # category
            ]

            # filter by category
            param_category = request.GET.get('category', '')
            if param_category != '' and param_category != drink[6]:
                continue

            drinks.append(drink)

    data = { 'data': drinks }
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8')
    return response

def categories(request):
    categories = []
    with open('categories.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header
        for row in reader:
            categories.append(row[1])
    data = { 'data': categories }
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8')
    return response

def teapot2(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def main(request):

    return render(request, 'main.html', {})
