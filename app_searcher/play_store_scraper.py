import requests
from bs4 import BeautifulSoup

# BASE_URL = 'https://play.google.com/store/apps/details?id=com.appxplore.voidtroopers&hl=en_IN'


def play_store_scraper(BASE_URL):
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        app_icon = soup.find('div', class_='xSyT2c').img.get('src')
    except:
        app_icon = 'Not avaliable'
    try:
        app_name = soup.find('h1', class_='AHFaub').text
    except:
        app_name = "Not avaliable"
    try:
        app_developer_name1 = soup.find_all('div', class_='hAyfc')[-2].text
    except:
        app_developer_name1 = "Not avaliable"
    try:
        app_developer_name2 = soup.find_all('div', class_='hAyfc')[-1].text
    except:
        app_developer_name2 = "Not avaliable"
    try:
        app_description = soup.find('div', class_='DWPxHb').text
    except:
        app_description = "Not avaliable"
    try:
        app_rating = soup.find('div', class_='BHMmbe').text  # may or may not be there on the page
    except:
        try:
            app_rating = soup.find_all('div', class_='hAyfc')[5].find('span', class_='htlgb').text
        except:
            app_rating = "Not avaliable"
    try:
        app_rating_figure = soup.find('span', class_='EymY4b').text  # may or may not be there on the page
    except:
        app_rating_figure = 'Not avaliable'
    try:
        app_downloaded_figure = soup.find_all('div', class_='hAyfc')[2].find('span', class_='htlgb').text
    except:
        app_downloaded_figure = 'None'
    try:
        app_developer_name = f'{app_developer_name1} and {app_developer_name2}'
    except:
        app_developer_name = 'None'
    # print('app_developer_name is ->', app_developer_name, '\n')
    # print('app_icon is ->', app_icon, '\n')
    # print('app_name is ->', app_name, '\n')
    # print('app_description is ->', app_description, '\n')
    # print('app_rating is ->', app_rating, '\n')
    # print('app_rating_figure is ->', app_rating_figure, '\n')
    # print('app_downloaded_figure is ->', app_downloaded_figure, '\n')
    return app_name, app_icon, app_downloaded_figure, app_description, app_rating, app_rating_figure, app_developer_name


# play_store_scraper(BASE_URL='https://play.google.com/store/apps/details?id=com.appxplore.voidtroopers&hl=en_IN')

'''At indices -:
0 - app_name
1 - app_icon
2 - app_downloaded_figure
3 - app_description
4 - app_rating
5 - app_rating_figure
6 - app_developer_name
'''