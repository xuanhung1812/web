# Generated by Django 3.2.6 on 2021-11-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Don_Nghi_Phep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hs', models.CharField(max_length=50)),
                ('id_hs', models.CharField(max_length=50)),
                ('name_ph', models.CharField(max_length=50)),
                ('reason', models.TextField()),
                ('tg_nghi', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
    ]
