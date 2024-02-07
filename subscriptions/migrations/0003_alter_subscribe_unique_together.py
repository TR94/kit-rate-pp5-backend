# Generated by Django 3.2.23 on 2024-02-06 14:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0006_category_owner'),
        ('subscriptions', '0002_auto_20240206_1148'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together={('owner', 'category')},
        ),
    ]