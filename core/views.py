# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, todo_svc, globalsettings_svc
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import re
import sys
import requests


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)

@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST['new_task'])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({'todos': todos})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d

#crawler
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
    return(JsonResponse(viagens))