# Generated by Django 5.0 on 2023-12-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0013_alter_myclass_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclass',
            name='request',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
