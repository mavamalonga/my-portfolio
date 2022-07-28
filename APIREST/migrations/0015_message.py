# Generated by Django 4.0.5 on 2022-07-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIREST', '0014_project_framework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]
