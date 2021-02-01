from bs4 import BeautifulSoup
import re
import requests
import sys


clickbus_url = "https://www.clickbus.com.br/onibus/"
re_tag = re.compile(r'^search-item search-item-direct')

def create_url(origem, destino, dia):
    return clickbus_url + origem + "/" + destino + "?departureDate=" + dia

def read_request(url):
    print(url)
    r = requests.get(url)
    return r.text


def buscrawl(origem, destino, dia):
    
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
        viagens[i] = {'horário': mytimes[i], 'preço': prices[i], 'classe': classe[i], 'vagas': vagas[i]}
    # for i in range(len(viagens)-1):
        # if viagens[i].preço < viagens[i+1].preço
            # viagens[i+1].horário = viagens[i+1].horário + "-L"
        # else viagens[i].horário = viagens[i].horário + "-L"
    
    return(viagens)


print(buscrawl("sao-jose-dos-campos-sp", "rio-de-janeiro-rj-todos", sys.argv[1]))