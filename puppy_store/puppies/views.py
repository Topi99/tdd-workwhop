from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class Puppies(APIView):
    def get(self, request):
        """
        Puppies
        """
        return Response({})
