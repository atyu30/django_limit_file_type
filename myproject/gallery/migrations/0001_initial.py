# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import validatedfile.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestContainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('the_file', validatedfile.fields.ValidatedFileField(null=True, upload_to=b'testfile', blank=True)),
                ('container', models.ForeignKey(related_name='test_elements', to='gallery.TestContainer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('the_file', validatedfile.fields.ValidatedFileField(null=True, upload_to=b'files/%Y/%m/%d', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestModelNoValidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('the_file', validatedfile.fields.ValidatedFileField(null=True, upload_to=b'testfile', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
