# Generated by Django 4.0.2 on 2022-03-14 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fireside_api', '0003_remove_profile_payment_delete_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='type',
            new_name='movie_type',
        ),
    ]
