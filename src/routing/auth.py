from django.urls import path
from django.contrib.auth.decorators import login_required
# from ratelimit.decorators import ratelimit
from app.http.decorators.auth import guest_required, signed_required
from support.route import route
from app.http.views.auth import authenticate_session

guest = [guest_required()]            # unauthenticated only
authn = [login_required]              # must be authenticated

urlpatterns = [

    # ----- guest group -----
    # path('register',  use(guest, authenticate_session.register_create), name='register'),
    # path('register',  use(guest, authenticate_session.register_store)),

    # path('login', middleware(guest, authenticate_session.create), name='login'),
    # path('login', middleware(guest, authenticate_session.store)),

    path(
        "login",
        route(
            get=authenticate_session.create,
            post=authenticate_session.store,
        ),
        name="login",
    ),


    # path('forgot-password', use(guest, authenticate_session.password_reset_link_create), name='password.request'),
    # path('forgot-password', use(guest, authenticate_session.password_reset_link_store),  name='password.email'),
    #
    # path('reset-password/<str:token>', use(guest, authenticate_session.password_reset_create), name='password.reset'),
    # path('reset-password',             use(guest, authenticate_session.password_reset_store),  name='password.store'),

    # ----- auth group -----
    # path('verify-email', use(authn, authenticate_session.verification_notice), name='verification.notice'),
    #
    # path(
    #     'verify-email/<int:id>/<str:hash>',
    #     use(
    #         authn + [
    #             signed_required(param='sig', max_age=3600),     # like Laravel 'signed'
    #             ratelimit(key='ip', rate='6/m', method='GET', block=True),  # like 'throttle:6,1'
    #         ],
    #         authenticate_session.verify_email
    #     ),
    #     name='verification.verify'
    # ),
    #
    # path(
    #     'email/verification-notification',
    #     use(
    #         authn + [ratelimit(key='ip', rate='6/m', method='POST', block=True)],
    #         authenticate_session.verification_send
    #     ),
    #     name='verification.send'
    # ),
    #
    # path('confirm-password', use(authn, authenticate_session.password_confirm_show), name='password.confirm'),
    # path('confirm-password', use(authn, authenticate_session.password_confirm_store)),
    #
    # path('password', use(authn, authenticate_session.password_update), name='password.update'),
    #
    # path('logout', use(authn, authenticate_session.logout_destroy), name='logout'),
]