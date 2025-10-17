from inertia import inertia
from inertia import render

@inertia('Auth/Login')
def create(request):
    return {
        'status': True,
        'canResetPassword': True,
    }