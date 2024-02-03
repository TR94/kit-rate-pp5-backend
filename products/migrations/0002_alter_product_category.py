# Generated by Django 3.2.23 on 2024-01-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('accessories', 'Accessories'), ('bikes', 'Bikes'), ('components', 'Components'), ('clothing', 'Clothing'), ('health and fitness', 'Health and Fitness'), ('tools and workshop', 'Tools and Workshop')], default='Accessories', max_length=32),
        ),
    ]