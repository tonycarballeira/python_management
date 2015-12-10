# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_tables', '0002_auto_20151210_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sysrlnsyasym',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='syssyaaccount',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='syssymmodule',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='syssyaaccount',
            name='sys_sym_modules',
            field=models.ManyToManyField(through='main_tables.SysRlnSyaSym', to='main_tables.SysSymModule'),
        ),
    ]