import requests
from bs4 import BeautifulSoup
import config

def scrape_index(index_name):
    url = config.BASE_URL + index_name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {}
    data['name'] = index_name

    price_element = soup.find(id=config.PRICE_ID)
    if price_element:
        data['price'] = price_element.text.strip()

    change_element = soup.find(id=config.CHANGE_ID)
    if change_element:
        data['change'] = change_element.text.strip()

    percent_change_element = soup.find(id=config.PERCENT_CHANGE_ID)
    if percent_change_element:
        data['percent_change'] = percent_change_element.text.strip()

    return data

def scrape():
    indices = [config.COR3M, config.COR1M]
    data = []
    for index in indices:
        data.append(scrape_index(index))
    return data