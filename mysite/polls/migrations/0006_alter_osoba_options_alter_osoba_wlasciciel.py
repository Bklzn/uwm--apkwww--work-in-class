# Generated by Django 4.1.2 on 2022-11-24 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_osoba_wlasciciel_alter_osoba_imie_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'permissions': [('can_view_other_persons', 'Pozwala widzieć osoby z tej samej drużyny')]},
        ),
        migrations.AlterField(
            model_name='osoba',
            name='wlasciciel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
