# Generated by Django 3.1 on 2020-08-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test_general', '0008_widgettweaksexamples'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgettweaksexamples',
            name='date_str',
            field=models.TextField(default='dd.mm.YYYY', max_length=10),
        ),
    ]