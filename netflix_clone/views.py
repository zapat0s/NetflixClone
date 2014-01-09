import os

from django.views.generic.base import View, TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from sendfile import sendfile

from netflix_clone.models import Movie, TvShow, Episode, Video, Subtitle
from netflix_clone.serializers import MovieSerializer, TvShowSerializer
from netflix_clone.serializers import EpisodeSerializer, VideoSerializer

@login_required
def video_view(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return sendfile(request, video.path)


@login_required
def subtitle_view(request, sub_id):
    sub = get_object_or_404(Subtitle, pk=sub_id)
    return sendfile(request, sub.path)


class IndexView(TemplateView):
    template_name = "netflix_clone/index.html"


class PlayView(TemplateView):
    template_name = "netflix_clone/play.html"

    def get_context_data(self, **kwargs):
        context = super(PlayView, self).get_context_data(**kwargs)
        context['video'] = Video.objects.get(pk=kwargs['video_id'])
        return context


# API Views
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TvShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TvShow.objects.all()
    serializer_class = TvShowSerializer


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


