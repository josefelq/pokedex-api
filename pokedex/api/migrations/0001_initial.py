# Generated by Django 4.0.4 on 2022-04-14 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Pokemon",
            fields=[
                (
                    "name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("height_cm", models.IntegerField()),
                ("weight_kg", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BUG", "Bug"),
                            ("DRAGON", "Dragon"),
                            ("FAIRY", "Fairy"),
                            ("FIRE", "Fire"),
                            ("GHOST", "Ghost"),
                            ("GROUND", "Ground"),
                            ("NORMAL", "Normal"),
                            ("PSYCHIC", "Psychic"),
                            ("STEEL", "Steel"),
                            ("DARK", "Dark"),
                            ("ELECTRIC", "Electric"),
                            ("FIGHTING", "Fighting"),
                            ("FLYING", "Flying"),
                            ("GRASS", "Grass"),
                            ("ICE", "Ice"),
                            ("POISON", "Poison"),
                            ("ROCK", "Rock"),
                            ("WATER", "Water"),
                        ],
                        default="BUG",
                        max_length=20,
                    ),
                ),
                ("description", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "discovered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
