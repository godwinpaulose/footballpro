# Generated by Django 3.2.13 on 2022-06-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livescore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='football',
            name='img',
            field=models.ImageField(default=2, upload_to='photos'),
            preserve_default=False,
        ),
    ]