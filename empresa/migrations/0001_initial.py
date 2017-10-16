# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('persona', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('puntuacion', models.DecimalField(max_digits=2, decimal_places=2)),
            ],
        ),
    ]
