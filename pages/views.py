from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
	t = loader.get_template('index.html')
	c = {'foo': 'bar'}
	return HttpResponse(t.render(c,request))