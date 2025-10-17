from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API first (usually versioned)
    path("api/", include(("app.urls.api", "api"), namespace="api")),

    # Auth routes (login/reset/etc.)
    path("auth/", include(("app.urls.auth", "auth"), namespace="auth")),

    # Regular web pages (Inertia)
    path("", include(("app.urls.web", "web"), namespace="web")),
]
