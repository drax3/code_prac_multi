# Generated by Django 4.2.5 on 2023-09-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=150)),
                ('birth_year', models.IntegerField()),
                ('img', models.FileField(blank=True, upload_to='cat/images')),
            ],
        ),
    ]
