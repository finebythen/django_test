# Generated by Django 3.1 on 2020-08-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user_created', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]