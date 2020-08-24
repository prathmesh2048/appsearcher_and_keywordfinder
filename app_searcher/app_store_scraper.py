import requests
from bs4 import BeautifulSoup

# BASE_URL = 'https://apps.apple.com/in/app/void-troopers-sci-fi-tapper/id1367822033'


def app_store_scraper(BASE_URL):
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        picture = soup.find('picture', class_='we-artwork ember-view product-hero__artwork we-artwork--fullwidth we-artwork--ios-app-icon')
    except:
        picture = '!!!!!!!!!!'
    try:
        app_icon = picture.img.get('src')
    except:
        app_icon = '!!!!!!!!!!'
    try:
        app_name = soup.find('h1', class_='product-header__title app-header__title').text[:-3]
    except:
        app_name = '!!!!!!!!!!'
    try:
        app_downloaded_figure = "Sorry, no. of downloads are not available on appstore :( "
    except:
        app_downloaded_figure = '!!!!!!!!!!'
    try:
        app_description = soup.find('div', class_='section__description').text
    except:
        app_description = '!!!!!!!!!!'
    try:
        rating_info = soup.find('div', class_='we-customer-ratings__stats l-column small-4 medium-6 large-4')
    except:
        rating_info = '!!!!!!!!!!'
    try:
        app_rating = rating_info.find('div', class_='we-customer-ratings__averages').text
    except:
        app_rating = '!!!!!!!!!!'
    try:
        app_rating_figure = rating_info.find('div', class_='we-customer-ratings__count small-hide medium-show').text
    except:
        app_rating_figure = '!!!!!!!!!!'
    try:
        app_developer_name = soup.find('div', class_='information-list__item l-row').find('dd', class_='information-list__item__definition l-column medium-9 large-6').text
    except:
        app_developer_name = '!!!!!!!!!!'
    print(app_name, '\n')
    print(app_icon, '\n')
    print(app_downloaded_figure, '\n')
    print(app_description, '\n')
    print(app_rating, '\n')
    print(app_rating_figure, '\n')
    print(app_developer_name)
    return app_name, app_icon, app_downloaded_figure, app_description, app_rating, app_rating_figure, app_developer_name


# app_store_scraper(BASE_URL='https://apps.apple.com/in/app/shaq-fu-a-legend-reborn/id1255910488')

