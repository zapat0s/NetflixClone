from django.contrib import admin
from videos.models import Video
from videos.models import Subtitle
from videos.models import Movie
from videos.models import TVShow
from videos.models import Episode

admin.site.register(Video)
admin.site.register(Subtitle)
admin.site.register(Movie)
admin.site.register(TVShow)
admin.site.register(Episode)