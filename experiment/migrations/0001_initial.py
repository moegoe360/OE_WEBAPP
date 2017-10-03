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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date uploaded')),
                ('name', models.CharField(unique=True, verbose_name='Experiment Name', max_length=100)),
                ('file', models.FileField(null=True, blank=True, upload_to=experiment.models.user_directory_path)),
                ('js_Code', models.TextField(null=True, blank=True)),
                ('js_Code_Header', models.TextField(null=True, blank=True, verbose_name='Any code for the header')),
                ('is_Published', models.BooleanField(default=False, verbose_name='Published')),
                ('description', models.TextField(null=True, blank=True, max_length=500)),
                ('created_By', models.CharField(max_length=50)),
            ],
        ),
    ]
