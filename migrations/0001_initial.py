# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'videos_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('duration', self.gf('django.db.models.fields.TimeField')()),
            ('mimeType', self.gf('django.db.models.fields.CharField')(default='video/mp4', max_length=64)),
            ('hd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'videos', ['Video'])

        # Adding model 'Subtitle'
        db.create_table(u'videos_subtitle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subtitles', to=orm['videos.Video'])),
            ('language', self.gf('django.db.models.fields.CharField')(default='en-us', max_length=8)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'videos', ['Subtitle'])

        # Adding model 'Movie'
        db.create_table(u'videos_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=512)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=512)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Video'])),
        ))
        db.send_create_signal(u'videos', ['Movie'])

        # Adding model 'TVShow'
        db.create_table(u'videos_tvshow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=512)),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=512)),
        ))
        db.send_create_signal(u'videos', ['TVShow'])

        # Adding model 'Episode'
        db.create_table(u'videos_episode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tvShow', self.gf('django.db.models.fields.related.ForeignKey')(related_name='episodes', to=orm['videos.TVShow'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('epNum', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('season', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['videos.Video'])),
        ))
        db.send_create_signal(u'videos', ['Episode'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'videos_video')

        # Deleting model 'Subtitle'
        db.delete_table(u'videos_subtitle')

        # Deleting model 'Movie'
        db.delete_table(u'videos_movie')

        # Deleting model 'TVShow'
        db.delete_table(u'videos_tvshow')

        # Deleting model 'Episode'
        db.delete_table(u'videos_episode')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'videos.episode': {
            'Meta': {'object_name': 'Episode'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'epNum': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.SmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tvShow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': u"orm['videos.TVShow']"}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']"})
        },
        u'videos.movie': {
            'Meta': {'object_name': 'Movie'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '512'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']"})
        },
        u'videos.subtitle': {
            'Meta': {'object_name': 'Subtitle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en-us'", 'max_length': '8'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subtitles'", 'to': u"orm['videos.Video']"})
        },
        u'videos.tvshow': {
            'Meta': {'object_name': 'TVShow'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '512'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'videos.video': {
            'Meta': {'object_name': 'Video'},
            'duration': ('django.db.models.fields.TimeField', [], {}),
            'hd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimeType': ('django.db.models.fields.CharField', [], {'default': "'video/mp4'", 'max_length': '64'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['videos']