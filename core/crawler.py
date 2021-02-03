from bs4 import BeautifulSoup
import re
import requests
import sys


def create_url(origem, destino, dia):
    return "https://www.clickbus.com.br/onibus/" + origem + "/" + destino + "?departureDate=" + dia

def read_request(url):
    print(url)
    r = requests.get(url)
    return r.text


def buscrawl(request, origem, destino, dia):
    re_tag = re.compile(r'^search-item search-item-direct')
    url = create_url(origem, destino, dia)
    response = read_request(url)
    soup = BeautifulSoup(response)
    divprices = soup.findAll("div", class_="price")
    mydivs = soup.findAll("div", class_= re_tag)
    divvagas = soup.findAll("div", class_= "service-class")
    prices=[]
    mytimes=[]
    classe=[]
    vagas=[]
    viagens={}
    for div in mydivs:
        departure_time = div.findAll("time", class_="departure-time")
        mytimes.append(departure_time[0].text)
    for price in divprices:
        price_aux = (price.find("span", class_="price-value"))
        prices.append(price_aux.text)
    for vaga in divvagas:
        classe.append(vaga.find("span").text)
        vagas.append(vaga.find("small").text[17:19])
    for i in range(len(mytimes)):
        viagens[i] = {'horario': mytimes[i], 'preco': prices[i], 'classe': classe[i], 'vagas': vagas[i]}    
    return(viagens)


print(buscrawl("sao-jose-dos-campos-sp", "rio-de-janeiro-rj-todos", sys.argv[1]))