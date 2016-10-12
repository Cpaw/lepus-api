# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lepus', '0003_auto_20160921_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='notice',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
