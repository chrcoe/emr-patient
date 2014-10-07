# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allergy_name', models.CharField(max_length=255)),
                ('severity', models.CharField(max_length=255)),
                ('allergy_description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LabResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lab_title', models.CharField(max_length=255)),
                ('lab_date', models.CharField(max_length=255)),
                ('lab_description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition_name', models.CharField(max_length=255)),
                ('is_family', models.BooleanField(default=False)),
                ('condition_description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medication_name', models.CharField(max_length=255)),
                ('dosage', models.IntegerField(default=0)),
                ('medication_description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=30, verbose_name=b'first_name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name=b'last_name', blank=True)),
                ('twitter_handle', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vitals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('height_inches', models.IntegerField(default=0)),
                ('weight_pounds', models.IntegerField(default=0)),
                ('blood_pressure', models.IntegerField(default=0)),
                ('pulse', models.IntegerField(default=0)),
                ('id_patient', models.ForeignKey(to='patient.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='medication',
            name='id_patient',
            field=models.ForeignKey(to='patient.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='medicalconditions',
            name='id_patient',
            field=models.ForeignKey(to='patient.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='labresults',
            name='id_patient',
            field=models.ForeignKey(to='patient.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allergies',
            name='id_patient',
            field=models.ForeignKey(to='patient.Patient'),
            preserve_default=True,
        ),
    ]
