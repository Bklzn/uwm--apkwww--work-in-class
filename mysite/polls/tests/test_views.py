from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..views import osoba_list
from .test_models import OsobaTest
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

class test_osoba_list(APITestCase):
    def setUp(self):
        OsobaTest.setUpTestData()
        self.factory = APIRequestFactory()
    
    def test_get_authorized(self):
        request = self.factory.get('osoby/')
        valid_user = User.objects.first()
        request.user = valid_user
        response = osoba_list(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unauthorized(self):
        request = self.factory.get('osoby/')
        response = osoba_list(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_authorized(self):
        data = {"imie":"John","nazwisko":"Smith","miesiac_urodzenia":5}
        request = self.factory.put('osoby/', data = data)
        valid_user = User.objects.first()
        request.user = valid_user
        response = osoba_list(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_unauthorized(self):
        data = {"imie":"John","nazwisko":"Smith","miesiac_urodzenia":5}
        request = self.factory.put('osoby/', data = data)
        response = osoba_list(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)