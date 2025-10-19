from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from support.route import route
from app.http.views import dashboard
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path("", lambda request: redirect("auth:login"), name="root"),

    path(
        "dashboard",
        route(
            login_required(),
            get=dashboard.show,
        ),
        name="dashboard",
    ),
]