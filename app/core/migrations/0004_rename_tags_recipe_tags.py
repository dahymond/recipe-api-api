# Generated by Django 3.2.22 on 2023-10-23 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20231020_0242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Tags',
            new_name='tags',
        ),
    ]
