from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

filmscat = {
	'horror': 'Хоррор - это жанр для тех кто любит страшилки, '
			  'кому нужно пострашнее',
	'comedy': 'Комедия - это жанр для тех, кто любит посмеяться,'
			  'кто хочет посмотреть что-то легкое',
	'romantic': 'Романтика - это жанр для тех, кто ценит любовные линии,'
				'кому важны история и сюжет'
}


def getmainpage(request):
	data = {
		'filmscat':filmscat.keys()
	}
	return render(request, 'Filmscat/Filmscat.html', context = data)
def getFilmscat(request, name):



	if filmscat.get(name):
		data = {
			'filmscat': name,
			'description': filmscat[name]
		}
		return render(request,'Filmscat/Films.html',context=data)
	else:
		return HttpResponseRedirect('404')
def getFilms(request, name):
	data={
		"Films" : filmscat.keys(),
	}
	return render(request, 'Filmscat/Films.html', context = data)
def getNotFound(request):
	return HttpResponseNotFound('<h1>Not founds</h1>')