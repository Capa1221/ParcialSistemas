# Generated by Django 5.0.6 on 2024-05-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
