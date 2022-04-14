from django.contrib import admin
from django.contrib.auth import get_user_model

# Models
from .models import Pokemon

CustomUser = get_user_model()


admin.site.register(CustomUser)
admin.site.register(Pokemon)
