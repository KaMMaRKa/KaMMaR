from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

filmscat = {
	'horror': 'horror',
	'comedy': 'comedy',
	'romantic': 'romantic',
}


def getFilmscat(request, name):

	data={
		'filmscat':name,
		'description':filmscat[name]
	}

	if filmscat.get(name):
		return render(request,'Filmscat/Filmscat.html',context=data)
	else:
		return HttpResponseRedirect('404')
def getFilms(request, name):
	data={
		"Films" : filmscat.keys(),
	}
	return render(request, 'Filmscat/Films.html', context = data)
def getNotFound(request):
	return HttpResponseNotFound('Not founds')