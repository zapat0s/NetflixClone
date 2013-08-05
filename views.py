import os

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from sendfile import sendfile

from videos.models import Movie
from videos.models import TVShow
from videos.models import Episode
from videos.models import Video

@login_required
def index(request):
    movies = Movie.objects.order_by('title')
    shows = TVShow.objects.order_by('title')
    context = {'movie_list': movies, 'tvshow_list': shows,}
    return render(request, 'videos/index.html', context)

@login_required
def movieList(request):
    movies = Movie.objects.order_by('title')
    context = {'movie_list': movies}
    return render(request, 'videos/movieList.html', context)

@login_required
def movieGenre(request, genre_slug):
    movies = Movie.objects.filter(genre__slug=genre_slug)
    context= {'movie_list':movies}
    return render(request, 'videos/movieList.html', context)

@login_required
def movieDetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'videos/movieDetail.html', {'movie': movie})

@login_required
def tvShowList(request):
    shows = TVShow.objects.order_by('title')
    context = {'tvshow_list': shows,}
    return render(request, 'videos/tvShowList.html', context)

@login_required
def tvShowGenre(request, genre_slug):
    shows = TVShow.objects.filter(genre__slug=genre_slug)
    context= {'tvshow_list':shows}
    return render(request, 'videos/tvShowList.html', context)

@login_required
def tvShowDetail(request, tvshow_id):
    show = get_object_or_404(TVShow, pk=tvshow_id)
    return render(request, 'videos/tvShowDetail.html', {'tvshow' : show})

@login_required
def episodeDetail(request, tvshow_id, episode_num):
    episode = get_object_or_404(Episode, tvShow=tvshow_id, epNum=episode_num)
    return render(request, 'videos/episodeDetail.html', {'episode' : episode})

@login_required
def sendVideo(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return sendfile(request, video.path)
