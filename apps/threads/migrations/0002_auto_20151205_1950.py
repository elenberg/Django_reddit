# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='internal',
            new_name='internal_link',
        ),
    ]
