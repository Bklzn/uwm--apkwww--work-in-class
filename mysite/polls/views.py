from django.http import HttpResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaSerializer, DruzynaSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class OsobaList(APIView):
    def get(self, request, format=None):
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OsobaDetails(APIView):
    def get_object(self, pk):
        try:
            osoba = Osoba.objects.get(pk=pk)
        except osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OsobaNameFit(APIView):
    def get_object(self, input):
        try:
            osoba = Osoba.objects.filter(imie__icontains = input)
            if(len(osoba) < 1):
                osoba = Osoba.objects.filter(nazwisko__icontains = input)
        except osoba.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, input, format=None):
        osoba = self.get_object(input)
        serializer = OsobaSerializer(osoba, many = True)
        return Response(serializer.data)

    def put(self, request, input, format=None):
        osoba = self.get_object(input)
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, input, format=None):
        osoba = self.get_object(input)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def druzyna_list(request):
    if request.method == 'GET':
        druzyna = Druzyna.objects.all()
        serializer = DruzynaSerializer(druzyna, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def druzyna_detail(request, pk):
    try:
        druzyna = Druzyna.objects.get(pk=pk)
    except druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        druzyna = Druzyna.objects.get(pk=pk)
        serializer = DruzynaSerializer(druzyna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DruzynaSerializer(druzyna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)