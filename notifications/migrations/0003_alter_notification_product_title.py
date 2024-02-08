# Generated by Django 3.2.23 on 2024-02-08 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('notifications', '0002_alter_notification_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='product_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
