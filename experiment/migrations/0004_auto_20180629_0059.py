# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_auto_20180629_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booleandata',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='charsdata',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='datedata',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='durationdata',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='floatdata',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='intdata',
            name='trial',
        ),
        migrations.RemoveField(
            model_name='strdata',
            name='trial',
        ),
        migrations.DeleteModel(
            name='BooleanData',
        ),
        migrations.DeleteModel(
            name='CharsData',
        ),
        migrations.DeleteModel(
            name='DateData',
        ),
        migrations.DeleteModel(
            name='DurationData',
        ),
        migrations.DeleteModel(
            name='FloatData',
        ),
        migrations.DeleteModel(
            name='IntData',
        ),
        migrations.DeleteModel(
            name='StrData',
        ),
    ]
