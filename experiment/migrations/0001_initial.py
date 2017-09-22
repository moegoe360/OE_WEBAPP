# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import experiment.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_uploaded', models.DateTimeField(verbose_name='date uploaded', default=django.utils.timezone.now)),
                ('name', models.CharField(unique=True, verbose_name='Experiment Name', max_length=100)),
                ('file', models.FileField(blank=True, upload_to=experiment.models.user_directory_path, null=True)),
                ('js_Code', models.TextField(blank=True, null=True)),
                ('js_Code_Header', models.TextField(verbose_name='Any code for the header', blank=True, null=True)),
                ('is_Published', models.BooleanField(verbose_name='Published', default=False)),
                ('description', models.TextField(max_length=500, blank=True, null=True)),
                ('created_By', models.CharField(max_length=50)),
            ],
        ),
    ]
