# Generated by Django 4.2 on 2023-05-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_categoria_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='categoria_imagenes'),
        ),
    ]
