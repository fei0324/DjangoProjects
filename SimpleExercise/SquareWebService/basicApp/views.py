from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def square(request):

	userInput = request.GET['userInput']

	response = float(userInput)**2

	return HttpResponse(response)
