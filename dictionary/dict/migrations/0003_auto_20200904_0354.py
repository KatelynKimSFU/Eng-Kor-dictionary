# Generated by Django 3.1 on 2020-09-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0002_auto_20200904_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='acronym',
            field=models.CharField(blank=True, default=None, max_length=20),
        ),
    ]