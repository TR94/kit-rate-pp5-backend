# Generated by Django 3.2.23 on 2024-02-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(default='Accessories', max_length=32),
        ),
    ]