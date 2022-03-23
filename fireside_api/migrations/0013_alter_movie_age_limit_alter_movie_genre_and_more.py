# Generated by Django 4.0.2 on 2022-03-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireside_api', '0012_alter_movie_age_limit_alter_movie_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(choices=[('Kids', 'Kids'), ('All', 'All')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('fantasy', 'Fantasy'), ('fiction', 'Fiction'), ('horror', 'Horror'), ('documentary', 'Documentary'), ('drama', 'Drama'), ('spirituality', 'Spirituality'), ('comedy', 'Comedy'), ('animation', 'Animation'), ('romance', 'Romance'), ('sports', 'Sports'), ('action', 'Action')], max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(choices=[('seasonal', 'Seasonal'), ('single', 'Single')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('Kids', 'Kids'), ('All', 'All')], max_length=10),
        ),
    ]
