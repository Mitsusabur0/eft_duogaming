# Generated by Django 4.2 on 2023-05-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_categoria_options_alter_juego_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='categoria_imagenes'),
        ),
    ]
