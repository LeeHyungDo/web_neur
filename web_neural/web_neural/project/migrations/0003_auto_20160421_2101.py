# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160408_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversegpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('congpufile', models.TextField(max_length=500)),
            ],
        ),
        migrations.RenameModel(
            old_name='Converse',
            new_name='Conversecpu',
        ),
        migrations.RenameField(
            model_name='conversecpu',
            old_name='confile',
            new_name='concpufile',
        ),
    ]
