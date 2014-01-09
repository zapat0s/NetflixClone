from rest_framework import serializers

from netflix_clone.models import Movie, TvShow, Episode, Video, Subtitle

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        read_only_fields = ('id', 'duration', 'mime_type', 'hd')
        exclude = ['path']


class GenreListSerializer(serializers.WritableField):

    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_native(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj


class MovieSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
    genre_tags = GenreListSerializer(blank=True)
    
    class Meta:
        model = Movie
        read_only_fields = ('id', 'title', 'release_date',
            'content_rating', 'description', 'poster')


class EpisodeSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Episode
        read_only_fields = ('id', 'tv_show','title', 'air_date', 'episode_num',
            'season_num', 'description')


class TvShowSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)
    genre_tags = GenreListSerializer(blank=True)

    class Meta:
        model = TvShow
        read_only_fields = ('id', 'title', 'start_date', 'end_date', 
            'content_rating', 'description', 'poster')


