# Generated by Django 4.1.3 on 2022-12-13 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_alter_urun_urunresmi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urun',
            old_name='yeniFiyat',
            new_name='indirimliFiyat',
        ),
    ]