```python
from polls.models import Osoba, Druzyna
from polls.serializers import OsobaSerializer, DruzynaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

osoba = Osoba(imie = 'Adam', nazwisko = 'Serializer',     miesiac_urodzenia = 2)
osoba.save()

serializer = OsobaSerializer(osoba) 
serializer.data
# {'imie': 'Adam', 'nazwisko': 'Serializer', 'miesiac_urodzenia': 2, 'data_dodania': '2022-10-27', 'druzyna': None}

content = JSONRenderer().render(serializer.data) 
content
# b'{"imie":"Adam","nazwisko":"Serializer","miesiac_urodzenia":2,"data_dodania":"2022-10-27","druzyna":null}


import io


stream = io.BytesIO(content) 
data = JSONParser().parse(stream) 

deserializer = OsobaSerializer(data=data) 
deserializer.is_valid()                  
# False

deserializer.errors    
# {'druzyna': [ErrorDetail(string='This field may not be null.', code='null')]}

deserializer.validated_data
# {}
```

```python
deserializer.is_valid()
# True


deserializer.fields
# {'imie': CharField(max_length=30), 'nazwisko': CharField(max_length=30), 'miesiac_urodzenia': ChoiceField(choices=((1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')), default=(1, 'Styczeń')), 'data_dodania': DateField(), 'druzyna': PrimaryKeyRelatedField(allow_null=True, queryset=<QuerySet [<Druzyna: LEGIA (PL)>, <Druzyna: jakaś Francuska (FR)>, <Druzyna: USA TEAM (US)>]>)}

repr(deserializer) 
# "OsobaSerializer(data={'imie': 'Adam', 'nazwisko': 'Serializer', 'miesiac_urodzenia': 2, 'data_dodania': '2022-10-27', 'druzyna': None}):\n    imie = CharField(max_length=30)\n    nazwisko = CharField(max_length=30)\n    miesiac_urodzenia = ChoiceField(choices=((1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')), default=(1, 'Styczeń'))\n    data_dodania = DateField()\n    druzyna = PrimaryKeyRelatedField(allow_null=True, queryset=<QuerySet [<Druzyna: LEGIA (PL)>, <Druzyna: jakaś Francuska (FR)>, <Druzyna: USA TEAM (US)>]>)"

deserializer.validated_data
# OrderedDict([('imie', 'Adam'), ('nazwisko', 'Serializer'), ('miesiac_urodzenia', 2), ('data_dodania', datetime.date(2022, 10, 27)), ('druzyna', None)])

deserializer.save()        
# <Osoba: Adam Serializer>



deserializer.data   
# {'imie': 'Adam', 'nazwisko': 'Serializer', 'miesiac_urodzenia': 2, 'data_dodania': '2022-10-27', 'druzyna': None}
```