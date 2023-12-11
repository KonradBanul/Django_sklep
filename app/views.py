from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Kategoria, Produkt, Klient, Zamowienie
from .serializers import KategoriaSerializer, ProduktSerializer, KlientSerializer, ZamowienieSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def klient_register(request):
    serializer = KlientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def kategoria_list(request):
    if request.method == 'GET':
        kategoria = Kategoria.objects.all()
        serializer = KategoriaSerializer(kategoria, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def kategoria_detail(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        kategoria = Kategoria.objects.get(pk=pk)
        serializer = KategoriaSerializer(kategoria)
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def kategoria_update(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = KategoriaSerializer(kategoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def kategoria_delete(request, pk):
    try:
        kategoria = Kategoria.objects.get(pk=pk)
    except Kategoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        kategoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def produkt_list(request):
    if request.method == 'GET':
        produkt = Produkt.objects.all()
        serializer = ProduktSerializer(produkt, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def produkt_detail(request, pk):
    try:
        produkt = Produkt.objects.get(pk=pk)
    except Produkt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        produkt = Produkt.objects.get(pk=pk)
        serializer = ProduktSerializer(produkt)
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def produkt_update(request, pk):
    try:
        produkt = Produkt.objects.get(pk=pk)
    except Produkt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProduktSerializer(produkt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def produkt_delete(request, pk):
    try:
        produkt = Produkt.objects.get(pk=pk)
    except Produkt.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        produkt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def klient_list(request):
    if request.method == 'GET':
        klient = Klient.objects.all()
        serializer = KlientSerializer(klient, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def klient_detail(request, pk):
    try:
        klient = Klient.objects.get(pk=pk)
    except Klient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        klient = Klient.objects.get(pk=pk)
        serializer = KlientSerializer(klient)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def zamowienie_list(request):
    if request.method == 'GET':
        zamowienie = Zamowienie.objects.all()
        serializer = ZamowienieSerializer(zamowienie, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def zamowienie_detail(request, pk):
    try:
        zamowienie = Zamowienie.objects.get(pk=pk)
    except Zamowienie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        zamowienie = Zamowienie.objects.get(pk=pk)
        serializer = ZamowienieSerializer(zamowienie)
        return Response(serializer.data)
