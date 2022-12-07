from django.test import TestCase
from ..models import Osoba, Druzyna
from django.contrib.auth.models import User

class DruzynaTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Druzyna.objects.create(nazwa = "RC Lens", kraj = "FR")
        Druzyna.objects.create(nazwa = "abc", kraj = "US")

    def test_str(self):
        druzyna = Druzyna.objects.get(id=1)
        self.assertEqual(druzyna.__str__(), "RC Lens (FR)")

    def test_nazwa_label(self):
        druzyna = Druzyna.objects.get(id=1)
        field_label = druzyna._meta.get_field('nazwa').verbose_name
        self.assertEqual(field_label, 'nazwa')

    def test_nazwa_max_length(self):
        druzyna = Druzyna.objects.get(id=1)
        max_length = druzyna._meta.get_field('nazwa').max_length
        self.assertEqual(max_length, 50)

    def test_kraj_max_length(self):
        druzyna = Druzyna.objects.get(id = 1)
        print(druzyna._meta.get_field('kraj'))
        max_length = druzyna._meta.get_field('kraj').max_length
        self.assertEqual(max_length, 2)

class OsobaTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DruzynaTest.setUpTestData()
        druzyna = Druzyna.objects.all()
        User.objects.create(username = "Jan")
        User.objects.create(username = "Joanna")
        users = User.objects.all()
        Osoba.objects.create(imie = "Jan", nazwisko = "Kowalski", miesiac_urodzenia = 1, druzyna = druzyna[0], wlasciciel = users[0])
        Osoba.objects.create(imie = "Joanna", nazwisko = "Kowalska", miesiac_urodzenia = 12, druzyna = druzyna[1], wlasciciel = users[1])
    
    def test_id(self):
        osoba1 = Osoba.objects.filter(imie = "Jan")[0]
        osoba2 = Osoba.objects.filter(imie = "Joanna")[0]
        self.assertEqual(osoba1.id, 1)
        self.assertEqual(osoba2.id, 2)

    def test_str(self):
        osoba = Osoba.objects.get(id=1)
        self.assertEqual(osoba.__str__(), "Jan Kowalski")

    def test_druzyna(self):
        osoba = Osoba.objects.get(id=1)
        druzyna = Druzyna.objects.all()[0]
        field_label = osoba.druzyna
        self.assertEqual(field_label, druzyna)

    def test_wlasciciel(self):
        users = User.objects.all()
        osoba1 = Osoba.objects.filter(imie = "Jan")[0]
        osoba2 = Osoba.objects.filter(imie = "Joanna")[0]
        self.assertEqual(osoba1.wlasciciel, users[0])
        self.assertEqual(osoba2.wlasciciel, users[1])

    def test_imie_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_imie_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 30)