# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscription'
        db.create_table(u'subscriptions_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='referral', null=True, to=orm['subscriptions.Subscription'])),
            ('ref_id', self.gf('django.db.models.fields.CharField')(default='ABC', max_length=120)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(default='ABC', max_length=120)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'subscriptions', ['Subscription'])

        # Adding unique constraint on 'Subscription', fields ['email', 'ref_id']
        db.create_unique(u'subscriptions_subscription', ['email', 'ref_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Subscription', fields ['email', 'ref_id']
        db.delete_unique(u'subscriptions_subscription', ['email', 'ref_id'])

        # Deleting model 'Subscription'
        db.delete_table(u'subscriptions_subscription')


    models = {
        u'subscriptions.subscription': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Subscription'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['subscriptions.Subscription']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['subscriptions']