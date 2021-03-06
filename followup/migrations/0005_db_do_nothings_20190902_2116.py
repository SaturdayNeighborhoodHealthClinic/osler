# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-03 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0004_simplehistory_add_v2_migrations_2_20190813_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreferralfollowup',
            name='apt_location',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text=b'Where is the appointment?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ReferralLocation'),
        ),
        migrations.AlterField(
            model_name='historicalreferralfollowup',
            name='noapt_reason',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text=b"If the patient didn't make an appointment, why not?", null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.NoAptReason'),
        ),
        migrations.AlterField(
            model_name='historicalreferralfollowup',
            name='noshow_reason',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text=b"If the patient didn't go to appointment, why not?", null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='followup.NoShowReason'),
        ),
        migrations.AlterField(
            model_name='historicalreferralfollowup',
            name='referral_type',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text=b'What kind of provider was the patient referred to?', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ReferralType'),
        ),
    ]
