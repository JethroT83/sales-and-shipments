"""
URL configuration for orders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from app.api import OrderViewSet
# from .views import auth as auth_views
# from django.shortcuts import render

# router = DefaultRouter()
# router.register(r"orders", OrderViewSet, basename="orders")

# urlpatterns = [
#     path('login', auth_views.login_create, name='login'),  # GET
#     path('login', auth_views.login_store, name='login.store'),  # POST (same URL is fine in Django)
#     path('logout', auth_views.logout_destroy, name='logout'),  # POST
#
#
#     # path("/"),
#     # path('', lambda request: render(request, 'index.html'), name='index'),
#     path("admin/", admin.site.urls),
#     path("api/", include(router.urls)),
#     path("api/auth/", include("dj_rest_auth.urls")),  # login, logout, password reset, user
#     path("api/auth/registration/", include("dj_rest_auth.registration.urls")),  # signup (needs allauth)
# ]


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
