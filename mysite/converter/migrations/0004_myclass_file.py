# Generated by Django 5.0 on 2023-12-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_alter_myclass_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclass',
            name='file',
            field=models.FileField(default=1, upload_to='upldfile/'),
            preserve_default=False,
        ),
    ]
