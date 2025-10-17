from django.http import Http404

class HideAdminFromNonSuperusersMiddleware:
    """
    اگر کاربر سوپریوزر نباشد، مسیر /admin/ را 404 می‌کنیم تا وجودش لو نرود.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if path.startswith('/admin/'):
            user = getattr(request, 'user', None)
            if not (user and user.is_authenticated and user.is_superuser):
                raise Http404("Page not found")
        return self.get_response(request)
