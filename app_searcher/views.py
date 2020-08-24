import json
from .play_store_scraper import play_store_scraper
from .app_store_scraper import app_store_scraper
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def index(request):
    template = 'app_searcher/index.html'

    context = {}
    return render(request, template, context)


def output(request):
    if request.is_ajax() and request.method == 'POST':
        package_name = request.POST.get('data')
        app_name = request.POST.get('data1')
        app_id = request.POST.get('data2')
        data = {}
        if package_name:
            print(package_name or 'NONE')
            result = play_store_scraper(BASE_URL=f'https://play.google.com/store/apps/details?id={package_name}&hl=en_IN')
            app_name = result[0]
            app_icon = result[1]
            app_downloaded_figure = result[2]
            app_description = result[3]
            app_rating = result[4]
            app_rating_figure = result[5]
            app_developer_name = result[6]
            data['app_name'] = f'{app_name}'
            data['app_icon'] = f'{app_icon}'
            data['app_downloaded_figure'] = f'{app_downloaded_figure}'
            data['app_description'] = f'{app_description}'
            data['app_rating'] = f'{app_rating}'
            data['app_rating_figure'] = f'{app_rating_figure}'
            data['app_developer_name'] = f'{app_developer_name}'
            data['play'] = 'play'
        elif app_name or app_id:
            string = app_name
            x = string.split()
            # print(x)
            List = ''
            for i in x:
                y = i.replace(',', '')
                z = y.replace(':', '')
                if z != '' and z != '-':
                    List += z + "-"
                    List.replace('--', '-')
                    # print(z)

            final_list = List[:-1].lower()
            print(final_list)

            result1 = app_store_scraper(BASE_URL=f'https://apps.apple.com/in/app/{final_list}/id{app_id}')
            app_name_play = result1[0]
            app_icon_play = result1[1]
            app_downloaded_figure_play = result1[2]
            app_description_play = result1[3]
            app_rating_play = result1[4]
            app_rating_figure_play = result1[5]
            app_developer_name_play = result1[6]
            data['app_name'] = f'{app_name_play}'
            data['app_icon'] = f'{app_icon_play}'
            data['app_downloaded_figure'] = f'{app_downloaded_figure_play}'
            data['app_description'] = f'{app_description_play}'
            data['app_rating'] = f'{app_rating_play}'
            data['app_rating_figure'] = f'{app_rating_figure_play}'
            data['app_developer_name'] = f'{app_developer_name_play}'
            data['store'] = 'store'

        return HttpResponse(json.dumps(data), content_type='application/json')