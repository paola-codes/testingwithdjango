# Generated by Django 4.1 on 2022-08-08 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='last_anme',
            new_name='last_name',
        ),
    ]
