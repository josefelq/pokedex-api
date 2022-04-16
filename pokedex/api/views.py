from rest_framework import viewsets, mixins, views
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
)
from .permissions import IsOwnerOrReadOnly
import requests
from .models import Pokemon
from .serializers import PokemonSerializer, RegisterSerializer, PokemonUpdateSerializer

from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class UserPokemonViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """A simple ViewSet for viewing and editing pokemons discovered by a user."""

    serializer_class = PokemonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the pokemon
        discovered by the user
        """
        user = self.request.user
        return Pokemon.objects.filter(discovered_by=user).order_by("-created_at")


class PokemonViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing pokemons.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Pokemon.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == "update" or self.action == "partial_update":
            return PokemonUpdateSerializer

        return PokemonSerializer


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    """A simple ViewSet for registering users into our application."""

    authentication_classes = []
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class GetRandomNumberView(views.APIView):
    authentication_classes = []

    def get(self, request):
        """Endpoint that fetches and returns a random number from randomnumberapi"""
        res = requests.get(
            "http://www.randomnumberapi.com/api/v1.0/random?min=1&max=1000&count=1"
        )
        json_data = res.json()
        if res.ok:
            json_data = {"data": json_data[0]}
        return Response(json_data, status=res.status_code)
