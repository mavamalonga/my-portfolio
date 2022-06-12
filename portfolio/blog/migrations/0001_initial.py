# Generated by Django 4.0.5 on 2022-06-12 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=50000)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='blog.categorie')),
            ],
        ),
    ]
