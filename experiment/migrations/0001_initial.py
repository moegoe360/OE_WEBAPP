# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import experiment.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(upload_to=experiment.models.experiment_directory_path, verbose_name='Attachment')),
            ],
        ),
        migrations.CreateModel(
            name='BooleanData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.BooleanField(verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharsData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.CharField(blank='false', max_length=255, verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.DateField(blank='false', verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DurationData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.DurationField(blank='false', verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(verbose_name='date uploaded', default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Experiment Name')),
                ('js_Code', models.TextField(blank=True, verbose_name='JS Experiment Code', null=True)),
                ('js_Code_Header', models.TextField(blank=True, verbose_name='JS Header Code', null=True)),
                ('is_Published', models.BooleanField(verbose_name='Published', default=False)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('created_By', models.CharField(max_length=50)),
                ('home_directory', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='FloatData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.FloatField(blank='false', verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IntData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.IntegerField(blank='false', verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StrData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dataType', models.CharField(blank='false', choices=[('FLO', 'Float'), ('INT', 'Integer'), ('CHAR', 'Chars'), ('STR', 'String'), ('DAT', 'Date'), ('BOOL', 'Boolean'), ('DUR', 'Duration')], max_length=5, verbose_name='Data Type')),
                ('value', models.TextField(blank='false', verbose_name='Data Value')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('trialNumber', models.PositiveIntegerField()),
                ('date_of_trial', models.DateTimeField(verbose_name='date uploaded', default=django.utils.timezone.now)),
                ('experiment', models.ForeignKey(to='experiment.Experiment')),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='strdata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='intdata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='floatdata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='durationdata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='datedata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='charsdata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='booleandata',
            name='trial',
            field=models.ForeignKey(to='experiment.Trial'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='experiment',
            field=models.ForeignKey(to='experiment.Experiment', verbose_name='Experiment'),
        ),
    ]
