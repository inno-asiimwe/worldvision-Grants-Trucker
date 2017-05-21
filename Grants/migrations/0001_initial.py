# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('physical_address', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenditure_text', models.CharField(max_length=200)),
                ('exp_date', models.DateTimeField(verbose_name='Date of Expenditure')),
                ('amount_spent', models.IntegerField(verbose_name='Amount spent')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_text', models.CharField(max_length=200)),
                ('pay_date', models.DateTimeField(verbose_name='Payment Date')),
                ('amount_paid', models.IntegerField(verbose_name='Amount paid')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project_identifier', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('description', models.CharField(max_length=200)),
                ('grant_amount', models.IntegerField(verbose_name='Grant Amount')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grants.Donor')),
                ('expenditure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grants.Expenditure')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grants.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='SupportOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='support_office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grants.SupportOffice'),
        ),
    ]