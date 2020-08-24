import json

from django.http import HttpResponse
from django.shortcuts import render
from .forms import DataForm
import requests
from bs4 import BeautifulSoup
from .models import Keywords, Url


def index(request):
    template = 'key.html'
    form = DataForm()
    context = {'form': form}
    if request.method == 'POST' and request.is_ajax():
        form = DataForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['url'])

            obj = form.save()
            page = requests.get(form.cleaned_data['url'])
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                description = soup.find('meta', attrs={'property': 'og:description'}).get('content')
            except:
                description = ''

            try:
                keywords = soup.find('meta', attrs={'name': 'keywords'}).get('content')
                x = keywords.split(',')
            except:
                x = []
            # variable description contains the description in txt format
            # variable x contains the list of keywords extracted
            print(description)
            print(x)

            url = Url.objects.get(id=obj.id)
            data = {}

            key_list = []
            for i in x:
                keywords = Keywords.objects.create(keyword=i, url=url)
                key_list.append(i)
                keywords.save()
            data['description'] = description
            data['keywords'] = key_list

            return HttpResponse(json.dumps(data), content_type='application/json')

    return render(request, template, context)
