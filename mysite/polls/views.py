from django.http import HttpResponse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaSerializer, DruzynaSerializer
from django.contrib.auth.models import User
from .permissions import MyDjangoModelPermission

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

for user in User.objects.all():
    Token.objects.get_or_create(user=user)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@api_view(['GET', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list(request):
    if request.method == 'GET':
        osoba = Osoba.objects.filter(wlasciciel_id=request.user.id)
        serializer = OsobaSerializer(osoba, many = True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk, wlasciciel_id=request.user.id)
    except osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_remove(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk, wlasciciel_id=request.user.id)
    except osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_namefit(request, input):
    try:
        osoba = Osoba.objects.filter(imie__icontains = input)
        if(len(osoba) < 1):
            osoba = Osoba.objects.filter(nazwisko__icontains = input)
    except osoba.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaSerializer(osoba, many = True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([MyDjangoModelPermission])
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

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def druzyna_teammates(request, id):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(druzyna_id=id, wlasciciel_id=request.user.id)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

def osoba_view(request, pk):
    if not request.user.has_perm('polls.view_osoba'):
        return HttpResponse(f"Nie masz uprawnień")
    try:
        osoba = Osoba.objects.get(pk=pk)
        return HttpResponse(f"Ten użytkownik nazywa się {osoba}")
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")


@api_view(['GET'])
@authentication_classes([SessionAuthentication])
def osoba_teamSquad(request, pk):
    if not request.user.has_perm('polls.can_view_other_persons'):
        return HttpResponse(f"Nie masz uprawnień")
    try:
        druzyna_id = Osoba.objects.get(pk = pk, wlasciciel_id=request.user.id).druzyna_id
        osoba = Osoba.objects.filter(druzyna_id = druzyna_id)
        serializer = OsobaSerializer(osoba, many = True)
        return Response(serializer.data)
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")
