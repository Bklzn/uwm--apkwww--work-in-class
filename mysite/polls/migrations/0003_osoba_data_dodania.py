# Generated by Django 4.1.2 on 2022-10-20 15:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
