from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from rest_framework.routers import DefaultRouter

from netflix_clone import views

api_router = DefaultRouter(trailing_slash=False)
api_router.register(r'movies', views.MovieViewSet)
api_router.register(r'tvshows', views.TvShowViewSet)
#api_router.register(r'episodes', views.EpisodeViewSet)

urlpatterns = patterns('',
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    
    # API URLs
    url(r'^api/', include(api_router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # Play URL
    url(r'^play/(?P<video_id>\d+)/$', login_required(views.PlayView.as_view()), name='play'),

    # Video URLs
	url(r'^videos/(?P<video_id>\d+)/$', views.video_view, name='video'),

    # Subtitle URL
    url(r'^subtitles/(?P<sub_id>\d+)/$', views.subtitle_view, name='subtitle'),
)

