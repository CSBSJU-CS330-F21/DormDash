# Generated by Django 3.2.8 on 2021-11-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DormDashApp', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='restaurant_name',
            field=models.TextField(default='none'),
        ),
    ]