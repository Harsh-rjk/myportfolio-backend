from django.http import HttpResponse;
from rest_framework.decorators import api_view 

from rest_framework.response import Response
from .models import entry
from .srealizer import SS


@api_view(['POST'])
def addentry(request):
    serializer = SS(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Student Added", "data": serializer.data})
    return Response(serializer.errors)

@api_view(['GET'])
def getentry(request):
     entryy = entry.objects.all()
     serializer = SS(entryy, many=True)
     return Response(serializer.data)


def harsh(request):
    return HttpResponse("hey i am harsh")

