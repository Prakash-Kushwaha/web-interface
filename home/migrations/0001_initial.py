# Generated by Django 4.2.5 on 2023-12-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('passowrd', models.CharField(max_length=255)),
            ],
        ),
    ]