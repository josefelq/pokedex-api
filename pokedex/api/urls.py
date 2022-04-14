from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from rest_framework import routers
from .views import PokemonViewSet, RegisterViewSet, UserPokemonViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"user_pokemons", UserPokemonViewSet, basename="user_pokemons")
router.register(r"pokemons", PokemonViewSet, basename="pokemons")
router.register(r"register", RegisterViewSet, basename="register")

urlpatterns = [
    path("token", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
