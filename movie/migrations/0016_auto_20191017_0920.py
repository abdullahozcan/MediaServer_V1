# Generated by Django 2.2.6 on 2019-10-17 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_auto_20191016_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_actor_name',
            old_name='actor_id',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='movie_actor_name',
            old_name='cast_id',
            new_name='cast_num',
        ),
        migrations.RenameField(
            model_name='movie_actor_name',
            old_name='movie_id',
            new_name='movie',
        ),
    ]