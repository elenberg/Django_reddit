# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20151205_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='internal_link',
            new_name='internal',
        ),
    ]
