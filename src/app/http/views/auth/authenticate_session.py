from inertia import inertia
from inertia import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.middleware.csrf import rotate_token
from django.shortcuts import redirect
from django.urls import reverse
import json
from support.debug import dd, var_dump
from django.contrib.auth.decorators import login_required


@inertia('Auth/Login')
def create(request):
    return {
        'status': True,
        'canResetPassword': True,
    }

@login_required
def store(request):
    """
    Handle the login POST.
    Expects fields like 'username' and 'password' (or 'email' if your auth backend uses it).
    """
    payload = json.loads(request.body)
    email = payload.get('email')
    password = payload.get('password')

    User = get_user_model()
    u = User.objects.filter(email__iexact=email).first()
    username = u.get_username()
    user = authenticate(request, username=username, password=password)

    var_dump(payload, username, password, user)
    if user is None:
        messages.error(request, 'Invalid credentials.')
        # you can also set a session status like Laravel
        request.session['status'] = 'Invalid credentials.'
        return redirect('auth:login')

    login(request, user)
    # Regenerate session (Laravel's regenerate())
    request.session.cycle_key()
    rotate_token(request)  # rotate CSRF token for safety

    # nxt = request.POST.get('next') or request.GET.get('next')
    return redirect(reverse('web:dashboard'))