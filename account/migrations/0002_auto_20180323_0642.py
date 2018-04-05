# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
        ('account', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
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
            field=models.ManyToManyField(to='auth.Group', related_name='user_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_query_name='user'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_name='user_set', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_query_name='user'),
        ),
    ]
