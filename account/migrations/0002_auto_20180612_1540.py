# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experiments',
            field=models.ManyToManyField(to='experiment.Experiment'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group', related_name='user_set', related_query_name='user', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', blank=True, to='auth.Permission', related_name='user_set', related_query_name='user', verbose_name='user permissions'),
        ),
    ]
