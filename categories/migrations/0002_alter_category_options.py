# Generated by Django 3.2.23 on 2024-02-05 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-category']},
        ),
    ]
