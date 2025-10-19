from .app import APP_URL
from django.urls import reverse_lazy

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# (Nice defaults for local dev)
LOGIN_URL = reverse_lazy('auth:login')
LOGOUT_REDIRECT_URL = 'auth:login'
LOGIN_REDIRECT_URL = 'web:dashboard'

# Optional: email-first auth (vs username)
# ACCOUNT_LOGIN_METHODS = {"email"}  # or "email"
# ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*"]
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False                 # set False if you want email-only
ACCOUNT_EMAIL_VERIFICATION = "optional"            # "mandatory" in prod


# HEADLESS_FRONTEND_URLS = {
#     "account_confirm_email": APP_URL + "/account/verify-email/{key}",
#     "account_reset_password_from_key": APP_URL + "/account/password/reset/key/{key}",
#     "account_signup": APP_URL + "/account/signup",
# }

HEADLESS_FRONTEND_URLS = {
    "account_confirm_email":            f"{APP_URL}/account/verify-email/{{key}}",
    "account_reset_password":           f"{APP_URL}/account/password/reset",
    "account_reset_password_from_key":  f"{APP_URL}/account/password/reset/key/{{key}}",
    "account_signup":                   f"{APP_URL}/account/signup",
    "socialaccount_login_error":        f"{APP_URL}/account/provider/callback",
}

HEADLESS_ONLY = True