# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Subscription.ref_id'
        db.alter_column(u'subscriptions_subscription', 'ref_id', self.gf('django.db.models.fields.CharField')(max_length=121))

    def backwards(self, orm):

        # Changing field 'Subscription.ref_id'
        db.alter_column(u'subscriptions_subscription', 'ref_id', self.gf('django.db.models.fields.CharField')(max_length=120))

    models = {
        u'subscriptions.subscription': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Subscription'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'referral'", 'null': 'True', 'to': u"orm['subscriptions.Subscription']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '121'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['subscriptions']