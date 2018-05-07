from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Welcome to the home page!")

def help(request):
	help_dict = {'insert_me': "Help Page!"}
	return render(request, 'AppTwo/help.html', context=help_dict)
