# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Booking'
        db.create_table('booking_booking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rejected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rejection_reason', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('booking', ['Booking'])

        # Adding M2M table for field kits on 'Booking'
        db.create_table('booking_booking_kits', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booking', models.ForeignKey(orm['booking.booking'], null=False)),
            ('kit', models.ForeignKey(orm['booking.kit'], null=False))
        ))
        db.create_unique('booking_booking_kits', ['booking_id', 'kit_id'])

        # Adding model 'KitType'
        db.create_table('booking_kittype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('booking', ['KitType'])

        # Adding model 'Kit'
        db.create_table('booking_kit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['booking.KitType'])),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('booking', ['Kit'])

        # Adding M2M table for field bookings on 'Kit'
        db.create_table('booking_kit_bookings', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('kit', models.ForeignKey(orm['booking.kit'], null=False)),
            ('booking', models.ForeignKey(orm['booking.booking'], null=False))
        ))
        db.create_unique('booking_kit_bookings', ['kit_id', 'booking_id'])


    def backwards(self, orm):
        
        # Deleting model 'Booking'
        db.delete_table('booking_booking')

        # Removing M2M table for field kits on 'Booking'
        db.delete_table('booking_booking_kits')

        # Deleting model 'KitType'
        db.delete_table('booking_kittype')

        # Deleting model 'Kit'
        db.delete_table('booking_kit')

        # Removing M2M table for field bookings on 'Kit'
        db.delete_table('booking_kit_bookings')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'booking.booking': {
            'Meta': {'object_name': 'Booking'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kits': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['booking.Kit']", 'symmetrical': 'False'}),
            'rejected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rejection_reason': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'booking.kit': {
            'Meta': {'object_name': 'Kit'},
            'bookings': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['booking.Booking']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['booking.KitType']"})
        },
        'booking.kittype': {
            'Meta': {'object_name': 'KitType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['booking']
