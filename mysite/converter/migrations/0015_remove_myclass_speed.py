# Generated by Django 5.0 on 2023-12-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0014_alter_myclass_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myclass',
            name='speed',
        ),
    ]
