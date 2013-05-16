# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banco'
        db.create_table('users_banco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('users', ['Banco'])

        # Adding model 'Voluntario'
        db.create_table('users_voluntario', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.UserProfile'], unique=True, primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('nascimento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('users', ['Voluntario'])

        # Adding model 'Cidade'
        db.create_table('users_cidade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Estado'])),
        ))
        db.send_create_signal('users', ['Cidade'])

        # Adding model 'Estado'
        db.create_table('users_estado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Pais'])),
        ))
        db.send_create_signal('users', ['Estado'])

        # Adding model 'Pais'
        db.create_table('users_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('users', ['Pais'])

        # Adding model 'Endereco'
        db.create_table('users_endereco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logradouro', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('complemento', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.Estado'], null=True, blank=True)),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.Cidade'], null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.Pais'], null=True, blank=True)),
        ))
        db.send_create_signal('users', ['Endereco'])

        # Adding model 'Beneficiario'
        db.create_table('users_beneficiario', (
            ('userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.UserProfile'], unique=True, primary_key=True)),
            ('banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.DadosBancarios'])),
            ('site', self.gf('django.db.models.fields.URLField')(default=None, max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('users', ['Beneficiario'])

        # Adding model 'DadosBancarios'
        db.create_table('users_dadosbancarios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agencia', self.gf('django.db.models.fields.IntegerField')()),
            ('conta', self.gf('django.db.models.fields.IntegerField')()),
            ('favorecido', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Banco'])),
        ))
        db.send_create_signal('users', ['DadosBancarios'])

        # Adding field 'UserProfile.endereco'
        db.add_column('users_userprofile', 'endereco',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.Endereco'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Banco'
        db.delete_table('users_banco')

        # Deleting model 'Voluntario'
        db.delete_table('users_voluntario')

        # Deleting model 'Cidade'
        db.delete_table('users_cidade')

        # Deleting model 'Estado'
        db.delete_table('users_estado')

        # Deleting model 'Pais'
        db.delete_table('users_pais')

        # Deleting model 'Endereco'
        db.delete_table('users_endereco')

        # Deleting model 'Beneficiario'
        db.delete_table('users_beneficiario')

        # Deleting model 'DadosBancarios'
        db.delete_table('users_dadosbancarios')

        # Deleting field 'UserProfile.endereco'
        db.delete_column('users_userprofile', 'endereco_id')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'users.area': {
            'Meta': {'object_name': 'Area'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'users.banco': {
            'Meta': {'object_name': 'Banco'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'users.beneficiario': {
            'Meta': {'object_name': 'Beneficiario', '_ormbases': ['users.UserProfile']},
            'banco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.DadosBancarios']"}),
            'site': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['users.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        'users.cidade': {
            'Meta': {'object_name': 'Cidade'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'users.dadosbancarios': {
            'Meta': {'object_name': 'DadosBancarios'},
            'agencia': ('django.db.models.fields.IntegerField', [], {}),
            'banco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Banco']"}),
            'conta': ('django.db.models.fields.IntegerField', [], {}),
            'favorecido': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'users.endereco': {
            'Meta': {'object_name': 'Endereco'},
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.Cidade']", 'null': 'True', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.Estado']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logradouro': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.Pais']", 'null': 'True', 'blank': 'True'})
        },
        'users.estado': {
            'Meta': {'object_name': 'Estado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Pais']"}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'users.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['users.Area']", 'symmetrical': 'False'}),
            'celphone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'endereco': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.Endereco']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'users.voluntario': {
            'Meta': {'object_name': 'Voluntario', '_ormbases': ['users.UserProfile']},
            'nascimento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['users.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['users']