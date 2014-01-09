from django.contrib import admin

from netflix_clone.models import Movie, TvShow, Episode, Video, Subtitle

admin.site.register(Video)
admin.site.register(Subtitle)
admin.site.register(Movie)
admin.site.register(TvShow)
admin.site.register(Episode)
