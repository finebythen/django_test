# Generated by Django 3.1 on 2020-08-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test_general', '0011_auto_20200830_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvgroupmodel',
            name='amount_a',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='csvgroupmodel',
            name='amount_b',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='csvgroupmodel',
            name='amount_c',
            field=models.IntegerField(null=True),
        ),
    ]
