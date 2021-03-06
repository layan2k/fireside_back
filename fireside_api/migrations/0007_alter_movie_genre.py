# Generated by Django 4.0.2 on 2022-03-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireside_api', '0006_alter_movie_age_limit_alter_movie_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('horror', 'Horror'), ('sports', 'Sports'), ('romance', 'Romance'), ('documentary', 'Documentary'), ('fiction', 'Fiction'), ('action', 'Action'), ('drama', 'Drama'), ('animation', 'Animation'), ('fantasy', 'Fantasy'), ('spirituality', 'Spirituality'), ('comedy', 'Comedy')], max_length=50),
        ),
    ]
