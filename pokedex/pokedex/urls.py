from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path(
        "schema",
        get_schema_view(
            title="Pokedex API",
            description="Pokedex API documentation",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
