# Generated by Django 4.1.3 on 2022-12-14 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0011_urun_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urun',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
