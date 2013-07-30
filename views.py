from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from videos.models import Movie
from videos.models import TVShow
from videos.models import Episode

def index(request):
    movies = Movie.objects.order_by('title')
    context = {'movie_list': movies,}
    return render(request, 'videos/movieList.html', context)

def movieList(request):
    movies = Movie.objects.order_by('title')
    context = {'movie_list': movies,}
    return render(request, 'videos/movieList.html', context)

def movieDetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'videos/movieDetail.html', {'movie': movie})

def tvShowList(request):
    shows = TVShow.objects.order_by('title')
    context = {'tvshow_list': shows,}
    return render(request, 'videos/tvShowList.html', context)

def tvShowDetail(result, tvshow_id):
    show = get_object_or_404(TVShow, pk=tvshow_id)
    episodes = Episode.objects.get(tvShow = show)
    return render(request, 'videos/tvShowDetail.html', {'tvshow': show})

def episodeDetail(result, episode_id):
    return HttpResponse("You are looking at the tv show episode %s." %episode_id)