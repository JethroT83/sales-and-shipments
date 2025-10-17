from django.urls import path
from django.contrib.auth.decorators import login_required
from ratelimit.decorators import ratelimit
from .decorators import guest_required, signed_required
from .urls_helpers import use
from .views import auth as V  # your functions from app/views/auth.py

guest = [guest_required()]            # unauthenticated only
authn = [login_required]              # must be authenticated

urlpatterns = [

    # ----- guest group -----
    path('register',  use(guest, V.register_create), name='register'),
    path('register',  use(guest, V.register_store)),

    path('login',     use(guest, V.login_create),    name='login'),
    path('login',     use(guest, V.login_store)),

    path('forgot-password', use(guest, V.password_reset_link_create), name='password.request'),
    path('forgot-password', use(guest, V.password_reset_link_store),  name='password.email'),

    path('reset-password/<str:token>', use(guest, V.password_reset_create), name='password.reset'),
    path('reset-password',             use(guest, V.password_reset_store),  name='password.store'),

    # ----- auth group -----
    path('verify-email', use(authn, V.verification_notice), name='verification.notice'),

    path(
        'verify-email/<int:id>/<str:hash>',
        use(
            authn + [
                signed_required(param='sig', max_age=3600),     # like Laravel 'signed'
                ratelimit(key='ip', rate='6/m', method='GET', block=True),  # like 'throttle:6,1'
            ],
            V.verify_email
        ),
        name='verification.verify'
    ),

    path(
        'email/verification-notification',
        use(
            authn + [ratelimit(key='ip', rate='6/m', method='POST', block=True)],
            V.verification_send
        ),
        name='verification.send'
    ),

    path('confirm-password', use(authn, V.password_confirm_show), name='password.confirm'),
    path('confirm-password', use(authn, V.password_confirm_store)),

    path('password', use(authn, V.password_update), name='password.update'),

    path('logout', use(authn, V.logout_destroy), name='logout'),
]