# Generated by Django 2.1.1 on 2019-08-15 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Genius_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe',
            new_name='recipe_ingredient',
        ),
        migrations.RenameField(
            model_name='step',
            old_name='recipe',
            new_name='recipe_step',
        ),
    ]