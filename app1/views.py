from django.shortcuts import render

from django.http import HttpResponse
def fun(request):
    return HttpResponse('im successfully in server')
