# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stylefile', models.ImageField(upload_to='style/%Y%m%d')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subjectfile', models.ImageField(upload_to='subject/%Y%m%d')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='converse',
            name='confile',
            field=models.TextField(max_length=500),
        ),
    ]
