# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Story'
        db.create_table(u'coalheartcache_story', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('charity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Charity'])),
            ('beneficiary_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('beneficiary_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('monthly_goal', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Story'])

        # Adding model 'Commitment'
        db.create_table(u'coalheartcache_commitment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Donor'])),
            ('beneficiary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Story'])),
            ('monthly_amount', self.gf('django.db.models.fields.IntegerField')()),
            ('next_payment', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Commitment'])

        # Adding unique constraint on 'Commitment', fields ['donor', 'beneficiary']
        db.create_unique(u'coalheartcache_commitment', ['donor_id', 'beneficiary_id'])

        # Adding model 'Donation'
        db.create_table(u'coalheartcache_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Donor'])),
            ('beneficiary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Story'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Donation'])

        # Adding model 'Comment'
        db.create_table(u'coalheartcache_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beneficiary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Story'])),
            ('commenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Donor'])),
            ('reply_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coalheartcache.Comment'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Comment'])

        # Adding model 'Charity'
        db.create_table(u'coalheartcache_charity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('stored_cash', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Charity'])

        # Adding model 'Category'
        db.create_table(u'coalheartcache_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Category'])

        # Adding model 'Donor'
        db.create_table(u'coalheartcache_donor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('stored_cash', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'coalheartcache', ['Donor'])


    def backwards(self, orm):
        # Removing unique constraint on 'Commitment', fields ['donor', 'beneficiary']
        db.delete_unique(u'coalheartcache_commitment', ['donor_id', 'beneficiary_id'])

        # Deleting model 'Story'
        db.delete_table(u'coalheartcache_story')

        # Deleting model 'Commitment'
        db.delete_table(u'coalheartcache_commitment')

        # Deleting model 'Donation'
        db.delete_table(u'coalheartcache_donation')

        # Deleting model 'Comment'
        db.delete_table(u'coalheartcache_comment')

        # Deleting model 'Charity'
        db.delete_table(u'coalheartcache_charity')

        # Deleting model 'Category'
        db.delete_table(u'coalheartcache_category')

        # Deleting model 'Donor'
        db.delete_table(u'coalheartcache_donor')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'coalheartcache.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'coalheartcache.charity': {
            'Meta': {'object_name': 'Charity'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'stored_cash': ('django.db.models.fields.IntegerField', [], {})
        },
        u'coalheartcache.comment': {
            'Meta': {'object_name': 'Comment'},
            'beneficiary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Story']"}),
            'commenter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'reply_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Comment']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'coalheartcache.commitment': {
            'Meta': {'unique_together': "(('donor', 'beneficiary'),)", 'object_name': 'Commitment'},
            'beneficiary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Story']"}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_amount': ('django.db.models.fields.IntegerField', [], {}),
            'next_payment': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'coalheartcache.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'beneficiary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Story']"}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Donor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'coalheartcache.donor': {
            'Meta': {'object_name': 'Donor'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'stored_cash': ('django.db.models.fields.IntegerField', [], {})
        },
        u'coalheartcache.story': {
            'Meta': {'object_name': 'Story'},
            'beneficiary_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'beneficiary_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'charity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['coalheartcache.Charity']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthly_goal': ('django.db.models.fields.IntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['coalheartcache']