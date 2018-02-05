# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Subscription.friend'
        db.delete_column(u'subscriptions_subscription', 'friend_id')


    def backwards(self, orm):
        # Adding field 'Subscription.friend'
        db.add_column(u'subscriptions_subscription', 'friend',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='referral', null=True, to=orm['subscriptions.Subscription'], blank=True),
                      keep_default=False)


    models = {
        u'subscriptions.subscription': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Subscription'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '121'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['subscriptions']