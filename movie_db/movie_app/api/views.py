from movie_app.models import Movie
from movie_app.api.api_serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view()
def movie_detials(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
