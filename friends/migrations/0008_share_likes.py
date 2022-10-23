# Generated by Django 4.1.1 on 2022-10-23 17:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0007_remove_profile_profileimg_profile_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='likes',
            field=models.ManyToManyField(related_name='posts_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]