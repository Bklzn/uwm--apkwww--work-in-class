from rest_framework import serializers
from rest_framework.decorators import api_view
from django.db import models
from datetime import date, datetime
from django.utils import timezone
from django.contrib import admin, auth


MONTHS = (
        (1, 'Styczeń'),
        (2, 'Luty'),
        (3, 'Marzec'),
        (4, 'Kwiecień'),
        (5, 'Maj'),
        (6, 'Czerwiec'),
        (7, 'Lipiec'),
        (8, 'Sierpień'),
        (9, 'Wrzesień'),
        (10, 'Październik'),
        (11, 'Listopad'),
        (12, 'Grudzień'),
)
COUNTRY_CODES = (
        ('PL', 'Polska'),
        ('DE', 'Niemcy'),
        ('US', 'Stany Zjednoczone'),
        ('FR', 'Francja'),
)
def lettersOnly(input):
    if not input.isalpha():
        raise serializers.ValidationError("Imię i nazwisko powinny zawierać tylko litery")
    return input

def noFutureMonth(input):
    if not input > datetime.now().month:
        raise serializers.ValidationError("Miesiąc nie może być późniejszy niż teraźniejszy")
    return input
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Osoba(models.Model):
    imie = models.CharField(max_length = 30, validators=[lettersOnly]) 
    nazwisko = models.CharField(max_length = 30, validators=[lettersOnly])
    miesiac_urodzenia = models.IntegerField(default = datetime.now().month, choices = MONTHS, validators=[noFutureMonth])
    data_dodania = models.DateField(auto_now_add = True)
    druzyna = models.ForeignKey(
        'Druzyna',
        on_delete = models.SET_NULL,
        null = True,
    )
    wlasciciel = models.ForeignKey('auth.User', null = True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nazwisko']
        permissions = [
            ('can_view_other_persons', 'Pozwala widzieć osoby z tej samej drużyny'),
        ]
    class OsobaAdmin(admin.ModelAdmin):
        list_display = ('imie', 'nazwisko', 'miesiac_urodzenia', 'data_dodania', 'druzyna_name')
        list_filter = ('druzyna', 'data_dodania')
        def druzyna_name(self, obj):
            return obj.druzyna
        druzyna_name.short_description = "Drużyna"
        
    def __str__(self):
        return str(self.imie + ' ' + self.nazwisko)
class Druzyna(models.Model):
    nazwa = models.TextField(max_length = 50)
    kraj = models.CharField(
        max_length = 2,
        choices = COUNTRY_CODES,
        default="PL"
    )
    class DruzynaAdmin(admin.ModelAdmin):
        list_display = ['nazwa', 'kraj']
    def __str__(self):
        return f'{self.nazwa} ({self.kraj})'
