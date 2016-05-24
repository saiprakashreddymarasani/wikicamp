# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'appwiki_tag', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
        ))
        db.send_create_signal(u'appwiki', ['Tag'])

        # Adding M2M table for field tags on 'Page'
        m2m_table_name = db.shorten_name(u'appwiki_page_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'appwiki.page'], null=False)),
            ('tag', models.ForeignKey(orm[u'appwiki.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'appwiki_tag')

        # Removing M2M table for field tags on 'Page'
        db.delete_table(db.shorten_name(u'appwiki_page_tags'))


    models = {
        u'appwiki.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['appwiki.Tag']", 'symmetrical': 'False'})
        },
        u'appwiki.tag': {
            'Meta': {'object_name': 'Tag'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'})
        }
    }

    complete_apps = ['appwiki']