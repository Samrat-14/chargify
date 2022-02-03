from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GpsSerializer
from .models import Gps


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/gps/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of gps locations of users'
        },
        {
            'Endpoint': '/gps/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single gps location of a user'
        },
        {
            'Endpoint': '/gps/create',
            'method': 'POST',
            'body': {'lat': "", 'lon': ""},
            'description': 'Creates new gps location with data sent in post request'
        },
        {
            'Endpoint': '/gps/id/update',
            'method': 'PUT',
            'body': {'lat': "", 'lon': ""},
            'description': 'Creates an existing gps location with data sent in post request'
        },
        {
            'Endpoint': '/gps/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing gps location'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getGpss(request):
    gpss = Gps.objects.all()
    serializer = GpsSerializer(gpss, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGps(request, pk):
    gps = Gps.objects.get(id=pk)
    serializer = GpsSerializer(gps, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createGps(request):
    data = request.data
    gps = Gps.objects.create(
        latitude = data['latitude'],
        longitude = data['longitude']
    )
    serializer = GpsSerializer(gps, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateGps(request, pk):
    gps = Gps.objects.get(id=pk)
    serializer = GpsSerializer(gps, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteGps(request, pk):
    gps = Gps.objects.get(id=pk)
    gps.delete()
    return Response('Gps location was deleted!')