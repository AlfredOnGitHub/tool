# Generated by Django 3.0.4 on 2020-03-21 17:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hamma', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileInfo',
            new_name='Usuario',
        ),
    ]
