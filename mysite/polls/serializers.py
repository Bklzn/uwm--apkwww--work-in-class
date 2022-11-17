from rest_framework import serializers
from .models import Question, Choice, Osoba, Druzyna, MONTHS, COUNTRY_CODES
from django.contrib.auth.models import User
class OsobaSerializer(serializers.Serializer):
    imie = serializers.CharField(max_length = 30)
    nazwisko = serializers.CharField(max_length = 30)
    miesiac_urodzenia = serializers.ChoiceField(choices = MONTHS, default = MONTHS[0])
    data_dodania = serializers.DateField()
    druzyna = serializers.PrimaryKeyRelatedField(queryset = Druzyna.objects.all(), allow_null = True)
    wlasciciel = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), allow_null = True)
    class Meta:
        model = Osoba
        fields = ('imie', 'nazwisko',  'miesiac_urodzenia', 'data_dodania' , 'druzyna', 'wlascicel')
        
    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance

class DruzynaSerializer(serializers.Serializer):
    nazwa = serializers.CharField(max_length = 50)
    kraj = serializers.ChoiceField(
        choices = COUNTRY_CODES,
        default = COUNTRY_CODES[0]
    )
    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        return instance

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question,
        fields = ['question_text', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice,
        fields = ['question', 'choice_text', 'votes']
