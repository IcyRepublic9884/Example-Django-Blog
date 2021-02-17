# Generated by Django 3.1.6 on 2021-02-17 04:36

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
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=80)),
                ('date_posted', models.DateField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
