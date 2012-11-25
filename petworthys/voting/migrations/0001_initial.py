# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('voting_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('voting', ['Category'])

        # Adding model 'Participant'
        db.create_table('voting_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('voting', ['Participant'])

        # Adding model 'Entry'
        db.create_table('voting_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('votes', self.gf('django.db.models.fields.IntegerField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voting.Category'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['voting.Participant'])),
        ))
        db.send_create_signal('voting', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('voting_category')

        # Deleting model 'Participant'
        db.delete_table('voting_participant')

        # Deleting model 'Entry'
        db.delete_table('voting_entry')


    models = {
        'voting.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'voting.entry': {
            'Meta': {'object_name': 'Entry'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voting.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['voting.Participant']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        'voting.participant': {
            'Meta': {'object_name': 'Participant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['voting']