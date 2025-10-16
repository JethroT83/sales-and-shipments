from inertia import inertia
from inertia import render

@inertia('Auth/Login')
def login(request):
    return {
        'status': True,
        'canResetPassword': True,
    }