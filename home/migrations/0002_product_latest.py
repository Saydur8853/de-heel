# Generated by Django 5.1.4 on 2025-01-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='latest',
            field=models.BooleanField(default=False, verbose_name='Latest Product'),
        ),
    ]
