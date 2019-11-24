# Generated by Django 2.2.7 on 2019-11-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('body', models.TextField(blank=True, default='')),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
            ],
        ),
    ]
