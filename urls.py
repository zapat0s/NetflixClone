from django.conf.urls import patterns, url

from videos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # Movie URLs
    url(r'^movies/$', views.movieList, name='movieList'),
    url(r'^movies/(?P<movie_id>\d+)/$', views.movieDetail, name='movieDetail'),

    # TV Show URLs
    url(r'^tvshows/$', views.tvShowList, name='tvShowList'),
    url(r'^tvshows/(?P<tvshow_id>\d+)/$', views.tvShowDetail, name='tvShowDetail'),
	url(r'^tvshows/(?P<tvshow_id>\d+)/(?P<episode_num>\d+)/$', views.episodeDetail, name='episodeDetail'),

	# Video URLs
	url(r'^videos/(?P<video_id>\d+)/$', views.sendVideo, name='getVideo'),
)
