# Generated by Django 5.1.2 on 2024-10-14 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserProfile_app', '0003_alter_userprofile_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoroscopeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moon_sign', models.CharField(max_length=50)),
                ('star', models.CharField(max_length=50)),
                ('gotra', models.CharField(max_length=50)),
                ('manglik', models.BooleanField(default=False)),
                ('shani', models.BooleanField(default=False)),
                ('horoscope_match', models.BooleanField(default=False)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('place_of_country', models.CharField(max_length=100)),
                ('hours', models.PositiveIntegerField()),
                ('minutes', models.PositiveIntegerField()),
                ('seconds', models.PositiveIntegerField()),
                ('am_pm', models.CharField(max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserProfile_app.userprofile')),
            ],
        ),
    ]
