from django.http import HttpResponse
from django.test import TestCase
from django.contrib.auth.decorators import login_required

# Create your tests here.

# @login_required(login_url='/auth/login/')
# def plataform(request):
#     return HttpResponse('plataforma')