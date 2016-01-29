# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('summary', models.TextField(blank=True, null=True, verbose_name='摘要', max_length=100)),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('author', models.CharField(verbose_name='作者', max_length=100)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
