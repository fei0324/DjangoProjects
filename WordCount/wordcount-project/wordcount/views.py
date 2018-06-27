from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def count(request):

	fulltext = request.GET['fulltext']
	newtext = re.sub('[^ a-zA-Z0-9]', '', fulltext)
	print(newtext)
	wordList = newtext.split()

	wordDict = {}

	for word in wordList:
		if word in wordDict:
			#increase
			wordDict[word] += 1
		else:
			#add word into dictionary
			wordDict[word] = 1

	sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 'sortedWords':sortedWords})