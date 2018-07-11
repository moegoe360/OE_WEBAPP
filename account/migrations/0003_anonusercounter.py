# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180612_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonUserCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('counter', models.IntegerField()),
            ],
        ),
    ]
