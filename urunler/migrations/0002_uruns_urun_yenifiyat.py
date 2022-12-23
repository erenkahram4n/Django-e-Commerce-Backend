# Generated by Django 4.1.3 on 2022-12-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uruns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=30)),
                ('urunAciklama', models.TextField(max_length=200)),
                ('eskiFiyat', models.IntegerField()),
                ('yeniFiyat', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='urun',
            name='yeniFiyat',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
