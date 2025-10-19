from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.core.signing import SignatureExpired, BadSignature, TimestampSigner
from functools import wraps

def guest_required(redirect_to='auth:login'):
    """Only allow not-logged-in users."""
    return user_passes_test(lambda u: not u.is_authenticated, login_url=redirect_to)

def signed_required(param='sig', max_age=3600):
    """
    Require a valid timestamped signature in ?sig=...
    Sign with: TimestampSigner().sign(str(payload_or_path))
    """
    def decorator(view):
        @wraps(view)
        def _wrapped(request, *args, **kwargs):
            sig = request.GET.get(param)
            if not sig:
                return HttpResponseForbidden("Missing signature")
            signer = TimestampSigner()
            try:
                # simple example: we sign the request.path
                signer.unsign(sig, max_age=max_age)
            except (BadSignature, SignatureExpired):
                return HttpResponseForbidden("Invalid/expired signature")
            return view(request, *args, **kwargs)
        return _wrapped
    return decorator
