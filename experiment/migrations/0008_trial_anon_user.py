# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_auto_20180711_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='anon_user',
            field=models.CharField(default='a0', max_length=50),
            preserve_default=False,
        ),
    ]
