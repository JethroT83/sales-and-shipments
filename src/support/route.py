from django.http import HttpResponseNotAllowed

def route(*decorators, **handlers):
    """
    handlers: get=..., post=..., put=..., delete=..., patch=...
    decorators: optional decorators to wrap the final view (e.g., guest_required(), ratelimit(...))
    """
    method_map = {k.upper(): v for k, v in handlers.items() if v}

    def view(request, *args, **kwargs):
        h = method_map.get(request.method)
        if not h:
            return HttpResponseNotAllowed(list(method_map))
        return h(request, *args, **kwargs)

    for d in decorators:
        view = d(view)
    return view
