# Generated by Django 5.0 on 2023-12-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0012_alter_myclass_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclass',
            name='request',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
