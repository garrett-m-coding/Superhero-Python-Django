# Generated by Django 3.2.7 on 2021-09-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alter_ego', models.CharField(max_length=75)),
                ('primary_ability', models.CharField(max_length=500)),
                ('secondary_ability', models.CharField(max_length=500)),
                ('catch_phrase', models.CharField(max_length=500)),
            ],
        ),
    ]
