from django.shortcuts import render
from movie_app.models import Movie
from django.http import JsonResponse

# Create your views here.


def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)


def movie_detials(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {'title': movie.name,
            'description': movie.decription,
            'active': movie.active, }
    return JsonResponse(data)
