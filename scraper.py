import re
import requests
from bs4 import BeautifulSoup


def Scraper():

    url = 'http://www.covidmaroc.ma/Pages/AccueilAR.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    if (page.status_code != 200):
        return (None, None)
    results = BeautifulSoup(page.content, 'html.parser')
    locas = results.find_all('tr', class_='ms-rteTableOddRow-6')
    locas += results.find_all('tr', class_='ms-rteTableEvenRow-6')
    elems = results.find('tbody')
    death = results.find('span', class_='ms-rteThemeForeColor-9-4')
    localisations = []
    i = 0
    for loca in locas:
        localisation = loca.text.encode(
            'ascii', 'ignore').decode("utf-8").split('\n')
        localisation = list(filter(None, localisation))
        localisations.append(localisation)
        i += 1

    death = death.text.encode(
        'ascii', 'ignore').decode("utf-8").split('\n')
    list_data = list(filter(None, elems.text.encode(
        'ascii', 'ignore').decode("utf-8").split('\n')))
    print(list_data)
    len_recovered = len(list_data[1]) - len(death) - 1
    if (len_recovered < 1):
        exit(-1)
    list_data[1] = list_data[1][:len_recovered]
    list_data = list_data[:2] + death + list_data[2:]
    print(list_data)
    return (list_data, localisations)
