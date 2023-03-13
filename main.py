import math
import unidecode
import requests
from bs4 import BeautifulSoup

def parse():
    url = 'https://media-markts.ru/c/telefony/apple-iphone/'# ссылка на страницу
    page = requests.get(url)  # отправка запроса на адрес и получение ответа в переменную
    print(page.status_code)  # вывод ответа (кода подключения)
    soup = BeautifulSoup(page.text, "html.parser") # передача сраницы в bs4

    for span in soup.find_all("span", {'class': 'woocommerce-Price-currencySymbol'}):# удаление тега с символом рубля
        span.decompose()
    block = soup.findAll('span', class_='price') # взятие контейнеров с ценами

    prices = [] # список цен
    for data in block:  # проходим циклом по содержимому списка
        if data.find('span', class_='woocommerce-Price-amount amount'):  # нахождение тега с ценой
            prices.append(data.text)  # добавление цены в список цен

    for i in range(len(prices)):
        prices[i] = unidecode.unidecode(prices[i]) #преобразование в ASCII символы
        prices[i] = prices[i].replace(' ','') #замена пробелов
        prices[i] = prices[i].replace(',', '') #замена запятых
        prices[i] = int(prices[i]) #преобразование строки в float

    print(prices)
    print("Max - ", max(prices)) # вывод максимального значения
    print("Min - ", min(prices)) # вывод минимального значения
    print("Average - ", math.fsum(prices)/len(prices))  # вывод среднего значения

if __name__ == '__main__':
    parse()