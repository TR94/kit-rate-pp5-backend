# Generated by Django 3.2.23 on 2024-02-06 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscribed', to='categories.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
