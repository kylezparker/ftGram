# Generated by Django 4.1.2 on 2022-10-12 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_alter_share_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='share',
            options={'ordering': ['-created_on']},
        ),
    ]
