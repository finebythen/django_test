# Generated by Django 3.1 on 2020-08-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test_general', '0004_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='cluster',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='project',
            field=models.CharField(max_length=255),
        ),
    ]
