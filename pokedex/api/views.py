from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import Pokemon
from .serializers import PokemonSerializer, RegisterSerializer

from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class UserPokemonViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
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
    serializer_class = PokemonSerializer


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
