# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'netflix_clone_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('duration', self.gf('django.db.models.fields.TimeField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(default='video/mp4', max_length=64)),
            ('hd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'netflix_clone', ['Video'])

        # Adding model 'Subtitle'
        db.create_table(u'netflix_clone_subtitle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subtitles', to=orm['netflix_clone.Video'])),
            ('language', self.gf('django.db.models.fields.CharField')(default='en-us', max_length=8)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'netflix_clone', ['Subtitle'])

        # Adding model 'Movie'
        db.create_table(u'netflix_clone_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('content_rating', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=512)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['netflix_clone.Video'])),
        ))
        db.send_create_signal(u'netflix_clone', ['Movie'])

        # Adding model 'TvShow'
        db.create_table(u'netflix_clone_tvshow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('content_rating', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=512)),
        ))
        db.send_create_signal(u'netflix_clone', ['TvShow'])

        # Adding model 'Episode'
        db.create_table(u'netflix_clone_episode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tv_show', self.gf('django.db.models.fields.related.ForeignKey')(related_name='episodes', to=orm['netflix_clone.TvShow'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('air_date', self.gf('django.db.models.fields.DateField')()),
            ('episode_num', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('season_num', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['netflix_clone.Video'])),
        ))
        db.send_create_signal(u'netflix_clone', ['Episode'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'netflix_clone_video')

        # Deleting model 'Subtitle'
        db.delete_table(u'netflix_clone_subtitle')

        # Deleting model 'Movie'
        db.delete_table(u'netflix_clone_movie')

        # Deleting model 'TvShow'
        db.delete_table(u'netflix_clone_tvshow')

        # Deleting model 'Episode'
        db.delete_table(u'netflix_clone_episode')


    models = {
        u'netflix_clone.episode': {
            'Meta': {'object_name': 'Episode'},
            'air_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'episode_num': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season_num': ('django.db.models.fields.SmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tv_show': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': u"orm['netflix_clone.TvShow']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['netflix_clone.Video']"})
        },
        u'netflix_clone.movie': {
            'Meta': {'object_name': 'Movie'},
            'content_rating': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '512'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['netflix_clone.Video']"})
        },
        u'netflix_clone.subtitle': {
            'Meta': {'object_name': 'Subtitle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en-us'", 'max_length': '8'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subtitles'", 'to': u"orm['netflix_clone.Video']"})
        },
        u'netflix_clone.tvshow': {
            'Meta': {'object_name': 'TvShow'},
            'content_rating': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '512'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'netflix_clone.video': {
            'Meta': {'object_name': 'Video'},
            'duration': ('django.db.models.fields.TimeField', [], {}),
            'hd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'default': "'video/mp4'", 'max_length': '64'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['netflix_clone']