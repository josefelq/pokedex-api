from django.contrib import admin
from .models import CustomUser, Pokemon

admin.site.register(CustomUser)
admin.site.register(Pokemon)
