# Generated by Django 4.1.2 on 2022-11-12 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_druzyna_alter_osoba_options_osoba_druzyna'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='wlasciciel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='imie',
            field=models.CharField(max_length=30, validators=[polls.models.lettersOnly]),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='miesiac_urodzenia',
            field=models.IntegerField(choices=[(1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')], default=11, validators=[polls.models.noFutureMonth]),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='nazwisko',
            field=models.CharField(max_length=30, validators=[polls.models.lettersOnly]),
        ),
    ]
