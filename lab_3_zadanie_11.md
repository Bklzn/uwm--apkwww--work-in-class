``` python
>>> from polls.models import Osoba, Druzyna
>>>
>>>
>>> Osoba.objects.all()
<QuerySet [<Osoba: Grzegorz Brzęczyszczykiewicz>, <Osoba: Giovanni Giorgio>, <Osoba: Karol Jakiśtam>, <Osoba: Test TEST>, <Osoba: Johny Test>, <Osoba: asd asd>, <Osoba: Dodane zAdminPanela>]>
>>> Osoba.objects.all().get(id=3)
<Osoba: Johny Test>
>>>
>>>
>>> Osoba.objects.filter(imie__startswith='G')  
<QuerySet [<Osoba: Grzegorz Brzęczyszczykiewicz>, <Osoba: Giovanni Giorgio>]>
>>> [print(f"{i.get('imie')} {i.get('nazwisko')} {Druzyna.objects.filter(id = i.get('druzyna_id'))}") for i in Osoba.objects.values()]
Grzegorz Brzęczyszczykiewicz <QuerySet [<Druzyna: jakaś Francuska (FR)>]>
Giovanni Giorgio <QuerySet []>
Karol Jakiśtam <QuerySet [<Druzyna: LEGIA (PL)>]>
Test TEST <QuerySet [<Druzyna: jakaś Francuska (FR)>]>
Johny Test <QuerySet [<Druzyna: USA TEAM (US)>]>
asd asd <QuerySet [<Druzyna: USA TEAM (US)>]>
Dodane zAdminPanela <QuerySet []>
[None, None, None, None, None, None, None]
>>>
>>>
>>> Druzyna.objects.all().order_by('-nazwa') 
<QuerySet [<Druzyna: jakaś Francuska (FR)>, <Druzyna: USA TEAM (US)>, <Druzyna: LEGIA (PL)>]>
>>>
>>>
>>> Osoba(imie = 'Shell', nazwisko = 'Queryset', miesiac_urodzenia = 4, druzyna_id= 2).save()
>>> Osoba.objects.values().get(imie = 'Shell') 
{'id': 15, 'imie': 'Shell', 'nazwisko': 'Queryset', 'miesiac_urodzenia': 4, 'data_dodania': datetime.date(2022, 10, 23), 'druzyna_id': 2}
>>>
```