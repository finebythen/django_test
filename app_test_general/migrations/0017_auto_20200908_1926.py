# Generated by Django 3.1 on 2020-09-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_test_general', '0016_timefilteringexamples'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timefilteringexamples',
            options={'ordering': ['id']},
        ),
    ]