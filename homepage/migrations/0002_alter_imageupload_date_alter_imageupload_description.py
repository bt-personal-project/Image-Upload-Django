# Generated by Django 4.1.6 on 2023-02-17 08:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]