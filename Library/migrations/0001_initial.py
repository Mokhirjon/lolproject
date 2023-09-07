# Generated by Django 4.2.5 on 2023-09-06 11:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('isnt_dead', models.BooleanField(default=datetime.datetime.now)),
                ('date_of_death', models.DateField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='author/')),
                ('country', models.CharField(default='', max_length=25)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
            ],
            options={
                'db_table': 'book_genre',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
                ('image', models.ImageField(upload_to='book/')),
                ('price', models.FloatField(default=0)),
                ('pages', models.PositiveSmallIntegerField(default=5)),
                ('desc', models.TextField(default='')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Library.genres')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Library.authors')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
        migrations.AddField(
            model_name='authors',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.genres'),
        ),
        migrations.AddField(
            model_name='authors',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]