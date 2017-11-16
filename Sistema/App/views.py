from django.shortcuts import render
from pkg_resources._vendor.six import _urllib_request_moved_attributes
from django.http.response import HttpResponse

# Create your views here.

def Artigo(request, ano):
    return HttpResponse('Ola Mundo! Esse foi o ano digitado: ' + ano)