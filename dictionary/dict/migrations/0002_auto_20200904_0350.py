# Generated by Django 3.1 on 2020-09-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(default=None, max_length=30)),
                ('translated', models.CharField(default=None, max_length=30)),
                ('acronym', models.CharField(default=None, max_length=20)),
                ('note', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='wordEnglish',
        ),
        migrations.DeleteModel(
            name='wordKorean',
        ),
    ]
