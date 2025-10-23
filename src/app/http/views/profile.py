from inertia import inertia

@inertia('Profile/Edit')
def edit(request):
    return {
        'mustVerifyEmail': False,
        'status': True,
    }

def update(request):
    return {}