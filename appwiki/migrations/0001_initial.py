# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'appwiki_page', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'appwiki', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'appwiki_page')


    models = {
        u'appwiki.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        }
    }

    complete_apps = ['appwiki']