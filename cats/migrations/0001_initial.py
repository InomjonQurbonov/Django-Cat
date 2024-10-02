# Generated by Django 5.1.1 on 2024-10-01 13:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_age', models.IntegerField(blank=True, null=True)),
                ('cat_gender', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_breed', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_color', models.CharField(blank=True, max_length=100, null=True)),
                ('cat_details', models.TextField(blank=True, null=True)),
                ('cat_image', models.ImageField(blank=True, null=True, upload_to='cats/Y%m%d')),
                ('cat_created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cat_points', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'Cats',
                'verbose_name_plural': 'Cats',
                'db_table': 'cats',
            },
        ),
    ]
