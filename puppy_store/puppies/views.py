from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Puppy
from .serializers import PuppySerializer


class Puppies(APIView):
    def get(self, request):
        """
        Puppies
        """
        if request.query_params.get("color"):
            puppies = Puppy.objects.filter(color=request.query_params.get("color"))
        else:
            puppies = Puppy.objects.all()

        if len(puppies) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND, data=[])

        serializer = PuppySerializer(puppies, many=True)

        return Response(serializer.data)
