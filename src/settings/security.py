from support.helpers import env, base_path
from pathlib import Path
from .app import APP_URL
from .app import WEB_URL
from urllib.parse import urlparse

# CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]
# CORS_ALLOW_CREDENTIALS = True
# CSRF_TRUSTED_ORIGINS = ["http://localhost:5173"]
#
# REST_USE_JWT = True
# from datetime import timedelta
# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
#     "AUTH_HEADER_TYPES": ("Bearer",),
# }
# # dj-rest-auth cookie names (optional but handy)
# JWT_AUTH_COOKIE = "access"           # access token cookie
# JWT_AUTH_REFRESH_COOKIE = "refresh"  # refresh token cookie
# JWT_AUTH_SECURE = False              # True in prod (HTTPS)
# JWT_AUTH_SAMESITE = "Lax"            # "None" if cross-site + HTTPS

# Hosts / CORS
#ALLOWED_HOSTS = env("ALLOWED_HOSTS", [urlparse(APP_URL).hostname, '192.168.1.183'], cast=list)
ALLOWED_HOSTS = env("ALLOWED_HOSTS", ['*'], cast=list) # e.g. "api.example.com,admin.example.com"
CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS", [WEB_URL], cast=list)  # e.g. "https://app.example.com"
# CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS", [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
#     "http://host.docker.internal:5173"
# ], cast=list)  # e.g. "https://app.example.com"
CORS_ALLOW_CREDENTIALS = env("CORS_ALLOW_CREDENTIALS", True, cast=bool)
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS", [WEB_URL], cast=list)  # e.g. "https://app.example.com"
# CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS", [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
#     "http://host.docker.internal:5173"
# ], cast=list)  # e.g. "https://app.example.com"

# Security (tune as you deploy behind HTTPS)
SECURE_SSL_REDIRECT = False #env("SECURE_SSL_REDIRECT", True, cast=bool)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = env("SECURE_HSTS_SECONDS", 0, cast=int)      # set >0 when ready (e.g., 31536000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env("SECURE_HSTS_INCLUDE_SUBDOMAINS", False, cast=bool)
SECURE_HSTS_PRELOAD = env("SECURE_HSTS_PRELOAD", False, cast=bool)

# JWT cookie behavior (only if you’re using dj-rest-auth + SimpleJWT)
JWT_AUTH_SECURE = env("JWT_AUTH_SECURE", True, cast=bool)
JWT_AUTH_SAMESITE = env("JWT_AUTH_SAMESITE", "None")  # "None" if cross-site + HTTPS, else "Lax"

