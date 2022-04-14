from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Pokemon(models.Model):

    # Pokemon types
    BUG = "BUG"
    DRAGON = "DRAGON"
    FAIRY = "FAIRY"
    FIRE = "FIRE"
    GHOST = "GHOST"
    GROUND = "GROUND"
    NORMAL = "NORMAL"
    PSYCHIC = "PSYCHIC"
    STEEL = "STEEL"
    DARK = "DARK"
    ELECTRIC = "ELECTRIC"
    FIGHTING = "FIGHTING"
    FLYING = "FLYING"
    GRASS = "GRASS"
    ICE = "ICE"
    POISON = "POISON"
    ROCK = "ROCK"
    WATER = "WATER"

    TYPE_CHOICES = [
        (BUG, "Bug"),
        (DRAGON, "Dragon"),
        (FAIRY, "Fairy"),
        (FIRE, "Fire"),
        (GHOST, "Ghost"),
        (GROUND, "Ground"),
        (NORMAL, "Normal"),
        (PSYCHIC, "Psychic"),
        (STEEL, "Steel"),
        (DARK, "Dark"),
        (ELECTRIC, "Electric"),
        (FIGHTING, "Fighting"),
        (FLYING, "Flying"),
        (GRASS, "Grass"),
        (ICE, "Ice"),
        (POISON, "Poison"),
        (ROCK, "Rock"),
        (WATER, "Water"),
    ]
    name = models.CharField(primary_key=True, max_length=20)
    height_cm = models.IntegerField()
    weight_kg = models.IntegerField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default=BUG)
    description = models.TextField()
    discovered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
