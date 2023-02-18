# Generated by Django 4.1.6 on 2023-02-18 11:16

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailTitle', models.CharField(max_length=50)),
                ('detailDescription', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
    ]